# CVscale translation notes: English → Estonian

**Source language:** English · **Target language:** Estonian (eesti keel)

Files written to `instruments/`:
- `cvscale-et.tsv` — 26 items across the five groups
- `dimensions-et.csv` — dimension names, English kept after " / "
- `scales-et.csv` — Likert anchors (`ei nõustu üldse`…`nõustun täielikult`; `väga ebaoluline`…`väga oluline`)

## Target-language characterization

Estonian is the first Finno-Ugric language in this corpus (Finnish and Hungarian are still
open), so none of the existing translations offered structural precedent — only the
harmonization decisions on individual items, which I did follow. Four properties shaped the
work.

**No grammatical gender at all.** Estonian has none — not on nouns, not on adjectives, and
crucially not in the third-person pronoun (*ta* covers he/she). The gender-neutrality
requirement is therefore free here, in a way it is not for German, Romanian, or the Slavic
translations: PO, UN, CO, and LT expose no gender whatever, and MA names *mehed*/*naised*
only because the source does. Estonian likewise has no T/V problem in this instrument, since
only UN1 and UN3 speak in the first person.

**Compounding + productive derivation.** Like German and Finnish, Estonian compounds freely
and derives abstract nouns at will (*-mine*, *-us*, *-likkus*). This makes UNI cheap to
honor — *grupi edu* / *üksikisiku edu* (CO4) reproduces the source's parallel with no
strain — but equally cheap to violate by accident. Three near-misses had to be actively
blocked: *otsustavalt* in LT2 (would share *otsus-* with PO1/PO4's "decisions"), *hoolimata*
in LT2 (would share *hool-* with LT1's "Careful"), and *isiklik* in CO1 (would share a stem
with LT3's "Personal"). The source keeps each of those pairs lexically distinct, so the
translation does too.

**Vocabulary layering, not register split.** Written Estonian is remarkably uniform — the
North-Estonian-based standard is what every respondent reads, and Võro/Seto is not a
competing written variety at this register. So comparability across respondents is not at
risk. The live axis is instead *lexical layer*: for many concepts Estonian offers a native
Finno-Ugric word beside an international loan (*juhis/instruktsioon*, *üksikisik/indiviid*,
*vastuseis/opositsioon*). The purist layer is usually the neutral one here, and the loan is
usually the one carrying a foreign or narrowed sense — the opposite of the Romanian
situation, where the Latinate member was the marked one.

**Polysemy is the main hazard.** Estonian's ordinary vocabulary is full of secondary senses
English lacks, and several land squarely on other dimensions of *this* instrument (see LT1
below) or on wrong domains entirely (*operatsioon* = surgery, *protseduur* = spa treatment,
*karjäär* = quarry). Most of these are killed by collocation; two were not, and drove the
decisions below.

**Connotation.** Estonian ordinary usage does not load authority, group loyalty, or gender
roles with more obligatory valence than neutral English — if anything, Estonian's cultural
individualism means words like *omakasu* ("self-interest") carry a *pejorative* charge the
English lacks, which is a CON risk in the CO group specifically. See the CO1 note.

Estonian is a language I can work in at close to the level of the major European languages
in this set; it is small but well-documented and well-represented. My one reservation is
below-average confidence about which Likert anchors are *conventional* in Estonian
scientific practice as opposed to merely correct — see the scales note. A native reviewer
should check that pair first.

## 1. LT1 "Thrift" (AMB — an ambiguity that lands on another dimension)

The natural Estonian words for "thrift" all carry a second sense English lacks:

- **A) *säästlikkus*** — thriftiness, from *säästma* "to save, to spare".
- **B) *kokkuhoidlikkus*** — thriftiness, from *kokku hoidma* "to economize".
- **C) *kasinus*** — frugality, austerity.

C is out on CON: *kasinus* is the ascetic/religious virtue term (abstinence, self-denial),
a charge English "Thrift" does not carry — the same trap Romanian's *cumpătare* skirts.

B is the interesting rejection. *Kokku hoidma* means both "to economize" **and** "to stick
together", and the derived *kokkuhoidlik* inherits both: *kokkuhoidlik pere* is either a
thrifty family or a close-knit one. The second sense is not merely an ambiguity absent from
the source (AMB) — it is *the CO2 concept*, "Individuals should stick with the group". In an
instrument that scores Collectivism and Long-Term Orientation as separate dimensions,
glossing an LT item with a word whose alternate reading names the CO construct is a
psychometric hazard, not just a stylistic one. The item text (*Rahaga hoolikas
ümberkäimine*) does pin the money reading, exactly as the Romanian notes argue for
*cumpătare* — but the gloss word is what a skimming respondent anchors on.

Chose **A**. *Säästlikkus* has its own faint overtone (*säästlik tarbimine*, economical/
sustainable consumption), but that overtone is weak, attaches more to *säästev* than to
*säästlik*, and — decisively — does not collide with any other dimension in this
questionnaire. Where two candidates both carry an extra sense, prefer the one whose extra
sense is outside the instrument.

## 2. PO4 "should not disagree with decisions" (LAM + CON beat UNI)

Estonian *nõustuma* ("to agree") under "should not" stacks into **"ei peaks mitte
nõustuma"** — grammatical but a badly doubled negative, the same trap Romanian hits. Worse,
*nõustuma* is also the scale anchor (*ei nõustu üldse*), so using it in the item text would
echo the response options. Three repairs:

- **A) *ei peaks olema eriarvamusel … otsuste suhtes*** — should not be of a differing
  opinion regarding the decisions.
- **B) *ei peaks vastu vaidlema … otsustele*** — should not argue against / talk back to
  the decisions.
- **C) *ei peaks vaidlustama … otsuseid*** — should not contest/challenge the decisions.

C is out immediately: *vaidlustama* is the formal-appeal verb (contesting a tender, a grade,
a ruling), importing an administrative-procedural overtone English "disagree" lacks — the
precise error Romanian avoided with *a contesta*.

B vs. A is the real choice, and it is the *converse* of the Romanian outcome. B is what a
native would most likely write, but *vastu vaidlema* means "to talk back, to contradict",
which (i) is stronger than the mild "disagree" (CON) and (ii) fixes the *voiced* reading,
whereas English "disagree with decisions" leaves holding-vs-voicing open (LAM). A is mild,
avoids the double negative, and — because *eriarvamusel olema* covers a silently held view
as readily as a stated one — preserves the source's ambiguity intact.

Against A: *eriarvamus* shares the *arvamus* stem with PO2's *arvamust* ("opinions"), while
the source uses unrelated words ("disagree" / "opinions"). That is UNI applied negatively —
a forged link.

Chose **A**. The decisive argument: the Romanian translation paid a LAM cost for the voiced
reading only because Romanian offered *no* mild non-voiced option; Estonian does, so there is
no reason to buy the cost. And the forged link A creates is *within* the PO group, between
two items already about subordinates' opinions of superiors — far cheaper than Romanian's
*cross-group* concern, and cheaper than B's twin CON+LAM violation.

## 3. MA4 "can do better" (LAM, unavoidable)

The corpus has already settled that "jobs" here means kinds-of-work, not professions (de
*Tätigkeiten*, nl *taken*, it *lavori*, ru *виды работы*, ro *activități*; fr was explicitly
corrected off *métiers* in a226e72). Estonian follows with *tegevused*: *ülesanded* is PO5's
word for "tasks" and *tööd* would echo UN4/LT6's *töö-*, both forging cross-group links the
source does not have; *ametid* is the rejected trades reading.

The harder problem is "can", which Estonian cannot render with one word:

- **A) *oskab*** — knows how to, has the skill/knack for.
- **B) *suudab*** — is capable of, has the capacity for.
- **C) *teeb alati paremini*** — simply "always does better", dropping the modal.

English "can" is ambiguous between learned skill and innate capacity, and MA4's whole point
is essentialist innate aptitude — so LAM says preserve the ambiguity, and neither A nor B
does. C preserves it by not resolving it, but converts a capability claim into a factual
one, which is a real change of meaning, not a hedge.

Chose **A**. Decisive: B foregrounds physical capacity and would thereby narrow the item to
physically demanding work — a SEM narrowing, since MA4 is meant to range over any kind of
work (its neighbours are MA1's career and MA3's problem-solving). A is also the default
Estonian collocation for "can do (a kind of work)", and *oskama* is not strictly
learned-skill: *ta oskab inimestega ümber käia* ("he has a knack with people") is an innate
reading. So A leaks less of the source's ambiguity than it first appears.

## Structural / uniformity notes

- **PO group:** "people in higher/lower positions" → *kõrgemal/madalamal positsioonil olevad
  inimesed* in all five items, matching the corpus consensus on "positions"
  (de/es/pt/fr/it/nl/ro). *Ametikoht* was rejected as narrowing to formal employment posts;
  *ülemused/alluvad* ("superiors/subordinates") was rejected as lexicalizing the very
  relation the item is probing.
- **PO1** uses *nõu pidamata* ("without conferring"), not *nõu küsimata* ("without asking
  advice"), deliberately: PO2 already owns *küsima* ("ask"), and the source keeps
  "consulting" (PO1) and "ask the opinions" (PO2) distinct.
- **PO3** "social interaction" → *sotsiaalset läbikäimist*. *Suhtlus/suhtlemine* is the
  everyday Estonian word for communication **including work communication**, so *sotsiaalset
  suhtlust* risks collapsing PO3 into PO1/PO2 (AMB). *Läbikäimine* names association and
  consorting specifically, which is what the item probes — social distance, not task
  communication. Parallel to German *sozialer Umgang*.
- **PO5** "tasks" → *ülesandeid*, with *delegeerima* — the standard Estonian management
  collocation.
- **UN group:** *juhised* recurs across UN1, UN2, UN5 and *protseduur-* across UN2, UN4,
  preserving the source's within-group repetition. UN2 uses *järgima* ("follow"), not
  *kinni pidama* ("comply with/observe"), which would add a deference charge belonging to
  the PO field (SEM). "Closely" → *täpselt*, not *hoolikalt*, to keep *hool-* as LT1's stem.
- **UN4/UN2 "procedures"** → *tööprotseduurid* / *protseduure*. Estonian *protseduur* has a
  salient medical-and-cosmetic sense (*iluprotseduurid*), but it is unreachable under
  *järgima* — one follows procedures, one undergoes treatments — and dead inside the
  compound. *Töökord* was rejected as genuinely ambiguous with "working order" (*masin on
  töökorras*), an ambiguity English lacks (AMB).
- **UN5 "Instructions for operations"** → *Toimingute juhised*. *Operatsioon* is
  surgical/military in Estonian and would have imported a plainly wrong reading;
  *toiming* is the ordinary administrative/technical word for an operation
  (*pangatoimingud*), which preserves the source's vagueness without adding a wrong sense
  (LAM/AMB) — the same repair Romanian made with *operațiuni* over *operații*.
- **UN1/UN3:** "what is expected of me" is *mida minult oodatakse* in both, as in English.
  UN1's "spelled out" → *lahti kirjutatud*, a close idiomatic match.
- **CO group — "Individuals":** *üksikisik* renders all six occurrences of the source's
  *individual-* stem, as noun (CO1, CO2, CO5) and as genitive attribute (*üksikisiku tasud*
  CO3, *üksikisiku edu* CO4, *üksikisiku eesmärgid* CO6). This is a better outcome than the
  Romanian or German solutions: it reproduces the source's stem recurrence across the whole
  group *and* keeps the CO4/CO3 parallel exact (*grupi edu* / *üksikisiku edu* — two genitive
  attributes, as in the source), *and* avoids *indiviid*, which in Estonian is cold,
  technical, and faintly shady in the singular (*kahtlane indiviid*) — the same pejorative
  tinge Romanian's *individ* has.
- **CO1 "self-interest"** → *enda huvid*, not *isiklikud huvid* and not *omakasu*.
  *Omakasu* is squarely pejorative in Estonian (*omakasupüüdlik* = self-serving, mercenary),
  a charge the neutral English lacks (CON). *Isiklikud huvid* is neutral but would share
  *isiklik* with LT3's "Personal steadiness", forging a cross-group link the source does not
  have (UNI, negatively applied) — the same trap Romanian sidesteps with *interesul propriu*.
  *Enda* also carries the reflexive emphasis of "self-".
- **CO1 "for the group"** → *grupi nimel*, not *grupi heaks* ("for the good of"), which would
  share *hea-* with CO3/CO5's *heaolu* ("welfare"); the source keeps these distinct.
- **CO2 vs. CO6:** "stick with the group" → *jääma grupi juurde*, avoiding any loyalty word
  so that CO6's *grupilojaalsust* stays the group's only loyalty item — the same separation
  Romanian and French protect (and which German does not, using *treu* in CO2).
- **CO group uniformity:** *grupp* throughout (not *rühm*, which reads as a squad or a school
  class); *heaolu* identical in CO3 and CO5; *eesmärgid* serves CO5 and CO6.
- **LT2 "Persistence"** → *visadus* (tenacity), keeping *püsivus* free for LT3's
  "steadiness" — the source uses distinct words. "Resolutely" → *kindlameelne*, **not**
  *otsustavalt*, which shares *otsus-* with PO1/PO4's "decisions" (the same reasoning that
  keeps *hotărâre* out of Romanian's MA3).
- **LT2 "opposition"** → *vastuseis*. Estonian *opositsioon* is exclusively political, so
  unlike Romanian — which could preserve the English political-Opposition polysemy with
  *opoziției* — using it here would **flip** the primary reading rather than mirror it. The
  source's minor polysemy is lost; this is the right loss to take.
- **LT form:** the source mixes noun phrases (LT1, LT3, LT4) with gerund phrases (LT2, LT5,
  LT6). Estonian's *-mine/-mine*-type nominalization covers both English patterns, so the
  distinction collapses naturally rather than being erased by choice; the *da*-infinitive was
  rejected because it would read as an imperative instruction, not a value label.
- **UNI on "success":** *edu* renders every occurrence (CO4, LT5, LT6); "success in the
  future" is *tuleviku edu* in both LT5 and LT6.
- **UNI on "important":** *oluline* renders every occurrence (PO5, UN1, UN2, UN3, UN5, CO3,
  CO4, MA1) and the `important5` anchors. *Tähtis* is an equally good synonym; the point is
  that only one of the two is used, since English uses only "important". UN4's "helpful" →
  *on abiks*, distinct, as in the source.
- **MA3** "active, forcible approach" → *aktiivset, jõulist lähenemisviisi*. *Jõuline* is
  forceful/vigorous without implying violence, matching the source. *Lähenemisviis*, not bare
  *lähenemine*, which also means physically approaching (AMB).
- **MA1** "professional career" → *ametialane karjäär* (cf. German *berufliche Karriere*).
  Estonian *karjäär* is homonymous with "quarry", but the sense is unreachable under
  *ametialane*; this is a dictionary homonym, not a live ambiguity.
- **Dimension names** use the Estonian management-literature terms: *võimudistants*,
  *ebakindluse vältimine*, *pikaajaline orientatsioon*. *Võimukaugus* is a defensible
  alternative for PO; *võimudistants* is the more common calque in Estonian textbooks.
  *Pikaajaline* also renders LT4's "Long-term", matching the source's own repetition.
- **Scale anchors:** *ei nõustu üldse*…*nõustun täielikult* is the standard Estonian 5-point
  agreement pair. For `important5` I kept the source's symmetry with *väga ebaoluline*…*väga
  oluline*, following German (*sehr unwichtig*/*sehr wichtig*) and Dutch rather than the
  asymmetric Romance and Ukrainian solutions. The idiomatic Estonian alternative is *üldse
  mitte oluline* ("not important at all"), which is more common in Estonian survey practice
  but breaks the *väga…väga* symmetry a rating scale wants. This is the single choice in this
  translation I would most like a native reviewer to second-guess.
