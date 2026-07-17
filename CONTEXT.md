# CuHaSc

CuHaSc (Culture Handbook for Scrum) is a webapp with which a software team determines
its culture profile by having each member fill in the CVSCALE questionnaire.

## Language

**Team**:
The set of all Team Members participating in one culture-profiling process.
This is the only meaning of "group" in this app; the app has no other notion of group.

**Team Member** (often **Member**):
A person in the software development team, including the Culture Lead.

**Culture Lead**:
The person who starts, leads, and moderates the profiling process. Often the Scrum Master.

**Dimension**:
One of the five Hofstede cultural dimensions measured by the questionnaire
(Power Distance, Uncertainty Avoidance, Collectivism, Long-Term Orientation, Masculinity).
Each Dimension corresponds to one item-group, identified by the item-code prefix
(`PO`, `UN`, `CO`, `LT`, `MA`).
_Avoid_: "group", "items group", "category".

**Score**:
A member's mean answer value for the items of one Dimension, in the interval [1, 5].

**Culture Profile**:
One member's result: a Score for each of the five Dimensions.
_Avoid_: "individual evaluation".

**Team Culture Profile**:
A team's aggregate result: the Culture Profiles of all Members plus the per-Dimension
team mean Score. Named to mirror "Culture Profile".
_Avoid_: "OverallCultureProfile", "team evaluation".

**Handbook**:
The collection of Sections, grouped into Chapters, from which Cuhasc advises a Team
about culturally induced execution problems in its agile process.

**Chapter**:
A named group of related Sections in the Handbook.

**Section**:
One piece of advice in the Handbook: a Markdown file (with YAML frontmatter carrying
its `title` and `trigger`) served at its own page.
_Avoid_: "advice" (as a countable noun for one item), "topic", "article".

**Trigger**:
The condition, attached to a Section, that determines whether the Section applies to
a given Team; evaluated against that Team's Team Culture Profile. Written as a single
Predicate call, e.g. `one-high(PO)`.
_Avoid_: "condition" (as a noun for the whole mechanism), "rule".

**Predicate**:
One named test usable inside a Trigger (e.g. `one-high`), taking a Dimension code as
its argument and applying a fixed, code-defined cutoff (e.g. "high" means Score >= 4).
A Predicate's name fixes both its cutoff comparison and whether it looks at individual
Members (`one-high`, `two-high`, `one-low`, `two-low`) or the team mean (`mean-high`,
`mean-low`) — there is no separate syntax for choosing that scope. The set of Predicates is fixed in code and
extended by a developer, not by handbook authors.
