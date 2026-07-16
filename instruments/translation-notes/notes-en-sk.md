# CVscale translation notes: English → Slovak

**Source language:** English · **Target language:** Slovak (slovenčina)

Files written to `instruments/`:
- `cvscale-sk.tsv` — 26 items across the five groups
- `dimensions-sk.csv` — dimension names, English kept after " / "
- `scales-sk.csv` — conventional Likert anchors (`rozhodne nesúhlasím`…`rozhodne súhlasím`;
  `úplne nedôležité`…`veľmi dôležité`)

## Target-language characterization

Slovak is a West Slavic language, extremely close to Czech (largely mutually intelligible), and
most of the Czech translation's decisions carry over. Four features shaped the item-level work:

- **Register / variety.** Unlike Czech, Slovak is *not* strongly diglossic: there is no
  everyday spoken variety comparable to Czech *obecná čeština* that competes with the written
  standard, and questionnaire Slovak uniformly uses *spisovná slovenčina* (standard literary
  Slovak). Central/Western/Eastern dialect differences exist but do not surface in a
  standard-register instrument, so the comparability risk that dominated the Czech notes is
  much milder here. Everything is standard written Slovak.
- **Derivational morphology and one unbreakable stem link.** Shared stems make UNI cheap
  (*skupina* → *skupiny*/*skupine*; *cieľ* → *ciele*). The one link Slovak cannot reproduce is
  the source's *individuals* / *individual*: the sociological noun is *jednotlivec*, but its
  adjective *jednotlivý* means "single, separate, each one", not "pertaining to the individual".
  The adjective must therefore be *individuálny*, a different stem. Semantics beat morphology;
  the broken link is accepted (exactly as in Czech and Polish).
- **A false friend, same as Czech.** "People in higher/lower positions" cannot use *stanovisko*
  (the Slovak cognate of Polish *stanowisko* "job post") because in Slovak *stanovisko* means
  only "standpoint, position on an issue". Slovak uses *pozícia*, disambiguated completely by
  the collocation *na vyšších pozíciách*.
- **Gender marking.** Slovak forces gender on first-person past-tense and conditional verbs and
  on predicate adjectives. Only UN1 is first-person and it needed restructuring (below).
  Elsewhere *ľudia* ("people") and *jednotlivci* keep gender invisible, and the scale anchors
  use present-tense verbs (*súhlasím*), which are gender-free.

Because of the Czech proximity, the translation was largely straightforward. Three decisions
were worth flagging, all inherited-with-checking from the Czech analysis.

## 1. PO4 "should not disagree with decisions" (CON)

Variants: **A) "by nemali nesúhlasiť s rozhodnutiami"** (should not disagree with the
decisions — literal) vs. **B) "by nemali spochybňovať rozhodnutia"** (should not
question/cast doubt on) vs. **C) "by nemali odporovať rozhodnutiam"** (should not
contradict/resist).

As in Czech, the double negation here is unproblematic: the negation is carried by a **bound
prefix** on each of two different words (*ne*-mali *ne*-súhlasiť), which is ordinary Slovak, not
a drafting error (the objection that pushed *Polish* away from its literal option does not
transfer to Slovak either). A is then the only variant that preserves the source's mildness:
English "disagree" is merely holding a contrary view, whereas *spochybňovať* (B) implies voicing
doubt about validity and *odporovať* (C) implies active resistance — both overshoot. Chose **A**;
with the naturalness objection gone, CON is decisive.

## 2. UN1 — first-person gender marking (gender-neutrality rule)

"…so that I always know what I'm expected to do." The natural purpose clause takes *aby som* +
an *l*-participle, which is unavoidably gendered: **A) "aby som vždy vedel"** (masc.) /
*"aby som vždy vedela"* (fem.). Slovak has no neutral form. I restructured instead:
**B) "…vďaka čomu vždy viem, čo sa odo mňa očakáva"** ("…thanks to which I always know what is
expected of me"). Present-tense *viem* carries no gender. The cost is a shift from purpose
("so that") to result ("thanks to which"), which is negligible — the item's force is that
detailed instructions *produce* the knowledge. Chose **B**; gender-neutrality is an explicit
rule. The clause *"čo sa odo mňa očakáva"* is reused verbatim in UN3, mirroring the source's own
repetition of "what is expected of me" across UN1 and UN3 (UNI).

## 3. UN5 "Instructions for operations" — the *operácia* trap (AMB, SEM)

Slovak inherits the same polysemy problem as Czech and Polish: **B) "Pokyny pre operácie"**
fails because *operácia* denotes first a **surgical** operation, secondarily a military one; the
neutral English "a thing done" is not a salient Slovak reading. **C) "Návod na obsluhu"** is the
fixed term for a *product user manual*, relocating the item out of the workplace. **D) "Prevádzkové
pokyny"** ("operating instructions") is idiomatic but *prevádzka* means the running of a plant or
facility, quietly narrowing the item to industrial settings (SEM). Chose
**A) "Pokyny pre pracovné činnosti sú dôležité."** ("instructions for work activities"), where
*činnosti* is the neutral Slovak word for work operations. *Pokyny* is used across UN1, UN2 and
UN5 to preserve the source's within-group repetition of "instructions" (UNI).

## Structural / uniformity notes

- **"people in higher/lower positions"** → *ľudia na vyšších/nižších pozíciách*, identical in all
  five PO items. *Pozícia* was preferred over *funkcia* (skews to formal office-holding) and
  *pracovné miesto* (a headcount slot, not a rank); *nadriadení*/*podriadení* ("superiors"/
  "subordinates") was rejected as presuming a direct reporting line the source does not.
- **PO1 "make most decisions"** → *prijímať väčšinu rozhodnutí*; *prijímať rozhodnutia* is the
  idiomatic Slovak collocation for "to make decisions".
- **PO3 "social interaction"** → *spoločenskému kontaktu* (socializing). *Sociálna interakcia* is
  sociology jargon and would wrongly include work interaction (SEM).
- **CO2 vs. CO6:** CO2 "stick with the group" → *držať sa skupiny* (cohesion), kept lexically
  clear of the *lojalita* field belonging to CO6, so the two items stay distinct as in the source.
- **"welfare of the group"** → *dobro skupiny*, identical in CO3 and CO5 (UNI); *blahobyt* was
  rejected as narrowing to material prosperity. CO1 "sacrifice self-interest **for the group**"
  is *v prospech skupiny* — a fixed "in favour of" phrase that does not lexically echo *dobro*,
  avoiding a CO1–CO3/CO5 link the source does not make.
- **"individual" adjective** → *individuálny/individuálne* across CO3 (*individuálne odmeny*),
  CO4 (*individuálny úspech*) and CO6 (*individuálne ciele*), matching the source's three-fold
  reuse of one word (UNI). CO4 uses *individuálny úspech*, not *úspech jednotlivca*, to keep that
  uniformity rather than opportunistically repairing the conceded *individuals*/*individual* link.
- **"success"** → *úspech* across CO4, LT5 and LT6, with *budúci úspech* identical in LT5 and LT6
  (UNI), as in the source.
- **"tasks" (PO5) vs. "jobs" (MA4)** stay distinct: *úlohy* and *práce*. MA4 "can always do
  better" → *vždy zvládne lepšie* (perfective future), since *môže* would read as permission —
  the same reasoning the Czech, Polish, French and Russian versions applied.
- **MA3 "active, forcible"** → *aktívny, razantný*. *Silový* ("by force") is far too strong and
  carries a coercive colouring the neutral English lacks; *energický* is a near-synonym of
  *aktívny* and would make the pair redundant. *Razantný* ("vigorous, forceful") carries the
  assertive-force nuance while staying a genuinely distinct second adjective (CON).
- **Comparatives** use *než* (*dôležitejšie než*, *lepšie než*); the colloquial *ako* was avoided
  in favour of the more formal standard-register connective appropriate to a questionnaire.
- **Dimension names** use established Slovak Hofstede terminology: *vzdialenosť moci* (the widely
  used alternative *mocenský odstup* was the runner-up), *vyhýbanie sa neistote*, *kolektivizmus*,
  *dlhodobá orientácia*, *maskulinita*.
- **Scale anchors:** *rozhodne nesúhlasím* / *rozhodne súhlasím* is the standard Slovak 5-point
  agreement pair, and its present-tense verbs are gender-free. For importance the conventional
  low anchor is **úplne nedôležité** ("completely unimportant"), not a literal *veľmi nedôležité*,
  which sounds wrong to a Slovak ear for the same reason Czech *zcela nedůležité* / Polish
  *zupełnie nieważne* were preferred; the skill's instruction to use conventional anchors decided
  this over literal symmetry with the source.

## Confidence

No capability caveat applies: Slovak is a well-resourced language and every source item has a
natural, register-stable Slovak equivalent. Its very closeness to Czech makes the translation
largely straightforward — the three genuine difficulties (a forced first-person gender marking,
the *operácia* polysemy trap, and the PO4 connotation call) are the same the Czech version faced
and resolve the same way, and unlike Czech vs. Polish there was no false-friend surprise that
forced a divergence.
