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
