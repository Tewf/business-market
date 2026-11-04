# Protocol: how the pool was built

A first pass, run on 2026-11-04 by one reviewer, a language model working under the maintainer's direction. Terms are in [frame](frame.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/protocol.md)

## 1. Why grey literature

Garousi's seven questions (Table 4), paraphrased and answered for this topic. One yes suggests including grey sources (Garousi 2019).

| Question | Answer |
|---|---|
| Is the subject too complex for the formal literature alone? | no |
| Is there a lack of volume or quality in the formal literature? | yes: no study measuring the error of a venture's market size was found |
| Is the context important to the results? | yes: a size is argued in a pitch, a valuation note or a blog |
| Is the goal to corroborate science with practice? | yes: the moat and the five forces are practice words for theory |
| Is the goal to challenge practice with evidence, or the reverse? | yes: practice quotes one top-down figure |
| Would a synthesis of both communities help? | yes |
| Is there a large volume of practitioner sources showing interest? | yes: guides to the total addressable market are many |

## 2. Questions

- Q1 how far apart do top-down and bottom-up sizes fall, and which assumptions explain the gap?
- Q2 which differences can a rival copy, and what does the literature say lasts?
- Q3 when is a venture a two-sided market, and what does that change in how it prices?
- Q4 what does tailoring a product do to rivalry, switching costs, cost and demand?

## 3. Existing reviews

- Found: surveys of two-sided markets (Rysman 2009; Evans 2003p), of entry (Geroski 1995) and of switching costs (Klemperer 1995).
- Found: surveys of mass customization (Silveira 2001; Fogliatto 2012) and of privacy (Acquisti 2016), and two meta-analyses of choice overload (Scheibehenne 2010; Chernev 2015).
- Not found, in these searches: a review of how far a market size falls from the sales later made (F26, F27).
- Not found, in these searches: a measured comparison of top-down and bottom-up sizes for a new venture.

## 4. Formal search

Database: OpenAlex, title and abstract (a title filter for a named lead), no key and no identity. Counts are of 2026-11-04. Per string, the top 8 by citations were screened, fewer where fewer came back. The shared free quota of the service ran out after F28, so the 42 lookups that fixed a DOI were made in Crossref, one top hit each, and are not searches: they are not tabled.

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | "two-sided markets" survey | 88 | nnynynnn |
| F2 | "platform competition in two-sided markets" | 27 | yynnnynn |
| F3 | "competition in two-sided markets" | 59 | nynnnynn |
| F4 | "price structure" "two-sided markets" evidence | 7 | yynnnnn |
| F5 | "economics of two-sided markets" | 26 | yyynnnnn |
| F6 | "multi-sided platforms" | 850 | yyyynnnn |
| F7 | "product differentiation" "price competition" Hotelling | 48 | ynynynnn |
| F8 | "entry and competition in concentrated markets" | 3 | yny |
| F9 | "what do we know about entry" | 5 | ynnnn |
| F10 | "how much does industry matter" | 12 | yynnnnn |
| F11 | "sustained competitive advantage" imitation | 130 | ynnnynyn |
| F12 | "switching costs" competition overview | 21 | ynnnnn |
| F13 | "behavior-based price discrimination" | 87 | yynyynnn |
| F14 | "mass customization" literature review | 331 | nyynynnn |
| F15 | "product variety" "supply chain" firm performance | 45 | nyynnnnn |
| F16 | "value of increased product variety" | 5 | ynnnn |
| F17 | "choice overload" meta-analysis | 17 | yynnnnn |
| F18 | "top-down" "bottom-up" forecasting aggregate disaggregate | 24 | yyynnnny |
| F19 | "hierarchical forecasting" top-down bottom-up | 46 | nynynnnn |
| F20 | decomposition judgment estimation accuracy | 49 | yynynnnn |
| F21 | "overconfident interval estimates" | 1 | n |
| F22 | "diffusion" "market potential" estimate bias parameter | 3 | nnn |
| F23 | "economics of privacy" | 100 | ynnnynyn |
| F24 | personalization customization choice marketing | 162 | ynnnnn |
| F25 | "recommender systems" "sales diversity" | 18 | yynnnnn |
| F26 | "market size" estimation startups | 3 | nnn |
| F27 | "total addressable market" | 102 | nnnnn |
| F28 | "economic moat" | 44 | nyynnnnn |

The strings F21, F22, F26 and F27 returned nothing usable. A zero or an off-topic hit is a statement about the string. F21 was replaced by a title lookup of Soll 2004, and F22 by one of Van den Bulte 1997. F26 and F27 found no study of a venture's size.

## 5. Grey search

The web searches returned a synthesis, not a list; their rows say `not recorded`. A page read directly has its own row.

