# CVscale translation notes: English → Romanian

**Source language:** English · **Target language:** Romanian (română)

Files written to `instruments/`:
- `cvscale-ro.tsv` — 26 items across the five groups
- `dimensions-ro.csv` — dimension names, English kept after " / "
- `scales-ro.csv` — conventional Likert anchors (`dezacord total`…`acord total`; `foarte puțin important`…`foarte important`)

## Target-language characterization

Romanian is the one Romance language in the Balkan Sprachbund: Latin morphology and a
Latinate learned vocabulary (largely re-imported from French and Italian in the 19th
century) sitting on top of an older Slavic and substrate lexical layer. Three consequences
shaped this translation.

**Register layering.** For many concepts Romanian offers a neologistic Latinate word beside
an inherited everyday one — *opinie/părere*, *a contesta/a se împotrivi*, *economie/
cumpătare*. The learned member often carries an administrative or legal-formal charge that
the neutral English lacks (see PO4 below), so the "obvious cognate" is frequently the wrong
choice under CON. The written standard is otherwise very stable across Romania and the
Republic of Moldova at this register, so comparability across respondents is not at risk.

**Derivational morphology.** Shared stems make UNI easy to honor — *individ/individual*,
*succes*, *grup*, *important/importanță* map one-to-one onto the source's own repetitions.
The same ease makes accidental links cheap: I had to keep *personal* out of CO1 and
*hotărâre* out of MA3 to avoid forging ties the source keeps separate (see below).

**Gender.** Romanian forces grammatical gender on nouns and adjectives. The PO and CO items
are third-person and impersonal, so no respondent-facing gender is exposed; *persoanele*
(fem.) and the generic masculine plural *indivizii* both refer without marking the reader.
The MA group names genders because the source does. Romanian has no tu/dumneavoastră
problem here: only UN1 and UN3 speak in the first person, where *ce se așteaptă de la mine*
is neutral everywhere.

Romanian is a well-resourced language for me; I am confident in this translation at the
same level as for the other major European languages in this set.

## 1. PO4 "should not disagree with decisions" (CON / LAM, plus a syntactic trap)

Romanian has no clean way to negate a negatable state verb here: the literal *a nu fi de
acord* ("to not agree") under "should not" yields **"nu ar trebui să nu fie de acord"** — a
grammatical but badly stacked double negative that respondents would have to parse twice.
So the choice was among three repairs:

- **A) "nu ar trebui să își exprime dezacordul față de deciziile…"** — should not express
  disagreement with the decisions.
- **B) "nu ar trebui să conteste deciziile…"** — should not contest/challenge the decisions.
- **C) "nu ar trebui să se opună deciziilor…"** — should not oppose the decisions.

C is plainly too strong (*a se opune* is active resistance). B is the idiomatic management
phrasing and is what the French translation reached for with *contester* — but Romanian *a
contesta* is much more strongly colored than French *contester*: its salient everyday sense
is the formal appeal (*contestație* — against a grade, a tender, an exam result), so B
imports an administrative-procedural overtone that English "disagree" does not have (CON).
A keeps *dezacord*, the exact cognate of the source's word and the mildest option. Its cost
is that *își exprime* fixes the voicing reading, whereas English "disagree with decisions"
leaves holding-vs-voicing open (LAM argues against A).

Chose **A**. The decisive argument: PO measures deference to authority, so the voiced
reading is squarely inside the dimension's field (SEM) and is the reading that actually
discriminates respondents — a silently held opinion is not what the item is probing. Paying
a small LAM cost to avoid B's register drift (CON) was the better trade. Note that
*dezacord* also appears as the scale anchor (*dezacord total*); this is a minor
questionnaire-design blemish I accepted as the lesser evil.

## 2. CO1/CO2/CO5 "Individuals" → "indivizii" (CON vs. UNI)

Romanian *individ* has a colloquial pejorative tinge absent from English "individual": *un
individ* often means "some bloke", faintly shady. Variants:

- **A) "Indivizii ar trebui să…"** — the generic plural.
- **B) "Oamenii" / "Persoanele"** — people/persons.
- **C) "Fiecare ar trebui să…"** — everyone should.

B collides with the PO group, which already owns *persoanele*, and would erase the
source's deliberate lexical opposition between "People" (PO) and "Individuals" (CO). C
dissolves the individual-vs-group contrast that is the whole point of the Collectivism
dimension (SEM). A's pejorative sense is confined to the colloquial singular with an
indefinite article; the definite generic plural *indivizii* in a normative statement reads
sociologically, which is the questionnaire's register.

Chose **A**, decisively because of UNI: *indivizii* (CO1, CO2, CO5) shares its stem with
*individuale* (CO3, CO6) and *individual* (CO4), reproducing exactly the individual- stem
recurrence the English source has across all six CO items. No other option preserves that.

## 3. MA4 "some jobs" (SEM, cross-group distinctness)

English "jobs" is ambiguous between occupations/trades and kinds-of-work. The corpus has
already settled this: German *Tätigkeiten* (activities), Dutch *taken*, Italian *lavori*,
Russian *виды работы* — and French was explicitly corrected from *métiers* (trades) to
*tâches* in commit a226e72. So the intended reading is kinds-of-work, not professions.
Romanian variants:

- **A) "unele activități"** — some activities (cf. German *Tätigkeiten*).
- **B) "unele sarcini"** — some tasks (cf. French *tâches*, Dutch *taken*).
- **C) "unele meserii"** — some trades/occupations (the rejected *métiers* reading).
- **D) "unele munci" / "unele lucrări"** — some labors/works.

C is out by the harmonization above. D drifts to manual labor (CON). B matches the French
and Dutch solutions, but *sarcini* is already PO5's word for "tasks", and the source keeps
"tasks" (PO5) and "jobs" (MA4) lexically distinct — B would forge a cross-group link the
source does not have. Chose **A**: it lands on the harmonized kinds-of-work reading while
staying distinct from PO5, exactly as German does (*Aufgaben* in PO5, *Tätigkeiten* in
MA4). The MA context (MA1's career, MA3's problem-solving) fixes the work reading, so
*activități* is not read as leisure activity.

## Structural / uniformity notes

- **PO group:** "people in higher/lower positions" is *persoanele aflate în poziții
  superioare/inferioare* in all five items, matching the corpus consensus on "positions"
  (de/es/pt/fr/it/nl). *Funcții* was rejected: *funcții superioare* collocates with *funcții
  cognitive superioare* in psychology, an ambiguity English lacks (AMB) and a bad one to
  introduce in a psychometric instrument.
- **PO5** "tasks" → *sarcini*, the standard management collocation (*delegarea sarcinilor*).
  *Sarcină* also means "pregnancy" in Romanian, but the sense is unreachable in the plural
  with *a delega*; *atribuții* was rejected as it denotes formally attached duties, i.e.
  transferring authority rather than work.
- **UN group:** *instrucțiuni* recurs across UN1, UN2, UN5 and *proceduri* across UN2, UN4,
  preserving the source's within-group repetition. UN2 uses *a urma* (to follow), not the
  more idiomatic *a respecta* (to comply with/observe): *a respecta* adds a deference charge
  that belongs to the Power Distance field, and would bleed UN toward PO (SEM).
- **UN5** "Instructions for operations" → *Instrucțiunile pentru operațiuni*. *Operațiuni*
  (business/technical operations), not *operații*, which is the surgical/mathematical word —
  this preserves the source's vagueness without adding a wrong reading (LAM/AMB).
- **UN1/UN3:** "what is expected of me" is *ce se așteaptă de la mine* in both, as in English.
- **CO group:** *bunăstarea grupului* is identical in CO3 and CO5; *obiectivele* serves CO5
  and CO6. CO1 uses *interesul propriu*, not *interesul personal*, deliberately: the source
  says "self-interest" (CO1) and "Personal steadiness" (LT3) with different stems, and
  reusing *personal* in CO1 would link two items English keeps apart (UNI, negatively
  applied).
- **CO2 vs. CO6:** "stick with the group" → *să rămână alături de grup*, avoiding any
  loyalty word so that CO6's *loialitatea față de grup* stays the group's only loyalty item —
  the same separation the French translation protects.
- **LT1 "Thrift"** → **Cumpătare**. Considered *Economie* (rejected: ambiguous with the
  discipline of economics, AMB), *Economisire* (money-specific and unambiguous, but names
  the activity of saving rather than the disposition English "Thrift" names), and *Spirit de
  economie* (dispositional and precise, but a phrase where the sibling gloss *Perseverență*
  is a single word). *Cumpătare* is the established Romanian virtue term; its broader
  "temperance" reading is neutralized by the item text (*Gestionarea atentă a banilor*)
  standing immediately before the gloss. Parallel to German *Sparsamkeit*, French *Épargne*,
  Spanish *Ahorro*.
- **LT2 "Persistence"** → *Perseverență*, the standard Romanian Hofstede term. "Opposition"
  → *opoziției*, which carries the same political-Opposition polysemy as the English, so the
  parallel is preserved rather than repaired (LAM).
- **LT form:** the source mixes noun phrases (LT1, LT3, LT4) with gerund phrases (LT2, LT5,
  LT6); Romanian mirrors this with noun phrases and *a* + infinitive respectively.
- **LT3:** *personale* is plural so that it modifies both *statornicie* and *stabilitate*,
  as in the source and as French does (*Constance et stabilité personnelles*).
- **UNI on "success":** *succes* renders every occurrence (CO4, LT5, LT6); "success in the
  future" is *succesul viitor* in both LT5 and LT6.
- **MA3** "active, forcible approach" → *o abordare activă și energică*. *Forțată* would be a
  false friend (= forced/artificial). *Hotărâtă* (determined) was rejected on UNI grounds: it
  shares its stem with LT2's *cu hotărâre* ("resolutely"), and the source uses distinct words
  ("resolutely" vs. "forcible") in the two items.
- **Dimension names** use the conventional Romanian management-literature terms: *distanța
  față de putere*, *evitarea incertitudinii*, *orientarea pe termen lung*. PO/UN/LT carry the
  definite article because their Romanian forms are deverbal nouns that require it; CO and MA
  are bare nouns that do not take one.
- **Scale anchors:** *dezacord total*…*acord total* is the standard Romanian 5-point Likert
  pair. For `important5`, *foarte puțin important* follows the Romance solutions (es *muy
  poco importante*, pt *muito pouco importante*, fr *très peu important*); the literal
  calque *foarte neimportant* was rejected as unidiomatic — *neimportant* is rare and stilted
  in Romanian.
- Orthography uses the comma-below diacritics ș/ț (U+0219/U+021B), per the Romanian standard,
  not the legacy cedilla forms.
