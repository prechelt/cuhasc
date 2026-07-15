# CVscale translation notes: English → Polish

**Source language:** English · **Target language:** Polish (polski)

Files written to `instruments/`:
- `cvscale-pl.tsv` — 26 items across the five groups
- `dimensions-pl.csv` — dimension names, English kept after " / "
- `scales-pl.csv` — conventional Likert anchors (`zdecydowanie się nie zgadzam`…`zdecydowanie się zgadzam`; `zupełnie nieważne`…`bardzo ważne`)

## Target-language characterization

Polish is a West Slavic language with an unusually uniform written standard: there is no
meaningful regional split in the formal register that questionnaires inhabit (Silesian and
Kashubian are treated as separate lects, not variants of the standard), so wording stays
comparable across all respondents. Four features drove the item-level choices:

- **Rich derivational morphology.** Shared stems make UNI cheap to honor (*grupa* →
  *grupy*/*grupowy*; *cel* → *cele*) but also easy to violate by accident. The one place the
  source's own stem link cannot be reproduced is *individuals* / *individual*: Polish has
  *jednostka* (the sociological term for an individual, opposed to *grupa*) but its adjective
  *jednostkowy* means "unitary, single-instance", not "pertaining to the individual". The
  adjective must therefore be *indywidualny*, a different stem. I accepted the broken stem
  link — semantics beat morphology, and the alternative noun *indywiduum* is pejorative.
- **Polysemy traps English lacks.** Several natural first choices carry a second sense the
  source does not (see PO2 and UN5 below); AMB drove the wording away from them.
- **Gender marking.** Polish forces gender on first-person past-tense and conditional verb
  forms and on predicate adjectives. UN1 speaks in the first person and needed restructuring
  (see below). Elsewhere the impersonal *osoby* (grammatically feminine but referentially
  neutral) and *jednostki* keep gender invisible. The scale anchors use present-tense verbs
  (*zgadzam się*), which are gender-free — a nicer fit than the Russian short-adjective
  anchors, which are not.
- **Connotation.** Polish organizational vocabulary is not notably more deferential than
  English, so PO needed no de-amplification; the only CON tension was PO4 (below).

Three decisions were worth flagging.

## 1. UN1 — first-person gender marking (gender-neutrality rule)

"…so that I always know what I'm expected to do." The obvious rendering of the purpose
clause takes *żeby* + a past-participle-derived form, which is unavoidably gendered:
**A) "żebym zawsze wiedział"** (masculine) / *"żebym zawsze wiedziała"* (feminine). Polish
offers no neutral form here, and slash notation ("wiedział/a") is the convention Polish
questionnaires fall back on — but it is visually intrusive and marks the respondent's gender
as salient in an item that has nothing to do with gender, sitting oddly in an instrument
whose MA group *does* measure gender attitudes.

I restructured instead: **B) "…dzięki czemu zawsze wiem, czego się ode mnie oczekuje"**
("…thanks to which I always know what is expected of me"). The present-tense *wiem* carries
no gender. The cost is a slight shift from purpose ("so that") to result ("thanks to which"),
which I judged negligible — the item's force is that detailed instructions *produce* the
knowledge. Chose **B**: keeping gender invisible is an explicit rule, and the semantic cost
is far smaller than the alternative's.

The same *"czego się ode mnie oczekuje"* is reused verbatim in UN3, mirroring the source's own
repetition of "what is expected of me" across UN1 and UN3 (UNI).

## 2. PO2 "opinions" and UN5 "operations" — two polysemy traps (AMB)

Both items have a natural Polish first choice that smuggles in an ambiguity the English lacks.

**PO2:** variants for "ask the opinions of" — **A) "pytać o opinię"** vs.
**B) "pytać o zdanie"**. B is arguably the more idiomatic collocation, but *zdanie* means both
"opinion" and "sentence (grammatical unit)". English "opinion" has no such twin sense. Chose
**A** (*opinia*), which is unambiguous and equally register-appropriate — a clean AMB call.

**UN5:** "Instructions for operations are important." The literal **B) "instrukcje
operacyjne"** / *"wykonywania operacji"* founders because Polish *operacja* denotes, first and
foremost, a **surgical operation**, secondarily a military one; the neutral English sense of
"a thing done" is not among its salient readings. **C) "instrukcja obsługi"** is worse — it is
the fixed term for a *product user manual*, which relocates the item out of the workplace
entirely. Chose **A) "Instrukcje dotyczące wykonywania czynności"** ("instructions for
carrying out activities"), where *czynności* is the neutral Polish word for work operations.
*Instrukcje* is retained across UN1, UN2 and UN5 to preserve the source's within-group
repetition (UNI).

## 3. PO4 "should not disagree with decisions" (CON)

Variants: **A) "nie powinny kwestionować decyzji"** (should not question/challenge the
decisions) vs. **B) "nie powinny nie zgadzać się z decyzjami"** (should not be in disagreement
with the decisions) vs. **C) "nie powinny sprzeciwiać się decyzjom"** (should not oppose the
decisions).

B is the literal, mildest match and preserves the source's "merely holding a contrary view"
reading — but the stacked negation (*nie powinny nie zgadzać się*) is genuinely clumsy in
Polish and would read as a drafting error to a native respondent. C over-shoots: *sprzeciwiać
się* implies active resistance, well beyond "disagree". A sits between them: *kwestionować*
implies voicing the disagreement, so it is slightly stronger than the source, but the item is
precisely about whether subordinates should express dissent toward superiors' decisions, which
makes that nuance on-topic rather than an over-translation. Chose **A** — the same trade-off
the French translation resolved the same way (*contester*); naturalness outweighed the small
CON gap, and C was ruled out as a real strength mismatch.

## Structural / uniformity notes

- **"people in higher/lower positions"** → *osoby na wyższych/niższych stanowiskach*,
  identical in all five PO items. *Stanowisko* (job post) was chosen over *pozycja* (a
  business-jargon calque, unidiomatic here) and over *osoby wyżej postawione* ("higher-placed
  people", which adds a faintly resentful social colouring the neutral English lacks, CON).
  *Stanowisko* does have a second sense ("stance, position on an issue"), but the collocation
  *na wyższych stanowiskach* forecloses it completely, so AMB does not bite.
- **PO3 "social interaction"** → *kontakty towarzyskie* (socializing), not *interakcje
  społeczne*, which is sociology jargon and would wrongly include work interaction (SEM).
- **CO2 vs. CO6:** CO2 "stick with the group" → *trzymać się grupy* (cohesion), deliberately
  kept lexically clear of the *lojalność* field that belongs to CO6 — otherwise the two items
  merge, a distinction the source keeps.
- **"welfare of the group"** → *dobro grupy*, identical in CO3 and CO5 (UNI). *Dobrobyt*
  was rejected as narrowing to material prosperity. Correspondingly, CO1 "sacrifice
  self-interest **for the group**" is *na rzecz grupy*, not *dla dobra grupy*: adding *dobro*
  there would forge a link to CO3/CO5 that the source does not make.
- **"tasks" (PO5) vs. "jobs" (MA4)** are distinct words in the source and stay distinct:
  *zadania* and *prace* respectively. MA4 uses *prace* ("kinds of work") rather than *zawody*
  (professions) or *zajęcia* (which also means "school classes"), landing where the German
  (*Tätigkeiten*), Dutch (*taken*), French (*tâches*) and Russian (*виды работы*) versions
  landed. "can always do better" → *zawsze wykona lepiej* (perfective future), since Polish
  *może* would read as permission; this matches the French and Russian handling.
- **"success in the future"** → *dla przyszłego sukcesu*, identical in LT5 and LT6 (UNI);
  *sukces* is also the CO4 word, as in the source.
- **LT glosses:** "Thrift" → *oszczędność* (the positively-valenced saving term, as with
  German *Sparsamkeit* / Spanish *Ahorro*); "Persistence" → *wytrwałość*, the standard Polish
  Hofstede term. LT3 "steadiness" is *stałość* (constancy), kept clear of *wytrwałość* so the
  source's separation of LT2 and LT3 survives. Glosses are lowercased per Polish orthography
  (as in the Russian version); German and French capitalize theirs for language-specific
  reasons.
- **MA3 "active, forcible"** → *aktywnego, stanowczego*. *Siłowy* ("by force") is far too
  strong and negative in Polish; *energiczny* is a near-synonym of *aktywny* and would make the
  pair redundant; *stanowczy* ("firm, insistent") carries the assertive-force nuance while
  staying a genuinely distinct second adjective (CON).
- **Dimension names** use the established Polish Hofstede terminology: *dystans władzy*,
  *unikanie niepewności*, *kolektywizm*, *orientacja długoterminowa*, *męskość*.
- **Scale anchors:** the agreement anchors are the standard Polish 5-point pair. For the
  importance scale I deliberately departed from a literal "very unimportant": Polish strongly
  disprefers *bardzo* + a negated adjective, so *bardzo nieważne* sounds wrong. The
  conventional low anchor is *zupełnie nieważne* ("completely unimportant"), which is what
  Polish questionnaires actually use — the same call the Russian version made (*совсем
  неважно*). The skill's instruction to prefer conventional scientific anchors decided this
  over literal symmetry with the source.

## Confidence

No capability caveat applies: Polish is a well-resourced language and every source item has a
natural, register-stable Polish equivalent. The genuine difficulties were the three flagged
above (a forced gender marking, two polysemy traps, one connotation gap), all of which have
defensible resolutions rather than compromises.