| Id | Producer or engine | String or what was read | Result | New concept |
|---|---|---|---|---|
| G1 | web search | Gurley, "How to Miss By a Mile", Uber market size | 16 links; found the post and Damodaran's reply | not recorded |
| G2 | web search | Damodaran, Uber, taxi market, 2014 | 30 links; found his post and the correction of a table | not recorded |
| G3 | web search | Mauboussin, "Measuring the Moat" | 18 links; found three editions, took the 2016 one | not recorded |
| G4 | web search | CB Insights, startup failure, "no market need" | 15 links; the page now reads differently from older write-ups | not recorded |
| G5 | web search | McKinsey, personalisation, "right or wrong" | 15 links; summaries and mirrors | not recorded |
| G6 | web search | abstract of Brynjolfsson 2003 | 10 links; working paper and record | not recorded |
| G7 | web search | abstract of McGahan 1997 | 10 links; the RePEc record | not recorded |
| G8 | web search | abstract of Randall 2001 | 10 links; the record | not recorded |
| G9 | web search | abstract of Athanasopoulos 2009 | 10 links; the author's page and the record | not recorded |
| G10 | web search | abstract of Dangerfield 1992 | 20 links; the design only, no result | not recorded |
| G11 | web search | abstract of Soll 2004 | 20 links; secondary descriptions | not recorded |
| G12 | web search | abstract of Kaiser 2006 | 10 links; the discussion paper and the record | not recorded |
| G13 | web search | abstract of Bresnahan 1991 | 10 links; no threshold values | not recorded |
| G14 | web search | abstract of Geroski 1995 | 10 links; the record | not recorded |
| G15 | web search | abstract of Van den Bulte 1997 | 10 links; the record | not recorded |
| G16 | web search | abstract of MacGregor 1994 | 10 links; the author's copy | not recorded |
| G17 | web search | abstract of Fleder 2009 | 10 links; the repository copy | not recorded |
| G18 | web search | abstract of Zhang 2011p | 10 links; the repository record | not recorded |
| G19 | page | Gurley's post | 1 page; read | y |
| G20 | page | Damodaran's post | 1 page; first 100000 of 114468 characters read | y |
| G21 | page | Mauboussin 2016, the report as a PDF | 1 report; read as text | y |
| G22 | page | CB Insights, startup failure reasons | 1 page; read | y |
| G23 | page | Porter 2008, the article | 1 page; an excerpt, the rest behind a paywall | y |
| G24 | page | Pine 1993, the article | 1 page; the opening, the rest behind a paywall | n |
| G25 | page | Eisenmann 2006, the article | 1 page; the opening, the rest behind a paywall | n |
| G26 | page | McKinsey 2021 article, two mirrors | 2 pages; both timed out, not read | not run |
| G27 | page | a venture investor's guide to modelling the total addressable market | 1 page; resolved to the firm's home page, no content on the method | n |
| G28 | page | Scheibehenne 2010 on the publisher's site | 1 page; abstract read | y |
| G29 | page | INFORMS and Wiley records of four formal sources | 4 pages; answered 403, not bypassed | not run |

## 6. Stopping rule

- Effort bounded: the top 8 results per string by citations, stated before the search.
- Saturation: a string stops after 5 consecutive results that add no concept (F10, F12, F17, F24, F27 stopped so).
- The pool stops at 40 sources, the first-pass ceiling.

## 7. Selection

- Include: a work that measures or models a market size, market structure, entry, the lasting of an advantage or a platform price.
- Include: a work on the effect of variety and personalisation on demand and cost, and the origin of a practice word.
- Exclude: studies of one industry with no point of method; papers on firm technology or on the digital economy at large; blogs that restate a source already kept.

## 8. Quality of grey sources

Garousi's 20 criteria (Table 7) in eight groups: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. The threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- Read in the text: Mauboussin 2016, Gurley 2014, Damodaran 2014 and CB Insights 2026; an excerpt of Porter 2008 and the openings of Pine 1993 and Eisenmann 2006.
- Read from the abstract: 17 formal sources; a figure from one is marked secondary in [review](review.md).
- The synthesis is narrative, by question, and traceable through [sources](sources.md).

## 10. Not searched, and limits

- Not searched: databases other than OpenAlex, Google Scholar, SSRN, the demand estimation of differentiated products in empirical industrial organisation, analyst houses behind a paywall, and the textbooks beyond Tirole 1988.
- Not recorded: the web searches (G1 to G18) returned a synthesis of the results, not a list of them, so no letter per result was kept.
- Not read: fourteen formal sources are located only; the McKinsey article was not opened; the two HBR articles were read at their opening.
- Not bypassed: four publisher records and the HBR bodies answered with a refusal or a paywall; none was circumvented.
- One reviewer, no second rater, no inter-rater agreement. Search engines personalise and change.
