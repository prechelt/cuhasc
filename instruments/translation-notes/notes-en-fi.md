# CVscale translation notes: English → Finnish

**Source language:** English · **Target language:** Finnish (suomi)

Files written to `instruments/`:
- `cvscale-fi.tsv` — 26 items across the five groups
- `dimensions-fi.csv` — dimension names, English kept after " / "
- `scales-fi.csv` — conventional Likert anchors (`täysin eri mieltä`…`täysin samaa mieltä`;
  `ei lainkaan tärkeää`…`erittäin tärkeää`)

## Target-language characterization

Finnish is the first non-Indo-European language in this set that is not also low-resource for
me. Four properties drove the item-level choices.

**No grammatical gender at all.** Finnish has a single third-person pronoun *hän* for both
sexes and marks no gender on nouns or adjectives. The gender-neutrality instruction is
therefore free everywhere except the MA group, where the source names the sexes explicitly
and Finnish simply says *miehet* / *naiset*. Nothing in PO, UN, CO, or LT exposes a gender.
Nor is there a T/V problem: only UN1 and UN3 speak in the first person, and *minulta
odotetaan* is neutral across every variety.

**Register / variety split.** The gap between written standard (*kirjakieli*) and everyday
speech (*puhekieli*) is unusually wide — *minä ei oo* vs. *minä en ole* — but it is a
speech/writing split, not a regional one, so a questionnaire written in plain kirjakieli is
equally comparable for every respondent. The real risk is the *other* direction: Finnish
officialese (*virkakieli*) is a recognizable register with its own vocabulary, and reaching
for it would load the normative items with an administrative charge the plain English lacks.
This decided the modal: **pitäisi**, not **tulisi**. Both are conditional deontics meaning
"should", but *tulisi* is the verb of statutes and memoranda; *pitäisi* is what an ordinary
Finn says. English "should" is unmarked, so *pitäisi* matches under CON. The same reasoning
kept *noudattaa* (UN2, the neutral verb for complying with instructions) rather than any
verb carrying deference — Romanian's *a respecta* trap, which would have bled UN toward PO.

**Agglutination and compounding.** Derivational morphology is extremely productive, so UNI
is cheap to honor: *yksilö* (CO1/2/5) and *yksilön* (CO3/4/6) reproduce the source's own
individual- stem recurrence exactly, as do *ohje-* across UN1/UN2/UN5 and *menestys* across
CO4/LT5/LT6. The flip side is that compounding makes accidental links almost free — Finnish
will happily fuse two items' vocabulary into one word — and the small native stock of
work-related roots (*työ*, *tehtävä*, *toiminta*) had to be rationed carefully across PO5,
UN4, UN5, LT6, and MA4 (see §1).

**Polysemy.** Finnish has little of the classical/learned layering that makes Romance and
Slavic translations tricky; the danger is instead the native compound whose salient use is
a fixed genre (*toimintaohje* = emergency instructions, see below). One near-miss worth
recording: *uskollisuus* (CO6 "loyalty") is built on *usko* "faith/belief", but modern
Finnish keeps them apart — *asiakasuskollisuus* (customer loyalty), *merkkiuskollisuus*
(brand loyalty) are ordinary business terms, so *ryhmäuskollisuus* carries no religious
tinge.

**Capability caveat.** Finnish is mid-resource for me. I am confident in the grammar,
the case government, and the dimension terminology, which is standardized in the Finnish
management literature (*valtaetäisyys*, *epävarmuuden välttäminen*). I am *less* confident
than I would be for German or French about fine collocational naturalness — specifically
whether *raha-asioiden hoitaminen* (LT1), *lujuus* for "steadiness" (LT3), and the
nominalization-heavy LT phrasing read as smoothly to a native as I judge them to. Those
three are the places a native review would pay off most.

## 1. MA4 "some jobs" (SEM / UNI, cross-group distinctness — the hardest item)

