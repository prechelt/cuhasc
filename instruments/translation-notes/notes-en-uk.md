# CVscale translation notes: English → Ukrainian

**Source language:** English · **Target language:** Ukrainian (українська)

Files written to `instruments/`:
- `cvscale-uk.tsv` — 26 items across the five groups
- `dimensions-uk.csv` — dimension names, English kept after " / "
- `scales-uk.csv` — conventional Likert anchors (`повністю не погоджуюся`…`повністю погоджуюся`;
  `зовсім неважливо`…`дуже важливо`)

## Target-language characterization

- **Register / variety.** The written standard is unified, but Ukrainian has a live
  prescriptive axis that Russian lacks: for many concepts there is a widely-used form
  regarded as a Russian calque and a "purer" recommended form (`приймати` vs `ухвалювати
  рішення`, `вирішувати` vs `розв'язувати проблеми`, `опір` vs `спротив`). The poles of that
  axis are not regionally symmetric — puristic forms skew western/literary, calqued forms
  skew eastern/colloquial. I chose forms that are **standard-correct and current everywhere**
  (`ухвалювати`, `розв'язувати`, `опір`), avoiding both the flagged calques and the more
  recent or literary variants that eastern respondents might read as marked. This keeps
  responses comparable across the varieties respondents span.
- **Derivational morphology.** Rich and transparent, so UNI is easy to honor: the `індивід-`
  family links CO "individuals" to "individual rewards / success / goals" exactly as the
  source does. The same transparency makes the *inverse* hazard real, and it bit once — see
  LT6 below.
- **Polysemy / register layering.** The main watch-points were loanword vs. native pairs
  (`лояльність` vs `вірність`, `делегувати` vs `доручати`) and calques whose native stem
  carries a hostile secondary sense (`переслідувати` — see CO5).
- **Connotation & culture.** No systematic amplification of the PO/CO/MA loadings in ordinary
  Ukrainian; the risk was per-word (LT1 "thrift", LT2 "resolutely", UN2 "closely", MA3
  "forcible", CO6 "loyalty"), and each got a CON check.
- **Gender & honorifics.** Ukrainian forces gender agreement on past-tense verbs and
  predicate short adjectives, so any first-person wording is a risk. Two places mattered and
  **both resolved cleanly** — unusually, better than in Russian:
  - The `disagree5` anchor. Russian is stuck with the masculine short adjective `согласен`
    (no neutral conventional form exists). Ukrainian's conventional anchor is built on a
    **present-tense 1sg verb**, `повністю не погоджуюся` … `повністю погоджуюся`, and
    Ukrainian present-tense verbs carry **no gender marking**. So the convention rule and the
    gender-neutrality rule, which genuinely conflict in Russian, agree here. No compromise
    was needed. (I avoided the equally current but gendered `цілком не згоден/згодна`.)
  - UN1, where the respondent speaks — see the minor checks below.
  `important5` poses no problem: `неважливо`/`важливо` are neuter predicatives.

## 1. LT6 "Working hard" — UNI violated *in reverse* (forging a link the source keeps apart)

The natural Ukrainian for "working hard for success in the future" is **A)** `Наполеглива
праця заради успіху в майбутньому`. The problem is LT2, whose parenthetical gloss
"(Persistence)" is `(наполегливість)` — the same `наполегл-` stem. The source keeps
"Persistence" (LT2) and "Working hard" (LT6) lexically distinct; A would forge a visible link
between two items the English separates, suggesting to the respondent that they probe one
construct. This is precisely the inverse-UNI hazard, and Ukrainian's transparent morphology
makes it invisible unless you look for it.

