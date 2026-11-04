# 0002: Keep the name, and size a market by two methods with intervals

**Decision:** The repository keeps its name after the frame step. The baseline of its first review is B1: a market sized bottom-up and top-down, every input an interval tagged PROVISIONAL, the gap reported, beside a competition frame of four questions.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The frame step found the field's words: industrial organisation for structure and entry, forecasting for size, two-sided markets for platforms, mass customization for tailoring ([frame](../evidence/market-structure/frame.md)).
- "Market" is the practitioners' word and covers all of them, so the mismatch is partial.
- The review found two sizes of one company 25 times apart on a single premise: whether the product expands the market.
- It found no study of the error of a venture's size ([review](../evidence/market-structure/review.md)).
- The review is finished only when it names a baseline.

## Decision

- Keep the name. A rename moves the address for no gain.
- Name the baseline B1: a bottom-up size from segments, a top-down size from a published market and a share, both as intervals, with the premise behind the gap named.
- Refuse a point in the program: one number says nothing about how far to trust it, and stated intervals are known to be too narrow ([against](../evidence/market-structure/against.md)).
- Name the evidence topic market-structure, the field's word.

## Consequences

- A reader can compare any sizing with B1 and with the studies that bear on each of its parts.
- The program `checks/local/market_size.py` computes the intervals, the gap and the input that brings most of the width; its tests run in CI.
- **Bad:** B1 reports a width, not an accuracy, since no source measures how far a sizing falls from later sales.
- **Bad:** the evidence for combining two levels is on series of existing sales, so B1 sets the two sizes side by side and does not reconcile them.

## See also

[Decisions](README.md); [baseline](../evidence/market-structure/baseline.md); [record 0001](0001-a-repository-of-its-own.md).