The corpus has already settled that "jobs" here means kinds-of-work, not professions
(German *Tätigkeiten*, Dutch *taken*, Russian *виды работы*; French was explicitly corrected
away from *métiers* in a226e72). Finnish has exactly three roots available for that reading,
and **each one is already spoken for by another item**:

- **A) *töitä*** (työ = work/job) — but *työ-* is LT6's root (*kova työnteko*) and UN4's
  (*työssä*).
- **B) *tehtäviä*** (task/assignment) — but *tehtävä* is PO5's word (*delegoida tärkeitä
  tehtäviä*).
- **C) *toimia* / *toimintoja*** (activities/functions, the calque of German *Tätigkeiten*) —
  but *toiminta-* is UN5's root (*toimintaohjeet*).
- **D) *ammatteja*** (professions) — the reading the corpus rejected.
- **E) *askareita* / *hommia*** — chores (domestic, wrong connotation) / colloquial
  (register break).

So UNI could not be satisfied negatively at all; the question was only which unwanted link
does least damage. B is the worst: *tehtävä* is the noun of *delegation* in this instrument,
and MA4 would then read as "there are some assignments a man does better" — importing PO5's
authority frame into a gender item and blurring two dimensions (SEM). C is nearly as bad and
additionally sounds bureaucratic. Chose **A**, *töitä*.

The decisive argument: LT6's *työnteko* and MA4's *töitä* are in *different dimensions that
do not compete*, and *työ* is Finnish's basic, unavoidable word for work — a Finn does not
perceive "hard work" and "some jobs" as a lexical echo any more than an English speaker
perceives one between "Working hard" and "jobs". The link is real but inert. The PO5 link
would not have been.

Rendered: *On olemassa joitakin töitä, jotka mies osaa aina tehdä paremmin kuin nainen.*
Note *osaa* (knows how to) rather than *pystyy* (is physically able to) — English "can do
better" is about skill here, and *pystyy* would drift toward physical capacity, a claim the
item does not make (CON).

## 2. PO1 "without consulting" (UNI applied negatively)

English uses two distinct verbs in adjacent items: "consulting" (PO1) and "ask the opinions"
(PO2). Finnish variants for PO1:

- **A) *kuulematta alemmassa asemassa olevia*** — without hearing/consulting.
- **B) *kysymättä neuvoa alemmassa asemassa olevilta*** — without asking advice from.
- **C) *konsultoimatta…*** — the loanword.

B is the most obvious phrasing and the one a translator reaches for first — but it puts
*kysyä* in PO1, and PO2 already is *kysyä* (*ei pitäisi kysyä … mielipiteitä*). B would fuse
the source's two distinct verbs into one and additionally smuggle in *neuvo* "advice", which
appears nowhere in the source. C is business-loan register drift (CON).

Chose **A**. *Kuulla* in the abessive *kuulematta* is the standard Finnish verb for
consulting parties before a decision (*päätös tehtiin asianosaisia kuulematta*), which is
precisely PO's semantic field (SEM), and the partitive object fixes the consult reading over
the bare "hear" reading. The decisive argument was UNI applied negatively: preserving the
PO1/PO2 verb contrast the source deliberately has.

## 3. The `important5` anchors: "very unimportant" (conventional translation vs. literal)

Finnish has no idiomatic bipolar negative importance anchor. Variants:

- **A) *ei lainkaan tärkeää*** — not at all important.
- **B) *erittäin epätärkeää*** — very unimportant (the literal calque).
- **C) *täysin merkityksetöntä*** — completely insignificant.
- **D) *hyvin vähän tärkeää*** — very little important (the Romance solution).

B is the exact structural match but *epätärkeä* is rare and stilted in Finnish — the same
objection Romanian raised against *foarte neimportant* and Polish sidestepped with
*zupełnie nieważne*. C overshoots badly (CON): "insignificant" is a stronger and more
dismissive claim than "unimportant". D is grammatical but not a phrase Finnish
questionnaires use. Chose **A**: *ei lainkaan tärkeää … erittäin tärkeää* is the
conventional pair in Finnish scientific questionnaires, and the skill directs me to use the
conventional anchors where they exist. The cost is honest and worth recording: A is a
unipolar zero-anchor ("not at all important") where English is bipolar ("very unimportant"),
so the Finnish scale's low end is very slightly less negative than the source's. No
idiomatic Finnish phrasing preserves the bipolarity.