Variants considered: **A)** `наполеглива праця` ("persistent work" — collides with LT2);
**B)** `важка/тяжка праця` ("heavy/hard labour" — reads as arduous toil, a burden, and CON
makes it negative where English "working hard" is neutral-to-positive; it also renders "hard
work", not "working hard"); **C)** `старанна праця` ("diligent work"). I chose **C**. It is a
distinct stem, carries the right effortful-and-positive valence, and pays only a small
semantic price — `старанна` foregrounds diligence where "hard" foregrounds effort. Decisive
argument: UNI is a property of the *instrument*, and a spurious cross-item link corrupts the
LT scale's internal structure, whereas C's slight semantic drift stays well inside the
Long-Term Orientation field (SEM).

The same collision check ruled out `рішучий` ("resolute") for MA3's "forcible", since LT2
already uses `Рішуче`.

## 2. PO1–PO5 "people in higher / lower positions" — SEM and LAM against naturalness

English "positions" is deliberately unspecific: the PO items imply an organizational setting
but never say "job" or "rank". Variants: **A)** `люди, які займають вище / нижче становище`
("people who occupy a higher / lower position", a general hierarchical-status phrase) vs.
**B)** `люди на вищих / нижчих посадах` ("people in higher / lower posts") vs. **C)**
`вищі / нижчі за посадою`, or `керівники` / `підлеглі` ("superiors" / "subordinates").

B and C read more crisply, but `посада` denotes a formal job post, and `керівники/підлеглі`
narrows all the way to a managerial superior-subordinate pair — both resolve an indeterminacy the
source leaves open (LAM) and shrink the item below the Power Distance dimension's scope,
which covers hierarchy generally (SEM). A's only cost is `становище`'s polysemy ("position"
but also "situation, plight", as in `скрутне становище`); the collocation `займати вище
становище` is fixed and dictionary-attested, and the comparative `вище`/`нижче` disambiguates
it immediately, so the AMB risk is nominal. I chose **A**, applied verbatim across all five PO
items (UNI). Decisive: preserving the source's generality outweighs a modest loss of
crispness in a psychometric instrument. This also matches how the sibling translations handle
it (Russian `занимающие более высокое положение`).

## 3. CO5 "pursue their goals" — a calque that is both flagged and ambiguous (AMB)

The word-for-word rendering is **A)** `переслідувати свої цілі`. Two problems compound: Ukrainian
style guides flag `переслідувати мету/цілі` as a Russian calque, and — more seriously for this
instrument — `переслідувати` natively means **to persecute, to hunt down**. That hostile sense
is entirely absent from English "pursue [one's] goals", so A imports an ambiguity the source
does not have (AMB), and it is a hostile one sitting in the middle of a Collectivism item
about weighing group welfare — it could tilt the reading of the whole item.

Variants: **A)** `переслідувати свої цілі`; **B)** `досягати своїх цілей` ("achieve their
goals" — but "pursue" is the striving, not the attainment; B also makes the item's temporal
logic odd); **C)** `прагнути до власних цілей` ("strive toward their own goals"). I chose
**C**: it is the striving sense English has, is prescriptively clean, carries no secondary
sense, and is current across all varieties. Decisive argument: AMB, sharpened by the fact
that the spurious sense is affectively loaded rather than merely distracting.

Note the source's own distinction is preserved: CO5 says "their goals" (`власних цілей`)
while CO6 says "individual goals" (`індивідуальних цілей`), so the `індивід-` stem marks
exactly the items the English marks.

## Minor connotation / lexical checks

- **UN1 "so that I always know" → impersonal `щоб мені завжди було зрозуміло, чого від мене
  очікують`.** A literal `щоб я завжди знав` (m) / `знала` (f) exposes respondent gender in
  the past/subjunctive. The impersonal `було зрозуміло` (neuter) removes every agreement slot
  without changing the meaning. The clause `чого від мене очікують` is reused verbatim in UN3
  for UNI, since both source items share "what is expected of me"; the active impersonal 3pl
  was preferred to a reflexive passive `що від мене очікується`, which Ukrainian style
  discourages. The item was also restructured to `Важливо мати детально розписані
  інструкції, щоб…` — one purpose clause instead of two stacked `щоб`, and closer to the
  source's "to have instructions spelled out in detail".
