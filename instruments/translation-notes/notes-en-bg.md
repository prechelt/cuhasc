# CVscale translation notes: English → Bulgarian

**Source language:** English · **Target language:** Bulgarian (български)

Files written to `instruments/`:
- `cvscale-bg.tsv` — 26 items across the five groups
- `dimensions-bg.csv` — dimension names, English kept after " / "
- `scales-bg.csv` — Likert anchors (`пълно несъгласие`…`пълно съгласие`; `съвсем неважно`…`много важно`)

## Target-language characterization

Bulgarian is South Slavic and Cyrillic-written, but typologically the odd one out in the family:
it has **lost nominal case** and **lost the infinitive**, and it **postposes the definite
article**. That makes it structurally closer to the Balkan sprachbund than to Russian, and it
changes which of the rules bite. Five features drove the item-level choices:

- **Register / variety split.** The written standard is uniform — there is no regional split a
  questionnaire would have to navigate. The real axis is a **vertical** one: Bulgarian's formal
  register carries a thick layer of Russian and Church Slavonic borrowings, and a translator
  working from a Russian model can produce text that *looks* правилен and is in fact a
  Russianism. One such trap fired here (UN1 `разписан`, below). I took the everyday-standard
  layer throughout, so no item depends on the respondent's education level.
- **No infinitive.** Every English infinitive becomes a `да` + finite-verb clause. This is a
  quiet gift for the gender rule: `да` clauses take **present-tense** verbs, which are
  gender-free, whereas Bulgarian past participles and predicate adjectives are gendered.
  UN1's "so that I always know" is therefore `за да знам` — no agreement slot at all.
- **Obligatory definiteness.** The postposed article forces a call English leaves open. Bulgarian
  generic plurals take the article, so `Хората на по-високи длъжности`, `Индивидите`, `Мъжете`
  are all definite where English has a bare plural. This is the neutral generic reading in
  Bulgarian and adds nothing the source lacks.