Both anchor pairs are in the **partitive** (*tärkeää*, not *tärkeä*) because every LT item is
an abstract nominalization or mass-like noun phrase, which governs a partitive predicative in
Finnish: *Pitkän aikavälin suunnittelu on erittäin tärkeää.*

## Structural / uniformity notes

- **PO group:** "people in higher/lower positions" → *ylemmässä/alemmassa asemassa olevat
  ihmiset* in all five items. *Asema* is singular throughout: Finnish generics prefer the
  singular (*olla korkeassa asemassa*), and plural *asemissa* would be unidiomatic without
  adding anything. The pair *ylempi/alempi* is chosen over *korkeampi/matalampi* because
  *matala asema* is not a Finnish collocation while *ylempi/alempi* is the standard
  hierarchical pair (cf. *ylempi toimihenkilö*). *Esimiehet/alaiset* (superiors/subordinates)
  was rejected as far too specific: it would restrict a deliberately generic item to
  workplace line management.
- **"People" vs. "Individuals":** *ihmiset* (PO) vs. *yksilöt* (CO), preserving the source's
  lexical opposition and matching the corpus (de *Menschen*, nl *Mensen*). *Henkilöt* was
  rejected for PO as bureaucratic (CON).
- **PO4:** *ei pitäisi olla eri mieltä* — Finnish negates cleanly here and needs none of the
  repairs Romanian required. This does reuse the scale anchor's phrase (*eri mieltä*), the
  same questionnaire-design blemish Romanian accepted; every alternative (*vastustaa* =
  oppose, *kyseenalaistaa* = call into question) is markedly stronger than English "disagree"
  (CON), so the blemish is the lesser evil.
- **UN group:** *ohje-* recurs across UN1, UN2, UN5 and *menettelytavat* across UN2 and UN4,
  reproducing the source's within-group repetition of "instructions" and "procedures". UN4 is
  *Standardoidut menettelytavat työssä* rather than the more compact *työmenetelmät* (work
  methods) precisely to keep that UN2/UN4 "procedures" link visible.
- **UN1 vs. UN3:** the source distinguishes "what I'm expected **to do**" (UN1) from "what is
  expected of me" (UN3), and Finnish reproduces the distinction at no cost: *mitä minun
  odotetaan tekevän* vs. *mitä minulta odotetaan*. (Romanian collapsed the two; Finnish need
  not.) UN1 uses *esitetty* for "spelled out" rather than *kerrottu*, because UN3's "inform
  me" is already *kertovat minulle* — the source uses different verbs, so the translation
  must too (UNI, negative).
- **UN5 "Instructions for operations"** → *Toimintaohjeet ovat tärkeitä.* The source noun is
  deliberately vague, and the Finnish compound *toimintaohje* is vague in the same way while
  keeping the *ohje-* stem. Rejected: *käyttöohjeet* (= user manual, far too narrow), and the
  analytic *toimintaa koskevat ohjeet* (stiff, and no gain). Recorded risk: *toimintaohjeet*
  has a salient use in emergency/crisis genres (*toimintaohjeet hätätilanteessa*) — an
  overtone English lacks (AMB). I judged it neutralized by context: UN4's workplace
  procedures and UN2's instructions stand immediately before it and fix the workaday reading.
  This is the one AMB compromise in the file.
- **CO1:** *uhrata oma etunsa ryhmän hyväksi*. *Oma etu* is the exact equivalent of
  "self-interest", and its stem stays clear of LT3's *henkilökohtainen* ("Personal"), which
  the source likewise keeps distinct.
