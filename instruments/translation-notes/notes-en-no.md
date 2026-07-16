# CVscale translation notes: English → Norwegian

**Source language:** English · **Target language:** Norwegian Bokmål (norsk bokmål)

Files written to `instruments/`:
- `cvscale-no.tsv` — 26 items across the five groups
- `dimensions-no.csv` — dimension names, English kept after " / "
- `scales-no.csv` — conventional Likert anchors (`helt uenig`…`helt enig`; `svært uviktig`…`svært viktig`)

Norwegian has two official written standards. Per the project's `target-languages-list.csv`
(note 8), this translation defaults to **Bokmål**, the majority written form; a Nynorsk version
would be a separate deliverable. Danish (`cvscale-da.tsv`) was available as an extremely close
North Germanic sibling and served as the primary cross-check, alongside German and Dutch.

## Target-language characterization

Bokmål is a North Germanic language that grew out of written Danish and remains lexically very
close to it, with heavy Middle Low German borrowing across exactly the organizational vocabulary
these items use. That closeness makes most items near-mechanical, but it also imports several of
the same traps the Danish notes flag.

- **Register / variety split.** The salient split for Norwegian is Bokmål vs. Nynorsk, resolved
  up front in favor of Bokmål. Within Bokmål there is a further conservative/radical (*riksmål*-leaning
  vs. *samnorsk*-leaning) spread, but none of the words needed here fall on a contested form —
  *personer*, *beslutninger*, *gruppen*, *viktig* are stable across the whole Bokmål range, so
  responses stay comparable. The old formal pronoun *De* is dead in questionnaire register; PO/CO/MA
  are impersonal third person, and only UN1/UN3 use the first person, where *hva som forventes av
  meg* is register-neutral.
- **Derivational morphology.** Norwegian compounds as freely as Danish and German
  (*gruppelojalitet*, *arbeidsprosedyrer*, *egeninteresse*, *arbeidsoppgaver*), so UNI is cheap to
  honor but equally cheap to violate by welding two source-distinct concepts into one stem. Watched
  this at CO2 vs. CO6 and UN2/UN4 vs. UN5.
- **Polysemy / register layering.** Low overall; no classical or religious lexical layer. The one
  live trap, inherited straight from Danish, is *velferd*: the literal cognate of "welfare" has been
  captured by the welfare state (*velferdsstaten*), so it carries a reading the neutral English
  "welfare" does not (see §1).
- **Connotation & culture.** As with Danish, Norway sits at the low end of Hofstede's Power Distance
  scale and the flat-hierarchy, egalitarian norm (the Norwegian counterpart of *Janteloven*) is
  culturally explicit. A verb of even moderate force in PO reads as more confrontational than the
  neutral English, so CON pushed toward the mildest literal option throughout PO (see §2).
- **Gender & honorifics.** Norwegian marks gender lexically on some nouns but not on *personer*,
  *individer* or *mennesker*, so PO, UN and CO stay gender-invisible with no effort. MA1–MA4 name
  genders in the source, so nothing is added there.

Norwegian Bokmål is a high-resource language and no capability caveats apply. The translation was
largely straightforward; three decisions were worth flagging, and most of them parallel the Danish
ones because the two languages converge on these exact points.

## 1. CO3 / CO5 "welfare of the group" (AMB)

The literal cognate of *welfare* is **velferd**, but in modern Norwegian *velferd* is dominated by
the welfare state (*velferdsstaten*, *velferdsordninger*, *velferdstjenester*). "Gruppens velferd"
would make a respondent hear public provision and benefits — an ambiguity the neutral English "group
welfare" does not carry (AMB).

Variants: **A) "gruppens vel"** (the group's good/wellbeing) vs. **B) "gruppens velferd"** (welfare,
with the welfare-state reading) vs. **C) "gruppens beste"** (the group's best interest) vs.
**D) "gruppens velvære"** (the group's felt wellbeing/comfort). B was rejected for the welfare-state
reading. D denotes personal, felt comfort and reads oddly of a collective. C is the most idiomatic
Norwegian of the four, but it shifts a *state* ("welfare") into an *interest* ("what is best for"),
slightly reframing the comparison the source makes.

Chose **A**. *Vel* is the exact counterpart of German *Wohl* / Danish *vel* and survives in current
Norwegian set phrases (*til felles vel*, *landets vel*, *til alles vel*); it is faintly formal but
well within questionnaire register, keeps the state-noun form, and avoids the welfare-state reading.
Avoiding an ambiguity the source lacks (AMB) was decisive over C's greater naturalness. Used
identically in CO3 and CO5, mirroring the source's own repetition (UNI).

## 2. PO4 "disagree with decisions" and the PO frame (CON / LAM / SEM)

The PO frame was settled once and applied verbatim across all five items: **personer i høyere
posisjoner** / **personer i lavere posisjoner**. *Posisjoner* (positions) was chosen over
*stillinger* (employment posts), which would add a workplace specificity the general English
"positions" lacks (LAM), and over *overordnede/underordnede* (superiors/subordinates), which names a
direct reporting relationship the source deliberately avoids with its descriptive periphrasis (SEM).
*Personer* was preferred to *mennesker* (foregrounds humanness, irrelevant) and *folk* (colloquial),
matching the de/da precedent.

For PO4's "disagree", variants were **A) "ikke være uenige i beslutninger"** (not be in disagreement
with decisions), **B) "ikke motsi beslutninger"** (not contradict decisions, the route German took
with *widersprechen*), and **C) "ikke stille spørsmål ved beslutninger"** (not call decisions into
question). B and C are lighter and more idiomatic, but both shift from *holding* a dissenting view to
*voicing* one — a real strengthening that, against Norway's egalitarian norm, would have respondents
rating a harsher proposition than the English (CON). Chose **A**, with CON decisive over naturalness.

