"""Tests of checks/local/market_size.py: hand-worked cases, the refusals, then the fictional fixture.

Run: python3 -m unittest discover -s checks
"""
import contextlib
import importlib.util
import io
import math
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("market_size", HERE / "local" / "market_size.py")
ms = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ms)
FIXTURE = HERE / "local" / "market.toml"


def box(low, high, status="PROVISIONAL", **extra):
    return {"low": low, "high": high, "status": status, **extra}


def segment(name="a", customers=(100, 200), adoption=(0.1, 0.2), frequency=(1, 2), price=(10, 20)):
    return {"name": name, "customers": box(*customers), "adoption": box(*adoption),
            "frequency": box(*frequency), "price": box(*price)}


class Bottom(unittest.TestCase):
    def test_one_segment_by_hand(self):
        # low 100 x 0.1 x 1 x 10 = 100; high 200 x 0.2 x 2 x 20 = 1600
        result = ms.size({"segment": [segment()]})
        self.assertAlmostEqual(result.bottom_up.low, 100)
        self.assertAlmostEqual(result.bottom_up.high, 1600)
        self.assertAlmostEqual(result.bottom_up.spread, 16)

    def test_segments_add_end_to_end(self):
        second = segment("b", customers=(10, 20), adoption=(0.5, 1.0), frequency=(1, 1.5), price=(2, 4))
        # b: low 10 x 0.5 x 1 x 2 = 10; high 20 x 1 x 1.5 x 4 = 120
        result = ms.size({"segment": [segment(), second]})
        self.assertAlmostEqual(result.bottom_up.low, 110)
        self.assertAlmostEqual(result.bottom_up.high, 1720)
        self.assertEqual(set(result.segments), {"a", "b"})

    def test_equal_spreads_share_the_width_equally(self):
        result = ms.size({"segment": [segment()]})
        for share in result.drivers.values():
            self.assertAlmostEqual(share, 0.25)

    def test_the_wide_input_drives_the_width(self):
        wide = segment(price=(10, 1000))
        result = ms.size({"segment": [wide]})
        self.assertEqual(max(result.drivers, key=result.drivers.get), "price")
        self.assertAlmostEqual(sum(result.drivers.values()), 1.0)

    def test_the_interval_never_shrinks_when_an_input_widens(self):
        narrow = ms.size({"segment": [segment()]}).bottom_up
        wider = ms.size({"segment": [segment(price=(5, 40))]}).bottom_up
        self.assertLessEqual(wider.low, narrow.low)
        self.assertGreaterEqual(wider.high, narrow.high)


class Gap(unittest.TestCase):
    def test_gap_by_hand(self):
        document = {"segment": [segment()], "top_down": {"market": box(10000, 20000), "share": box(0.1, 0.2)}}
        result = ms.size(document)
        self.assertAlmostEqual(result.top_down.low, 1000)
        self.assertAlmostEqual(result.top_down.high, 4000)
        self.assertAlmostEqual(result.gap.ratio, math.sqrt(1000 * 4000) / math.sqrt(100 * 1600))
        self.assertTrue(result.gap.overlap)  # [100, 1600] and [1000, 4000] meet between 1000 and 1600

    def test_disjoint_intervals_are_reported(self):
        document = {"segment": [segment()], "top_down": {"market": box(1e6, 2e6), "share": box(0.1, 0.2)}}
        result = ms.size(document)
        self.assertFalse(result.gap.overlap)
        self.assertGreater(result.gap.ratio, 1)

    def test_no_top_down_means_no_gap(self):
        result = ms.size({"segment": [segment()]})
        self.assertIsNone(result.gap)
        self.assertIn("no gap to report", ms.report(result))


class Refusals(unittest.TestCase):
    def refuses(self, document, fragment):
        with self.assertRaises(ms.MarketError) as caught:
            ms.size(document)
        self.assertIn(fragment, str(caught.exception))

    def test_a_point_is_not_an_interval(self):
        self.refuses({"segment": [segment(price=(10, 10))]}, "a point")

    def test_low_above_high(self):
        self.refuses({"segment": [segment(price=(20, 10))]}, "above high")

    def test_untagged_input(self):
        bad = segment()
        bad["price"] = {"low": 10, "high": 20}
        self.refuses({"segment": [bad]}, "PROVISIONAL")

    def test_measured_needs_a_source(self):
        bad = segment()
        bad["price"] = box(10, 20, status="MEASURED")
        self.refuses({"segment": [bad]}, "source")
        bad["price"] = box(10, 20, status="MEASURED", source="a paid pilot")
        result = ms.size({"segment": [bad]})
        self.assertEqual((result.provisional, result.measured), (3, 1))

    def test_not_a_positive_number(self):
        self.refuses({"segment": [segment(price=(0, 20))]}, "positive")
        self.refuses({"segment": [segment(price=(-1, 20))]}, "positive")
        bad = segment()
        bad["price"] = box("ten", 20)
        self.refuses({"segment": [bad]}, "positive")

    def test_missing_pieces(self):
        self.refuses({}, "[[segment]]")
        bad = segment()
        del bad["frequency"]
        self.refuses({"segment": [bad]}, "frequency")
        self.refuses({"segment": [segment(), segment()]}, "twice")

    def test_top_down_inputs_are_checked_too(self):
        self.refuses({"segment": [segment()], "top_down": {"market": box(1, 2), "share": {"low": 0.1, "high": 0.2}}},
                     "PROVISIONAL")


class Fixture(unittest.TestCase):
    def test_fictional_market(self):
        result = ms.size(ms.read_file(FIXTURE))
        # urban households: 40000 x 0.01 x 2 x 18 = 14,400 up to 90000 x 0.04 x 6 x 35 = 756,000
        self.assertAlmostEqual(result.segments["urban households"].low, 14400)
        self.assertAlmostEqual(result.segments["urban households"].high, 756000)
        self.assertAlmostEqual(result.bottom_up.low, 24000)  # pinned: a change here is a change of the fixture
        self.assertAlmostEqual(result.bottom_up.high, 1370400)
        self.assertEqual((result.provisional, result.measured), (10, 0))
        self.assertTrue(result.gap.overlap)

    def test_every_input_of_the_fixture_is_an_interval_and_provisional(self):
        document = ms.read_file(FIXTURE)
        tables = [seg[f] for seg in document["segment"] for f in ms.FACTORS]
        tables += list(document["top_down"].values())
        for table in tables:
            interval, status = ms.read_interval(table, "fixture")
            self.assertEqual(status, "PROVISIONAL")
            self.assertLess(interval.low, interval.high)


class Files(unittest.TestCase):
    def test_bad_toml_is_named(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.toml"
            path.write_text("[[segment\n")
            with self.assertRaises(ms.MarketError):
                ms.read_file(path)

    def test_command_line(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(ms.main(["market_size.py", str(FIXTURE)]), 0)
            self.assertEqual(ms.main(["market_size.py", str(FIXTURE.with_name("nope.toml"))]), 1)
            self.assertEqual(ms.main(["market_size.py"]), 2)
        self.assertIn("bottom-up: 24,000 to 1,370,400 EUR", out.getvalue())


if __name__ == "__main__":
    unittest.main()