- **CO2 vs. CO6:** *pysyä ryhmässä myös vaikeuksien keskellä* uses no loyalty word, so CO6's
  *ryhmäuskollisuus* remains the group's only loyalty item — the separation the source has
  and the French and Romanian translations also protect. CO6 is *Ryhmäuskollisuuteen pitäisi
  kannustaa* (illative + *kannustaa*), the natural Finnish construction for encouraging
  toward something; *kannustaa* takes a person as object, so the abstract-object calque was
  not available.
- **CO3/CO4:** "individual rewards" / "individual success" are rendered with the **genitive**
  *yksilön palkkiot* / *yksilön menestys*, not the adjective *yksilölliset*. Finnish
  *yksilöllinen* means "individualized, personalized" — an AMB the source does not have; the
  genitive says what English means (rewards accruing to the individual) and mirrors the
  *Ryhmän X … yksilön X* parallel exactly.
- **CO3/CO5:** *ryhmän hyvinvointi* is identical in both, as "group welfare" is in the source;
  *tavoitteet* serves CO5 and CO6.
- **LT1 "Thrift"** → **Säästäväisyys**, the established Finnish virtue term, neutral-positive
  like the English (*kitsaus* = stinginess was rejected outright on CON). The item text is
  *Raha-asioiden huolellinen hoitaminen*: *raha-asioiden hoitaminen* is the idiomatic Finnish
  for managing one's money, where the literal *rahan hoitaminen* is odd and *rahan käsittely*
  suggests physically handling cash.
- **LT2 "Persistence"** → *Sinnikkyys*. "Resolutely" → *päättäväinen*; note this word is then
  deliberately **kept out of MA3** (see below). "Opposition" → *vastustus*: Finnish uses a
  wholly separate word (*oppositio*) for the parliamentary sense, so the source's faint
  political-Opposition polysemy is not reproducible here (LAM cost accepted — no Finnish
  option carries it, and *vastustus* is unambiguously the intended reading).
- **LT form:** the source mixes noun phrases (LT1, LT3, LT4) with gerund phrases (LT2, LT5,
  LT6). Finnish nominalizes both, which is what Finnish does with such headings; the
  *-minen* forms (*hoitaminen*, *eteneminen*, *luopuminen*) carry the gerund flavor. LT6 is
  the exception: *Kova työnteko* rather than the grammatical but graceless *Kovasti
  työskenteleminen*. *Työnteko* is itself a verbal compound, so the loss is small.
- **UNI on "success":** *menestys* renders every occurrence (CO4, LT5, LT6); "for success in
  the future" is the identical *tulevaisuuden menestyksen vuoksi* in LT5 and LT6, as in the
  source.
- **MA1 "professional career"** → *Ammattiura*. *Työura* (the most frequent Finnish word for
  a career) was rejected on UNI grounds: it would drag the *työ-* stem into a third group
  where the source says "professional", not "work". *Ammatillinen ura* was rejected on AMB
  grounds: *ammatillinen* collocates overwhelmingly with vocational **education**
  (*ammatillinen koulutus*), a reading English "professional" does not invite.
- **MA2:** the semicolon and the exact parallelism of the two clauses are preserved; both
  instruments are adessive (*loogisella analyysillä* / *intuitiolla*), matching the source's
  repeated "with".
- **MA3 "active, forcible approach"** → *aktiivista ja voimakasta lähestymistapaa*.
  *Päättäväinen* (determined) was rejected on UNI grounds — it is LT2's word for
  "resolutely", and the source uses distinct words in the two items (the same trap Romanian
  found with *hotărâre*). *Voimakas* carries the force of "forcible" without *voimallinen*'s
  literary tinge. Finnish coordinates with *ja* where the source uses an asyndetic comma;
  the bare comma reads as an unfinished list in Finnish.
- **Dimension names** use the established terms of the Finnish management literature:
  *valtaetäisyys*, *epävarmuuden välttäminen*, *pitkän aikavälin orientaatio* (consistent
  with LT4's *pitkän aikavälin suunnittelu*), *kollektivismi*, *maskuliinisuus*.
- **Modal:** *pitäisi* throughout the PO and CO groups, never *tulisi* — see the
  characterization above.
