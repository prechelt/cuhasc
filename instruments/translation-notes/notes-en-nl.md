# CVscale translation notes: English → Dutch

**Source language:** English · **Target language:** Dutch (Nederlands)

Files written to `instruments/`:
- `cvscale-nl.tsv` — 26 items across the five groups
- `dimensions-nl.csv` — dimension names, English kept after " / "
- `scales-nl.csv` — conventional Likert anchors (`helemaal mee oneens`…`helemaal mee eens`; `zeer onbelangrijk`…`zeer belangrijk`)

## Target-language characterization

Dutch is a West Germanic language, structurally close to English and closer still to
German, which makes most items near-transparent. The relevant axes:

- **Register / variety split.** The written standard is stable across the Netherlands and
  Flanders; the main risk is Belgian/Netherlandic lexical divergence, which is negligible
  in the abstract organizational vocabulary these items use. The impersonal third-person
  framing of PO, CO and MA sidesteps the *je/u* address problem entirely; only UN1 and UN3
  speak in the first person, where "wat er van mij wordt verwacht" is register-safe in both
  varieties.
- **Derivational morphology.** Dutch compounds freely (*groepsloyaliteit*,
  *werkprocedures*, *langetermijnplanning*), which makes UNI easy to honor — but the same
  freedom makes it easy to forge a link the source keeps separate, since any two concepts
  can be welded into one stem. Watched for this in CO2 vs. CO6 and UN4/UN5.
- **Polysemy / register layering.** Low risk. Dutch has no classical/religious lexical
  layer of the kind that complicates Arabic, Persian or Hindi here. The one live trap is
  *zuinig* (thrifty), which carries a "stingy" overtone English *thrift* lacks — see LT1.
- **Connotation & culture.** Dutch workplace usage is, if anything, *less* deferential than
  English: the flat-hierarchy norm means an over-strong PO verb (e.g. *zich verzetten tegen*,
  "oppose") reads as unusually confrontational rather than neutral. CON therefore pushed
  toward the mildest literal options in PO4.
- **Gender & honorifics.** Dutch marks gender on nouns lexically but not on *mensen*,
  *individuen*, or *personen*, so PO/UN/CO stay gender-invisible without effort. MA1–MA4
  name genders in the source, so nothing is added there.

Hofstede was himself Dutch, so the dimension names have established native forms
(*machtsafstand*, *onzekerheidsvermijding*, *langetermijngerichtheid*) rather than
ad-hoc calques; these were used.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. CO2 "stick with the group" vs. CO6 "loyalty" (UNI / SEM)

The natural first reflex for "stick with the group even through difficulties" is a loyalty
word — but CO6 is *precisely* the loyalty item ("Group loyalty should be encouraged…"), and
the source keeps the two lexically apart. Variants: **A) "bij de groep blijven"** (stay with
the group) vs. **B) "de groep trouw blijven"** (stay loyal/faithful to the group) vs.
**C) "solidair blijven met de groep"** (stay in solidarity with the group). B pulls CO2 into
the *trouw/loyaliteit* field that belongs to CO6, collapsing two distinct items into one
concept — exactly the compound-friendly trap Dutch invites. C is defensible but adds a
solidarity nuance the plain English "stick with" does not carry. A is the literal match,
stays squarely inside the Collectivism field (SEM), and remains lexically distinct from
CO6's *groepsloyaliteit*. Chose **A**; preserving the source's separation of the two items
(UNI, applied negatively) was decisive.

## 2. PO4 "disagree with decisions" (CON)