- **UN3 "regulations" → `приписи`**, not `інструкції`. `Інструкції` already renders
  "instructions" in UN1, UN2 and UN5; reusing it here would forge a link the source keeps
  apart (inverse UNI). Also avoided `регламенти` (corporate-flavoured).
- **CO6 "loyalty" → `вірність групі`** (native, "faithfulness/allegiance") over the loanword
  `лояльність`, which in modern Ukrainian leans toward neutral compliance / non-hostility,
  and over `відданість` ("devotion"), which overshoots. "Group loyalty" in the collectivism
  frame is the warmer allegiance sense (CON).
- **LT1 "Thrift" → `(ощадливість)`**, the positively-valenced virtue term, over `економність`
  (faint stinginess tinge) and `скупість` ("miserliness") (CON). "Careful management of
  money" → `Дбайливе поводження з грошима`: I deliberately used a *different* stem
  (`дбайлив-`) from the gloss, because the English pairs two distinct words ("careful" /
  "Thrift"); `ощадливе поводження … (ощадливість)` would have been tautological.
- **LT2 "resolutely / opposition" → `Рішуче продовження розпочатого попри опір`.** Avoided
  `упертість`/`упертий` ("stubborn", negative) and kept the gloss `(наполегливість)` distinct
  from the adverb. For "opposition" I chose `опір` over `спротив` — synonymous, but `опір` is
  the older, universally standard term, while `спротив` is more recent and literary-flavoured
  (variety stability). `Опозиція` was excluded as political.
- **PO5 "delegate" → `доручати`** (native, "entrust/assign") rather than `делегувати`, a
  corporate loanword that is more clinical than the ordinary managerial English "delegate"
  (CON).
- **PO4 "disagree" → `висловлювати незгоду`** ("express disagreement", mild) rather than
  `оспорювати` ("challenge/dispute", stronger); a bare `не погоджуватися` would produce the
  awkward double negative `не повинні не погоджуватися` (CON + naturalness).
- **PO3 "social interaction" → `неформального спілкування`** ("informal interaction"). The
  calque `соціальної взаємодії` is a sociological term of art that would *include* work
  contact — the opposite of the item's intent, which is socializing beyond the working
  relationship (SEM).
- **UN2 "closely follow" → `точно дотримуватися`** rather than `суворо`/`неухильно`
  ("strictly / rigidly"), which overshoot the moderate "closely" (CON).
- **MA3 "forcible" → `напористого`** ("assertive, pushing"). `Силового` overshoots into
  coercion/violence; `енергійного` undershoots; `рішучого` collides with LT2 (see §1).
- **MA2** repeats `розв'язують проблеми` in both clauses exactly as the source repeats "solve
  problems" (UNI / parallelism).
- **MA4 "jobs" → `види роботи`** ("kinds of work"), not `професії` ("professions") — which
  would additionally collide with MA1's `професійну кар'єру` — and not `завдання` ("tasks"),
  which PO5 already uses. This matches the reading the other translations converged on
  (German `Tätigkeiten`, Dutch `taken`, Russian `виды работы`, and the French correction from
  `métiers` to `tâches`).
- **`уникати` in PO3 vs. `Уникнення невизначеності`** (the UN dimension name) is *not* an
  accidental link: English likewise uses "avoid" in PO3 and "Avoidance" in the dimension
  name, so the echo is faithful.

## Overall

Ukrainian matches the source closely and the translation was largely straightforward. Two
things are worth remembering. First, the difficulty here was not gender — the standard
`погоджуюся` anchor is gender-free, so the one structural compromise Russian must make does
not arise. It was **inverse UNI**: transparent Slavic morphology quietly forges links between
items the source keeps apart, and LT6/LT2 and MA3/LT2 both had to be steered away from
`наполегл-` and `рішуч-`. Second, Ukrainian's prescriptive calque-vs-purist axis demands a
consistent policy; I took standard-correct-but-universally-current throughout, so no item
depends on the respondent's regional variety.
