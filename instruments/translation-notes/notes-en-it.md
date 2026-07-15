# CVscale translation notes: English → Italian

**Source language:** English · **Target language:** Italian (italiano)

Files written to `instruments/`:
- `cvscale-it.tsv` — 26 items across the five groups
- `dimensions-it.csv` — dimension names, English kept after " / "
- `scales-it.csv` — conventional Likert anchors (`totalmente in disaccordo`…`totalmente d'accordo`; `molto poco importante`…`molto importante`)

## Target-language characterization

Italian's written standard is markedly uniform across regions: regional variation in Italy is
overwhelmingly a spoken phenomenon (and, at the extreme, a matter of separate regional languages),
while the formal written register questionnaires use is stable from Milan to Palermo and in
Italian-speaking Switzerland. Respondent comparability is therefore not at risk, and the main
register decision is only how formal to be. Most items are impersonal third-person statements,
which sidesteps the *tu/Lei* address problem entirely; only UN1 and UN3 speak in the first person,
where the neutral "io … che cosa ci si aspetta da me" is safe in every variety.

The dense Latinate overlap with English makes UNI cheap to honor (*individuo/individuale*, *gruppo*,
*successo*, *obiettivi*) but correspondingly easy to violate by accident — shared stems can forge a
link across items the source deliberately keeps apart, which is exactly the CO2/CO6 trap below. The
same overlap raises false-friend risk in the other direction: the etymologically obvious word is
sometimes the wrong register (*persistenza* is technical/physical in Italian, not a virtue).

Grammatical gender is forced on every noun and adjective. "Le persone" (feminine plural) and "gli
individui" (masculine plural) are both semantically gender-neutral in ordinary usage and were used
as such, following the Spanish and French solution. For MA the gendering is of course intentional
and in the source. Connotation-wise, Italian offers no temptation to inflate PO's authority framing:
the conditional *dovrebbero* carries the same hedged, non-obligatory force as English "should",
so CON is satisfied without effort across the whole PO group.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. PO4 "disagree with decisions" (CON / AMB)

Variants: **A) "dissentire dalle decisioni"** (to dissent from / disagree with the decisions) vs.
**B) "essere in disaccordo con le decisioni"** (to be in disagreement with the decisions) vs.
**C) "contestare le decisioni"** (to challenge/dispute the decisions).

C is what French settled on (*contester*), but in Italian *contestare* is distinctly stronger than
the source: it implies actively disputing or protesting, and carries a faint political-agitation
overtone (*contestazione* is the standard word for the 1968 protest movement) that "disagree" has no
trace of — an over-translation under CON, and an added connotation under AMB. B is the literal match
and mild, but it re-uses the exact wording of the response anchors (*totalmente in disaccordo* …
*totalmente d'accordo*): the item would then ask respondents to agree-or-disagree about being in
disagreement, an echo the English avoids because "disagree with decisions" and the anchor "strongly
disagree" don't collide in the same phrasing register. A is a single natural verb, sits at the same
strength as the source, and covers voicing dissent to a superior — precisely the Power Distance
field (SEM). Chose **A**; avoiding the item/anchor echo was the most decisive argument.

## 2. CO2 "stick with the group" vs. CO6 "loyalty" (UNI)

The trap is translating CO2 with a loyalty word and thereby merging it into CO6, where loyalty is
the actual construct. Variants for "stick with the group even through difficulties":
**A) "restare uniti al gruppo"** (stay united with / hold together with the group) vs.
**B) "rimanere fedeli al gruppo"** (stay faithful/loyal to the group) vs.
**C) "rimanere nel gruppo"** (remain in the group).

