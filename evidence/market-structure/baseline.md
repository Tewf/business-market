# Baseline

Step 5 of the review: the baseline the work is compared against. Evidence is in [review](review.md).

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/baseline.md)

## B1: a market sized by two methods with intervals, and a competition frame of four questions

1. Split the market into segments. For each, write customers, adoption, frequency and price, each as a low and a high, each tagged PROVISIONAL. The program `checks/local/market_size.py` multiplies the ends and adds the segments.
2. Size the same market top-down: a published market times a reachable share, each an interval, each tagged.
3. Report both intervals, whether they overlap, the ratio of their centres and the input that brings most of the width.
4. Name the premise that explains the gap, above all whether the product expands the market, and say which side of it each size takes.
5. Ask four things of the competition before any data of your own.
   - How many rivals the segment holds.
   - Whether a difference is horizontal or vertical, and what it costs a rival to copy.
   - What it costs a customer to switch.
   - Whether the venture is a two-sided market by the two conditions of Rysman 2009.

The single top-down figure of practice is the thing B1 is compared with.

## Compared with what the review found

| Item | In B1 | Fit |
|---|---|---|
| Intervals, not points (Soll 2004) | every input is an interval; a point is refused | matches |
| Splitting into parts helps for extreme, uncertain targets (MacGregor 1994) | the bottom-up is a product of four parts | matches |
| Two levels, reconciled (Athanasopoulos 2009; Hyndman 2011) | both are shown and compared, not reconciled | in part |
| A ceiling from early sales is biased (Van den Bulte 1997) | no sales are used | matches |
| The premise behind a gap (Damodaran 2014; Gurley 2014) | named in step 4 | matches |
| Few rivals change conduct (Bresnahan 1991) | the count of rivals is asked | in part |
| What lasts is business-specific (Rumelt 1991; McGahan 1997) | the cost of copying a difference is asked | in part |
| A two-sided test (Rysman 2009) | asked before pricing | matches |
| Cost of variety (Randall 2001) | not asked | lacks |

## What B1 lacks

- A measured error: no source gives how far a sizing of this kind falls from later sales, so B1 reports a width and not an accuracy (position, Not found).
- Weights to combine the two sizes, since the evidence for combining is on series of existing sales (Athanasopoulos 2009).
- The cost side of variety (Randall 2001).
- A field effect of personalisation on rivalry (position, Not found).

## How it is measured

- The width of the bottom-up interval, as the ratio of its high end to its low end, and the share of the width each input brings, by the program.
- Whether the two intervals overlap, and the ratio of their centres.
- Later, coverage: over several sizings, the share whose interval contained the revenue actually made, set against the confidence claimed.
- A repeat: the program runs on any such file, and its tests pass on a fictional one with no real figure.

## The review is finished

The baseline is named: B1. The next work is a design document that fixes one example market and the sale that closes the loop.