## 3. LT2 "Persistence" gloss (CON / semantic precision)

The parenthetical gloss had to name the Hofstede "persistence" concept. Variants: **A) "Vedholdenhet"**
(persistence, sticking-to-it in a task) vs. **B) "Utholdenhet"** (endurance, staying-power) vs.
**C) "Standhaftighet"** (steadfastness) vs. **D) "Iherdighet"** (diligent perseverance). *Utholdenhet*
is the more everyday Norwegian word, but its primary sense is *physical* endurance (stamina), which
narrows and slightly misdirects the concept — the same reason the Danish notes rejected *udholdenhed*
in favor of *vedholdenhed*. C was reserved for LT3's "steadiness" (*standhaftighet*), and reusing it
here would collapse the source's distinct "persistence"/"steadiness" pair. Chose **A) Vedholdenhet**,
which names persistence-in-a-pursuit precisely and keeps LT2 and LT3 lexically distinct as the source
does. "Thrift" (LT1) → **Sparsommelighet**, the saving-as-virtue term, over *gjerrighet* (stinginess,
plainly negative) (CON).

## Structural / uniformity notes

- PO1–PO5 keep a fixed frame: "personer i høyere posisjoner" / "personer i lavere posisjoner",
  mirroring the source's verbatim repetition.
- PO1 "consulting" → *rådføre seg med* and PO2 "ask the opinions of" → *spørre … om deres mening* are
  kept lexically distinct, as in the source. "make decisions" → *ta beslutninger*, and PO4 keeps the
  same stem *beslutninger*.
- "instructions" stays a standalone *instruksjoner* across UN1, UN2 and UN5, preserving the source's
  within-group repetition. UN5 "instructions for operations" → "Instruksjoner for arbeidsoppgaver",
  reading "operations" as work tasks; the compound *driftsinstruksjoner* was rejected as
  plant/machinery-specific.
- "what I'm expected to do" (UN1) and "what is expected of me" (UN3) both become "hva som forventes av
  meg" — the source varies only syntactically, not conceptually.
- "Individuals" is *individer* throughout CO1/CO2/CO5, preserving the stem link to *individuelle
  belønninger* (CO3) and *individuell suksess* (CO4). The more idiomatic *den enkelte* would have
  broken that link.
- "success" is *suksess* everywhere it recurs (CO4, LT5, LT6); "success in the future" is identically
  "suksess i fremtiden" in LT5 and LT6.
- CO2 "difficulties" → *vanskeligheter* deliberately shares a stem with MA3's *vanskelige problemer*,
  because the source shares one too (difficulties / difficult). CO2 stays lexically distinct from CO6's
  *gruppelojalitet*: the source keeps "stick with the group" (CO2) apart from "group loyalty" (CO6), so
  the loyalty stem was reserved for CO6 (UNI applied negatively — as the Danish/Dutch notes also did,
  rather than the German *treu bleiben* route that collapses the two).
- "usually" is *vanligvis* in both MA2 and MA3 (UNI).
- LT2/LT5/LT6 use a uniform "Å + infinitive" phrase form; LT1, LT3, LT4 are noun phrases, exactly as in
  the source. The parenthetical glosses in LT1 and LT2 are translated.
- MA1 "professional career" → *profesjonell karriere*. The amateur/professional reading of *profesjonell*
  exists in Norwegian, but it exists in the English source too, so AMB is not engaged.
- MA3 "forcible approach" → *kraftfull tilnærming*; MA4 "jobs" → *oppgaver*, reading "jobs" broadly as
  tasks (nl *taken*, fr *tâches*, da *opgaver*). This reuses *oppgaver* from PO5's "tasks", but the
  overlap is cross-group rather than within-group, so UNI does not forbid it, and the source's own
  "tasks"/"jobs" are near synonyms.
- `scales-no.csv`: *helt uenig* / *helt enig* is the conventional Norwegian Likert pair in scientific
  questionnaires. For the importance scale, the bipolar *svært uviktig* / *svært viktig* was kept
  (matching the source's bipolar "very unimportant"/"very important") in preference to a unipolar
  anchor such as *svært lite viktig*.
- `dimensions-no.csv` uses established Norwegian Hofstede terms: *maktdistanse*, *usikkerhetsunngåelse*
  (with *unngåelse* "avoidance"), *kollektivisme*, *langsiktig orientering*, *maskulinitet*.

## Confidence

Norwegian Bokmål is a high-resource language, structurally close to English and extremely close to
Danish, which was available as a cross-check. No capability caveats apply. The one point a native
reviewer should look at first is CO3/CO5 *gruppens vel*: the choice is deliberate and defended above,
but *vel* is the most formal register note in the instrument, and a reviewer weighting naturalness over
the state/interest distinction might prefer *gruppens beste*.