Variants: **A) "het niet oneens zijn met beslissingen"** (not be in disagreement with the
decisions) vs. **B) "beslissingen niet tegenspreken"** (not contradict the decisions) vs.
**C) "beslissingen niet ter discussie stellen"** (not call the decisions into question).
B and C are syntactically lighter and more idiomatic, but both shift from *holding* a
dissenting view to *voicing or acting on* it — a real strengthening. That strengthening is
riskier in Dutch than it was in French: against the flat-hierarchy norm of Dutch workplace
usage, *tegenspreken* and *ter discussie stellen* read as markedly confrontational, so a
respondent would be answering a harsher question than the English one. A is slightly
clunky after "zouden … moeten" but is the exact match for the source's mild "disagree".
Chose **A**, with CON decisive over naturalness.

## 3. MA4 "jobs" (SEM / cross-group consistency)

Variants for "some jobs": **A) "taken"** (tasks) vs. **B) "werkzaamheden"** (activities,
work) vs. **C) "beroepen"** (occupations, professions) vs. **D) "banen"** (job positions).
C and D read "jobs" as the occupational slot, which narrows the item to career choice and
over-links it to MA1's professional-career framing; the sibling translations do not go that
way (de *Tätigkeiten*, fr *tâches*, es *trabajos*, pt *trabalhos* all read "jobs" broadly as
work/tasks). That leaves A vs. B. The one argument for B was to avoid reusing *taken*,
which PO5 already uses for the source's "tasks" — but that overlap is cross-group, not
within-group, so UNI does not forbid it, and the source's own "tasks"/"jobs" are near
synonyms rather than a drawn contrast. French makes exactly the same reuse (*tâches* in
both PO5 and MA4). Chose **A**: "Er zijn bepaalde taken die een man altijd beter kan
uitvoeren dan een vrouw."

## Structural / uniformity notes

- PO1–PO5 keep a fixed frame: "mensen in hogere posities" / "mensen in lagere posities"
  throughout, mirroring the source's verbatim repetition. *Mensen* was preferred over
  *personen* as the register-natural Dutch choice.
- "success" is rendered **succes** everywhere it recurs (CO4, LT5, LT6) for UNI; "success in
  the future" is identically "succes in de toekomst" in both LT5 and LT6.
- "welfare of the group" / "group welfare" is identical in CO3 and CO5 ("het welzijn van de
  groep"); "goals" is "doelen" in both CO5 and CO6.
- "instructions" is kept as a standalone *instructies* across UN1, UN2 and UN5 to preserve
  the source's within-group repetition. UN5 "instructions for operations" → "Instructies
  voor werkzaamheden"; the compound *werkinstructies* (the route German took with
  *Arbeitsanweisungen*) was rejected because it dissolves the standalone word and the
  "for X" structure that es/pt/fr all keep.
- "what I'm expected to do" (UN1) and "what is expected of me" (UN3) both become "wat er van
  mij wordt verwacht" — the source varies only syntactically, not conceptually.
- LT glosses: "Thrift" → **Spaarzaamheid**, the saving-as-virtue term, chosen over
  *zuinigheid*, which carries a stinginess overtone the neutral-positive English *thrift*
  lacks (AMB); this matches the de *Sparsamkeit* / fr *Épargne* / es *Ahorro* choice.
  "Persistence" → **Volharding**, the standard Dutch Hofstede term. LT3 "steadiness" →
  *standvastigheid*, which overlaps somewhat with *volharding* — but the source's own
  "steadiness"/"persistence" overlap to the same degree, so this is faithful rather than a
  defect.
- LT4 "Long-term planning" → **Langetermijnplanning**, one word per current Dutch spelling
  (Groene Boekje).
- MA3 "forcible" → **krachtdadig** (forceful, vigorous), preferred over the plainer
  *krachtig* (strong) and the softer *doortastend* (decisive): it is the term Dutch
  management usage reaches for and matches the source's assertive-but-not-aggressive
  valence (CON).
- Item form is preserved throughout: PO/UN/CO/MA are complete sentences, LT items are bare
  phrases; parenthetical glosses in LT1 and LT2 are translated.

## Confidence

Dutch is a high-resource language and structurally close to both English and German, and
the sibling German translation provided a useful cross-check on several items. No
capability caveats apply to this translation.