B is the most idiomatic single rendering, but *fedeltà/lealtà* is the field CO6 occupies ("La lealtà
verso il gruppo…"), so B collapses two items the source keeps distinct — a UNI violation in the
negative direction (manufacturing uniformity that isn't there). C is safely distinct but drains the
item to mere membership, losing the cohesion-under-pressure sense that puts it inside Collectivism
(SEM). A keeps CO2 about sticking together through hardship, stays squarely in the Collectivism
field, and shares no stem with CO6. Chose **A**: preserving the source's separation of the two items
was decisive, matching the French *solidaires* reasoning.

## 3. LT1 "Thrift" gloss (CON)

Variants: **A) "Risparmio"** (saving, savings) vs. **B) "Parsimonia"** (parsimony, thrift) vs.
**C) "Frugalità"** (frugality).

B is the closest one-to-one lexical match — it names a disposition, as "Thrift" does, where A names
the act or its result. But ordinary Italian usage has drifted *parsimonia* toward the stingy end:
the live idiom *con parsimonia* means "sparingly", and applied to a person the word reads closer to
tight-fisted than to prudent. C is worse on the same axis, importing an austerity/self-denial
overtone. "Thrift" in the Hofstede instrument is a positively-valenced virtue, so B and C both
undershoot its connotation (CON). A is neutral-to-positive, is the word Italian actually uses for
careful money management, and matches the sibling Romance convention (es *Ahorro*, fr *Épargne*,
pt *Poupança*) as well as de *Sparsamkeit* / nl *Spaarzaamheid*. Chose **A**, accepting the small
act-vs-disposition mismatch as the cheaper cost — the gloss's job is to name the value, and the head
phrase "Gestione attenta del denaro" already supplies the dispositional framing.

## Structural / uniformity notes

- **MA4 "jobs" → "lavori"**: taken as the concrete work reading, not the occupational one. The
  alternatives *mestieri* (trades) and *professioni* (professions) would pull toward the
  career/profession framing that MA1 already owns. This follows the established cross-language
  convention (de *Tätigkeiten*, nl *taken*, es *trabajos*, pt *trabalhos*, ru *виды работы*) and
  specifically the maintainer's correction of French *métiers* → *tâches* in commit `a226e72`.
  *lavori* is also the exact cognate of the Spanish/Portuguese choice.
- PO5 "tasks" → **compiti**, kept lexically distinct from MA4 *lavori*, since the source likewise
  distinguishes "tasks" from "jobs" (French collapsed both onto *tâches*; Italian need not).
- "what is expected of me" is rendered identically in UN1 and UN3 (**che cosa ci si aspetta da me**)
  for UNI, as in the source.
- "instructions" is kept across UN1, UN2, UN5 (**istruzioni**) to preserve the source's within-group
  repetition; UN5 "Instructions for operations" → **istruzioni operative**, the standard Italian
  term for operating instructions, rather than the clunky calque *istruzioni per le operazioni*.
- "welfare of the group" / "group welfare" is identical in CO3 and CO5 (**benessere del gruppo**);
  "goals" is **obiettivi** in CO5 and CO6; "success" is **successo** everywhere it recurs (CO4, LT5,
  LT6), with "success in the future" → **il successo futuro** in both LT5 and LT6.
- MA2 repeats "risolvono i problemi" in both clauses, mirroring the source's deliberate repetition.
- LT2 gloss "Persistence" → **Perseveranza**, the standard Italian Hofstede term; *Persistenza* was
  rejected as technical/physical in Italian (persistence of a substance, of an image) — an ambiguity
  the English lacks (AMB).
- LT items are kept as phrases, not sentences, as in the source.
- Dimension names use the conventional Italian management-literature terms: *distanza dal potere*
  (Power Distance) and *avversione all'incertezza* (Uncertainty Avoidance), the latter preferred over
  the calque *evitazione dell'incertezza*.
- `scales-it.csv`: *molto poco importante* … *molto importante* mirrors the symmetric bipolar
  anchoring of the source and the Romance siblings (es *muy poco importante*, fr *très peu
  important*, pt *muito pouco importante*), rather than the also-common Italian questionnaire anchor
  *per nulla importante* ("not at all important"), which would shift the low endpoint from "very
  unimportant" to a zero point.

## Capability note

Italian is a high-resource language and a close structural relative of the source; no
capability-related caveats apply to this translation.
