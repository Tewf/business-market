"""A bottom-up market size as an interval, set beside a top-down one, from a small toml file.

A tool, not a check: it has no NAME and no check(), so the standard's runner imports it and skips it.
Run it:  python3 checks/local/market_size.py checks/local/market.toml

Bottom-up: for each segment, size = customers x adoption x frequency x price, a yearly amount of money. Segments add up.
Top-down: the size of a published market x the share a venture could reach. The two are set side by side, as
evidence/market-structure/baseline.md asks, and the gap between them is reported, not hidden.

Every input is an interval {low, high} and carries status = "PROVISIONAL" (a guess nobody has measured), or status =
"MEASURED" with a source. A point is refused: one number says nothing about how far to trust it (Soll 2004).
All inputs are positive, so the interval of a product is the product of the ends; no sampling is needed.
Time O(inputs); space O(inputs). Standard library only (tomllib, Python 3.11 and after).
"""
import math
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

FACTORS = ("customers", "adoption", "frequency", "price")
PROVISIONAL = "PROVISIONAL"
MEASURED = "MEASURED"


class MarketError(ValueError):
    """A file or an input that cannot be read as a market size."""


@dataclass(frozen=True)
class Interval:
    low: float
    high: float

    def times(self, other: "Interval") -> "Interval":
        return Interval(self.low * other.low, self.high * other.high)

    def plus(self, other: "Interval") -> "Interval":
        return Interval(self.low + other.low, self.high + other.high)

    @property
    def centre(self) -> float:
        """The geometric centre: the middle on a ratio scale, where an interval of money lives."""
        return math.sqrt(self.low * self.high)

    @property
    def spread(self) -> float:
        """The ratio of the high end to the low end; 1 would be a point."""
        return self.high / self.low


@dataclass(frozen=True)
class Gap:
    overlap: bool
    ratio: float  # top-down centre over bottom-up centre; above 1 means top-down is the larger
    centre_bottom_up: float
    centre_top_down: float


@dataclass(frozen=True)
class Sizing:
    bottom_up: Interval
    segments: dict[str, Interval]
    drivers: dict[str, float]  # share of the width (in logs) that each factor brings, summing to 1
    top_down: Interval | None
    gap: Gap | None
    provisional: int
    measured: int


def read_interval(table: object, where: str) -> tuple[Interval, str]:
    """An input {low, high, status, source}: the interval and its status, or a named refusal."""
    if not isinstance(table, dict):
        raise MarketError(f"{where}: expected a table with low, high and status")
    status = table.get("status")
    if status == MEASURED:
        if not str(table.get("source", "")).strip():
            raise MarketError(f"{where}: a MEASURED input says where it was measured (source)")
    elif status != PROVISIONAL:
        raise MarketError(f"{where}: status must be {PROVISIONAL}, or {MEASURED} with a source")
    values = []
    for end in ("low", "high"):
        value = table.get(end)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise MarketError(f"{where}: {end} must be a positive number")
        values.append(float(value))
    low, high = values
    if low == high:
        raise MarketError(f"{where}: low and high are equal, which is a point; give an interval")
    if low > high:
        raise MarketError(f"{where}: low is above high")
    return Interval(low, high), status


def read_file(path: str | Path) -> dict:
    try:
        with open(path, "rb") as handle:
            return tomllib.load(handle)
    except tomllib.TOMLDecodeError as error:
        raise MarketError(f"{path}: not valid toml ({error})") from None


def size(document: dict) -> Sizing:
    """The bottom-up interval, where its width comes from, and the top-down one with the gap, if given."""
    segments_in = document.get("segment")
    if not isinstance(segments_in, list) or not segments_in:
        raise MarketError("the file needs at least one [[segment]]")
    counts = {PROVISIONAL: 0, MEASURED: 0}
    segments: dict[str, Interval] = {}
    log_width = {factor: 0.0 for factor in FACTORS}
    total = None
    for number, segment in enumerate(segments_in, start=1):
        name = str(segment.get("name", f"segment {number}"))
        if name in segments:
            raise MarketError(f"segment '{name}' appears twice")
        product = None
        parts = {}
        for factor in FACTORS:
            interval, status = read_interval(segment.get(factor), f"segment '{name}' {factor}")
            counts[status] += 1
            parts[factor] = interval
            product = interval if product is None else product.times(interval)
        weight = product.centre
        width = sum(math.log(parts[factor].spread) for factor in FACTORS)
        for factor in FACTORS:  # a segment's width is shared among its factors; big segments count for more
            log_width[factor] += weight * math.log(parts[factor].spread) / width
        segments[name] = product
        total = product if total is None else total.plus(product)
    weight_sum = sum(log_width.values())
    drivers = {factor: log_width[factor] / weight_sum for factor in FACTORS}

    top_down = None
    gap = None
    section = document.get("top_down")
    if section is not None:
        market, status_market = read_interval(section.get("market"), "top_down market")
        share, status_share = read_interval(section.get("share"), "top_down share")
        counts[status_market] += 1
        counts[status_share] += 1
        top_down = market.times(share)
        gap = Gap(
            overlap=max(total.low, top_down.low) <= min(total.high, top_down.high),
            ratio=top_down.centre / total.centre,
            centre_bottom_up=total.centre,
            centre_top_down=top_down.centre,
        )
    return Sizing(total, segments, drivers, top_down, gap, counts[PROVISIONAL], counts[MEASURED])


def report(result: Sizing, currency: str = "") -> str:
    unit = f" {currency}" if currency else ""
    lines = [f"bottom-up: {result.bottom_up.low:,.0f} to {result.bottom_up.high:,.0f}{unit} a year "
             f"(spread {result.bottom_up.spread:.1f}x)"]
    for name, interval in result.segments.items():
        lines.append(f"  segment {name}: {interval.low:,.0f} to {interval.high:,.0f}")
    drivers = ", ".join(f"{factor} {share:.0%}" for factor, share in sorted(result.drivers.items(), key=lambda kv: -kv[1]))
    lines.append(f"width comes from: {drivers}")
    if result.top_down is not None and result.gap is not None:
        lines.append(f"top-down: {result.top_down.low:,.0f} to {result.top_down.high:,.0f}{unit} a year")
        lines.append(f"gap: the intervals {'overlap' if result.gap.overlap else 'do not overlap'}; "
                     f"top-down centre is {result.gap.ratio:.2f} times the bottom-up centre")
    else:
        lines.append("top-down: not given, so no gap to report")
    lines.append(f"inputs: {result.provisional} PROVISIONAL, {result.measured} MEASURED")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: market_size.py MARKET.toml")
        return 2
    try:
        document = read_file(argv[1])
        print(report(size(document), str(document.get("currency", ""))))
    except (MarketError, OSError) as error:
        print(f"error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