- **Derivational transparency (inverse-UNI risk).** As in the other Slavic versions, shared stems
  can forge links the source keeps apart. Two were steered around: LT6 "working hard" must not
  reach for `упорит-` (that stem belongs to LT2 `упоритост`), and MA3 "forcible" must not reach
  for `решител-` (LT2 again, `Решително`). Conversely Bulgarian hands us one link for free that
  Polish could not have: `индивид` → `индивидуален` reproduces the source's own
  *individuals*/*individual* stem tie exactly across CO1–CO6.
- **Connotation.** Bulgarian organizational vocabulary is not more deferential than English, so PO
  needed no de-amplification. The one CON pressure point is the modal `трябва` (below).

Bulgarian's genuinely hard spot is the **agreement scale**, where — unlike Ukrainian, and exactly
like Russian — convention and gender-neutrality actually conflict.

## 1. `disagree5` anchors — convention vs. gender-neutrality (the one real conflict)

Bulgarian's stative "to agree" is **`съгласен съм`**, built on an adjective that is gendered:
`съгласен` (m) / `съгласна` (f). The most frequent anchor in Bulgarian scientific questionnaires
is accordingly **A) `напълно несъгласен` … `напълно съгласен`** — masculine forms used
generically. This is the Russian situation, not the Ukrainian one: Ukrainian's conventional
anchor `повністю погоджуюся` happens to be a present-tense verb and is gender-free for free, so
there the two rules agree. Bulgarian gets no such luck.

Three ways out were considered:

- **A) `напълно несъгласен` / `напълно съгласен`** — the most conventional; masculine generic.
  Marks the respondent's gender in an instrument whose MA group *measures* gender attitudes.
- **B) `напълно не се съгласявам` / `напълно се съгласявам`** — present-tense verb, gender-free,
  and the direct analogue of the Ukrainian anchor. But `съгласявам се` in Bulgarian is the
  **process/consent** verb ("I consent", "I come round to agreeing"), not the stative "I hold the
  same view". The item asks about a held position, so B mis-aspects it.
- **C) `пълно несъгласие` / `пълно съгласие`** — nominal ("complete disagreement/agreement").
  Both nouns are neuter, so `пълно` agrees with the *noun*, not the respondent: gender is
  structurally invisible, not merely avoided. Nominal anchors are a recognized and current
  Bulgarian survey form.

Chose **C**. The decisive argument: it is the only variant that satisfies *both* rules rather
than trading one off. It is also the solution the **Romanian** version in this same set arrived at
independently for the same reason (`dezacord total` / `acord total`), and Italian/Spanish dodge
the identical gender problem with the same nominal/prepositional move. C does depart from the
single most frequent Bulgarian anchor form (A), which is why the skill's "use the conventional
translation" instruction deserved a second look — but "conventional" here names a *family* of
current forms, not one string, and C is inside it. B was ruled out on semantics, not on style.

A pleasant side effect: `несъгласие` in the anchor now echoes `изразяват несъгласие` in PO4,
mirroring the source's own echo between "strongly **disagree**" and PO4's "should not
**disagree**".

## 2. "Individuals" (CO1, CO2, CO5) — `индивидите` and its colloquial shadow (CON / UNI)

Variants: **A) `Индивидите`** (the individuals) vs. **B) `Отделният човек`** (the individual
person) vs. **C) `Личността`** (the person/personality — and `личност–група` is a standard
collocation in Bulgarian psychology).

The subtlety is that `индивид` is register-split in a way English "individual" is not. In
scientific writing it is the neutral sociological term; in colloquial Bulgarian it is faintly
**dismissive** — `някакъв индивид` is roughly "some character", the way English "specimen" can be.
That is a CON risk: it could tint the CO items with a contempt the source does not have.

B and C both dissolve the risk but break the source's morphology. English ties *individuals*
(CO1, CO2, CO5) to *individual* (CO3 `individual rewards`, CO4 `individual success`, CO6
`individual goals`) by a shared stem. Bulgarian's only possible adjective there is
`индивидуален` — which is entirely neutral, with none of the noun's colloquial shadow. Pick B or
C and the noun/adjective link is severed for no gain; `отделният човек` … `индивидуалните цели`
reads as two unrelated concepts.

Chose **A**. Decisive: the item's own frame disambiguates the register. Standing in explicit
opposition to `групата`, in a written questionnaire, `индивидите` can only be read as the
sociological term — the dismissive sense needs a colloquial context and an indefinite,
evaluative frame (`някакъв`) that is absent here. So the CON risk is foreclosed by context, while
the UNI gain is real and unconditional. This is the one place Bulgarian does *better* than Polish,
which had to abandon the same stem link because `jednostkowy` means "unitary".

## 3. UN5 "operations" — the same polysemy trap Polish hit, sprung slightly differently (AMB)

"Instructions for operations are important." The literal **B) `Инструкциите за операции`** fails:
Bulgarian `операция` denotes, in order of salience, a **surgical** operation, a **military** one,
and a **financial transaction**. The bland English sense of "a thing done at work" is not among
its live readings. English "operations" carries no such ambiguity, so B violates AMB.

**C) `Инструкциите за работните операции`** was the near-miss worth weighing: the modifier
`работни` does forecloses the surgical and military senses, the way `на по-високи длъжности`
forecloses the second sense of `длъжност` elsewhere in this file. But it leaves the financial
reading half-alive (`работни операции` sits close to accounting usage), and it buys the rescue by
adding a word the source does not have.

Chose **A) `Инструкциите за извършване на работните дейности`** ("instructions for carrying out
work activities"), where `дейности` is the neutral Bulgarian word for work operations and
`извършване` carries the "operations = things done" sense that `дейности` alone would lose.
Decisive: it is unambiguous outright rather than disambiguated by a crutch modifier, and it stays
lexically distinct from `процедури` (UN2, UN4), a distinction the source makes and I had to keep.
`Инструкции` is retained across UN1, UN2 and UN5 to preserve the source's own repetition (UNI).

## Structural / uniformity notes

- **`трябва да` for "should" (CON).** Bulgarian has no crisp separate "should": `трябва да` is the
  general deontic covering both "must" and "should", with strength read off the context, while
  `би трябвало да` adds a speculative/evidential hedge ("presumably ought to") that lands *below*
  the source. Ten items use "should" (all of PO, plus CO1/CO2/CO5/CO6), so consistency matters
  more than a per-item tuning: `трябва да` throughout, and `не трябва да` for "should not" —
  which keeps the modal uniform across the positive and negative PO items exactly as the source
  does. `не бива да` ("it is not proper to") was tempting for PO2/PO4/PO5 but would have split
  the modal across the group.
- **UN1 `разписани` — a Russianism caught (register).** The obvious rendering of "spelled out in
  detail", modelled on Russian `детально расписаны`, is `подробно разписани`. But Bulgarian
  `разписвам се` means **"to sign one's name"**, and `разписание` is a *timetable*; the Russian
  sense of "written out in full" does not carry over. Used `подробно описани` instead. The clause
  `какво се очаква от мен` is reused verbatim in UN3, mirroring the source's repetition of "what
  is expected of me" (UNI).
- **UN3 "rules and regulations"** → `Правилата и разпоредбите`. `предписания` was rejected despite
  being the Russian cognate: in Bulgarian a `предписание` is first of all a **medical
  prescription** (AMB).
- **"people in higher/lower positions"** → `хората на по-високи/по-ниски длъжности`, identical in
  all five PO items. `длъжност` (job post) beats `позиция`, which is both a corporate calque and
  ambiguous with "stance on an issue" — Bulgarian `длъжност` has no such twin sense, so this is a
  cleaner call than the Polish `stanowisko` one.
- **PO3 "social interaction"** → `неформалното общуване` (informal socializing), not `социално
  взаимодействие`, which is sociology jargon and would wrongly sweep in work interaction (SEM).
  Matches the Russian and Ukrainian handling.
- **PO5 "delegate"** → `възлагат` (assign/entrust). `делегирам` exists but is bureaucratic and
  collocates with *authority*, not tasks.
- **CO2 vs. CO6.** CO2 "stick with the group" → `да остават с групата` (cohesion), deliberately
  kept clear of the `лоялност` field that belongs to CO6, so the two items stay as distinct as
  the source keeps them. CO6 "loyalty" → `лоялността`, not `вярност`, which in Bulgarian leans
  toward marital fidelity.
- **"welfare of the group"** → `благополучието на групата`, identical in CO3 and CO5 (UNI).
  `благосъстояние` was rejected as narrowing to material prosperity. CO1's "sacrifice
  self-interest **for the group**" is plain `заради групата` — adding `благото` there would forge
  a CO3/CO5 link the source does not make.
- **"tasks" (PO5) vs. "jobs" (MA4)** stay distinct, as in the source: `задачи` and `видове работа`.
  MA4 "can always do better" → `винаги ще свърши по-добре` (perfective future), the generic-
  capability form; `може да` would tilt toward permission/possibility. Same call as the Russian,
  Ukrainian, Polish and French versions.
- **"success in the future"** → `заради успеха в бъдеще`, identical in LT5 and LT6 (UNI); `успех`
  is also the CO4 word, as in the source.
- **LT glosses** are lowercased per Bulgarian orthography (as in the Russian, Ukrainian and Polish
  versions). "Thrift" → `пестеливост`, the positively-valenced thrift term (`скъперничество` =
  miserliness would invert the valence, CON). "Persistence" → `упоритост`, the standard Bulgarian
  Hofstede term and positive in ordinary use (`инат` is the negative one). LT3 "steadiness" →
  `устойчивост`, kept clear of `упоритост` so the source's LT2/LT3 separation survives; the
  `устойчиво развитие` ("sustainable development") sense of the word is foreclosed by `лична`.
  LT6 is `Усърдна работа`, **not** `упорита работа` — inverse UNI (see characterization).
- **MA3 "active, forcible"** → `активен, напорист`. `силов` is far too strong (Bulgarian
  `силов подход` means the use of force); `енергичен` is a near-synonym of `активен` and would
  make the pair redundant; `решителен` would forge the LT2 link. `напорист` carries the
  assertive-force nuance while staying genuinely distinct from `активен` (CON).
- **Dimension names** use established Bulgarian Hofstede terminology: `дистанция на властта`,
  `избягване на несигурността`, `колективизъм`, `дългосрочна ориентация`. For MA I chose
  `маскулинност` (the technical loan) over `мъжественост` ("manliness/virility"), which carries a
  valorizing charge the neutral dimension name should not have (CON) — the same call German,
  Russian and Italian made.
- **`important5` anchors** pose no gender problem: `важно`/`неважно` are neuter predicatives.
  Following the Russian and Polish precedent I did not translate "very unimportant" literally —
  Bulgarian, like them, disprefers *много* + a negated adjective (`много неважно` sounds wrong).
  `съвсем неважно` ("completely unimportant") is what Bulgarian questionnaires actually use.

## Confidence

No capability caveat applies: Bulgarian is well-resourced for me and every source item has a
natural, register-stable Bulgarian equivalent. The genuine difficulties were the three flagged
above. Only the first is a real compromise — Bulgarian, like Russian and unlike Ukrainian, has no
gendered-free *conventional* stative agreement anchor, and I resolved it by moving to a nominal
anchor that is current in Bulgarian surveys rather than by accepting a masculine generic. The
other two have clean resolutions. The Bulgarian-specific hazard worth remembering is not gender
but the **Russianism layer**: Bulgarian's formal register borrows heavily enough from Russian that
plausible-looking cognates (`разписан`, `предписание`) mean something else, and each had to be
checked against Bulgarian usage rather than trusted from the Russian version.
