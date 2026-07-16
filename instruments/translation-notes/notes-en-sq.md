# CVscale translation notes: English → Albanian

**Source language:** English · **Target language:** Albanian (shqip)

Files written to `instruments/`:
- `cvscale-sq.tsv` — 26 items across the five groups
- `dimensions-sq.csv` — dimension names, English kept after " / "
- `scales-sq.csv` — Likert anchors (`nuk pajtohem aspak`…`pajtohem plotësisht`;
  `shumë e parëndësishme`…`shumë e rëndësishme`)

## Target-language characterization

Albanian is an isolate branch of Indo-European with no close relative, written in a standard
(*gjuha letrare*) codified in 1972 on a predominantly Tosk base. Four properties of the
language bear directly on the translation rules.

**Register / variety split.** The respondent pool spans Albania, Kosovo, and North Macedonia.
Written standard Albanian is shared across all three, but the everyday lexicon is not: Albania
leans on Italianisms (*jam dakord* "I agree"), Kosovo on native or Slavic-adjacent forms
(*pajtohem*). Wherever the two diverged I chose the native standard form, which is current in
both — this matters most for the scale anchors, where a Tirana-only word would make Kosovar
responses non-comparable. The Gheg/Tosk split does not surface at this register.

**Derivational morphology.** Albanian derives freely, which makes UNI cheap to honor —
*rregull/rregullore* reproduces English *rules/regulations* stem-for-stem, *zgjidh-* covers
MA2's "solve" and MA3's "solving", *individ/individual* covers all six CO items. The same
freedom makes accidental links cheap, and Albanian's small native root inventory means the
same root keeps resurfacing. I had to actively keep *qëndroj* out of CO2 and *kundërshtim* out
of LT2 to avoid forging cross-group ties the source does not have (see below).

**Polysemy / register layering.** The Albanian lexicon is stratified: a native (often
Rilindja-era purist) layer, a Turkish layer, and a Latin/Italian neologistic layer. The native
word is frequently the one carrying a sacral or honor-code charge that the neutral English
lacks — *flijoj* "sacrifice" is ritual slaughter, *besë* is the Kanun's sacred pledge. So in
Albanian the *native* word, not the learned one, is often the AMB/CON risk; this inverts the
pattern seen in the Romance targets of this corpus.

**Connotation & culture.** Traditional Albanian social vocabulary loads hierarchy, group
loyalty, and manliness (*burrëri*) with a markedly more positive and obligatory valence than
the neutral English of the instrument. Since PO, CO, and MA are exactly the dimensions being
measured, any amplification here would bias agreement. Matching valence rather than
naturalness was the recurring tie-breaker.

**Gender & honorifics.** Albanian forces gender on nouns and adjectives and has a live T/V
distinction (*ti*/*Ju*). The PO and CO items are impersonal third-person, so no
respondent-facing gender or address is exposed; *personat* and *individët* refer without
marking the reader. Only UN1 and UN3 speak in the first person, which is neutral. The LT
group's form choice was driven largely by keeping *ti* off the page (see §3).

Albanian is a smaller language than the others in this set (~8 M speakers) and I have less
attested questionnaire text to anchor on — in particular I am not aware of an established
Albanian Hofstede terminology, so the dimension names below are constructed from the standard
management-literature vocabulary rather than quoted from a canonical source. I am confident in
the grammar and the item-level lexical choices; the residual uncertainty is about
*conventionality*, not correctness — chiefly whether `shumë e parëndësishme` or `aspak e
rëndësishme` is the more usual bottom anchor (see §4).

## 1. PO1–PO5, CO1, CO2, CO5, CO6 "should" → *duhet të* (CON, pervasive)

This is the single most consequential decision in the file, and Albanian gives no clean
answer. English "should" is a weak deontic: it advises. Albanian does not grammaticalize the
should/must distinction — *duhet të* covers the whole range from "ought to" to "has to", with
the strength read off context. Variants:

- **A) "duhet të marrin…"** — the plain modal, spanning should/must.
- **B) "do të duhej të merrnin…"** — the conditional, "would have to / ought to".
- **C) "është mirë që të marrin…"** — "it is good that they take", an explicit softener.

B is the only form that isolates the weak reading, and it is what a literal mapping from
German *sollten* or Italian *dovrebbero* would reach for. But Albanian's conditional is
counterfactual-flavored: *do të duhej* invites the inference "…but they don't", which turns a
normative statement into a complaint about the status quo. In a nine-item sweep that would
systematically re-frame what respondents are rating. C dissolves the deontic into an
evaluation and drifts out of the items' field.

Chose **A** throughout. Decisive: *duhet të* is what every attested Albanian normative
questionnaire item uses, so respondents parse it as the instrument's register rather than as a
strong obligation; and it is the only option that stays uniform across all nine items (UNI),
where B would compound its counterfactual tilt item by item. The residual CON cost — *duhet*
sitting slightly stronger than "should" — is real and unavoidable, and worth flagging to
anyone comparing Albanian PO scores against languages whose modal is genuinely weak.

## 2. PO4 "should not disagree with decisions" (CON / UNI, plus a double-negative trap)

Literal negation collapses: "disagree" is *nuk pajtohem*, and "should not disagree" yields
**"nuk duhet të mos pajtohen"** — a stacked double negative that respondents must parse twice.
So the choice was among repairs:

- **A) "nuk duhet t'i kundërshtojnë vendimet…"** — should not object to / contest the
  decisions.
- **B) "nuk duhet të shprehin mospajtim me vendimet…"** — should not express disagreement
  with the decisions.
- **C) "nuk duhet të vënë në dyshim vendimet…"** — should not call the decisions into
  question.

C shifts from disagreeing to doubting the decisions' validity — a different act. B is the
literal repair and is the route Romanian took (*să își exprime dezacordul*); it keeps the
source's exact word, since *mospajtim* is "disagreement" morpheme-for-morpheme. Its problem is
specific to Albanian: my `disagree5` anchors are verb-based (*nuk pajtohem aspak* /
*pajtohem plotësisht*), so B makes the item and the response options share the *pajt-* stem.
The respondent would read "I agree completely that people should not express disagreement" —
the stem collision is exactly where a Power Distance item can least afford to be confusing.

Chose **A**. *Kundërshtoj* ("counter-speak") is the near-exact analogue of German
*widersprechen*, and the corpus consensus on this item is a verb of precisely this class —
de *widersprechen*, it *dissentire*, fr *contester*, pl *kwestionować*. Unlike Romanian's *a
contesta*, Albanian *kundërshtoj* carries no administrative-appeal charge; it is the ordinary
everyday verb for objecting, so A costs nothing under CON while B costs the anchor echo.
Decisive: A is the only option that keeps the item legible against its own response scale.

A knock-on: choosing *kundërshtim* here meant LT2's "opposition" had to move off that stem —
see the structural notes.

## 3. CO6 "Group loyalty" → *Besnikëria ndaj grupit* (CON, the *besa* problem)

- **A) "Besnikëria ndaj grupit"** — the native word; *besnik* "faithful" derives from *besë*.
- **B) "Lojaliteti ndaj grupit"** — the Latinate loan.

*Besë* is the Kanun's sacred word-of-honor, the most culturally loaded concept in the Albanian
moral lexicon, and CO6 is a Collectivism item — precisely where an amplified loyalty word
would push agreement and inflate the score. That is a serious CON argument for B, and B is
otherwise a clean register match: English *loyalty* is itself a Latinate word beside native
*faithfulness*, so B even mirrors the source's own lexical stratum.

Chose **A**. Decisive: the *besë* charge is etymological, not live in this collocation.
Modern *besnikëri* is the ordinary, unremarkable word for loyalty in exactly this sense —
*besnikëria e klientëve* "customer loyalty" — and *ndaj grupit* fixes the mundane reading.
Meanwhile B's cost is not neutrality but bureaucratic distance: *lojalitet* in Albanian reads
as political-vetting vocabulary (*lojaliteti ndaj partisë*), which is its own CON drift, and
away from the plain sociological register the rest of the CO group sits in. A's residual risk
is the marital-fidelity sense of *besnikëri*, which *ndaj grupit* rules out.

## Structural / uniformity notes

- **PO group:** *personat në pozita më të larta / më të ulëta* in all five items, matching the
  corpus consensus on "positions" (de/es/pt/fr/it/nl/ro). *Poste* was rejected as denoting
  formal office specifically; *pozicione* reads physical. *Pozita* does collide with the
  political sense "the governing bloc" (*pozita dhe opozita*), but that sense needs the
  definite singular and is unreachable here.
- **PO1 vs. PO2:** the source distinguishes "consulting" (PO1) from "ask the opinions" (PO2),
  so PO1 uses *pa u konsultuar me* and PO2 *të kërkojnë mendimin*. Rendering PO1 as *pa marrë
  mendimin* would have collapsed the two. Note *konsultohem me* (reciprocal) is the idiomatic
  Albanian frame; transitive *konsultoj* takes documents, not people.
- **PO2** "too frequently" → *tepër shpesh*, not *shumë shpesh* ("very often"), which loses
  the excess reading that carries the item.
- **PO5** "tasks" → *detyra*. Kept distinct from MA4's "jobs", as the source keeps them
  (cf. it *compiti*/*lavori*); nl collapsed both to *taken*, which I did not follow. *Detyrë*
  also means "duty/homework", but *delegoj detyra* fixes the work reading.
- **UN group:** *udhëzime* recurs across UN1, UN2, UN5 and *procedura* across UN2, UN4,
  preserving the source's within-group repetition. The loan *instruksione* was rejected as
  sub-standard. UN2 uses *ndiqen* ("be followed"), not *zbatohen* ("be complied with"):
  *zbatoj* adds a deference charge belonging to the Power Distance field and would bleed UN
  toward PO (SEM) — the same trap Romanian flagged with *a respecta*.
- **UN3:** *rregullat dhe rregulloret* reproduces the source's *rule/regul-* stem sharing
  exactly.
- **UN5** "Instructions for operations" → *Udhëzimet operative*, following it *istruzioni
  operative* and ro *instrucțiuni pentru operațiuni*. The noun *operacionet* was rejected:
  in Albanian it leans military/surgical much harder than English "operations" does (AMB),
  whereas the adjective *operativ* is ordinary business/admin vocabulary. The alternative
  *udhëzimet e punës* (cf. de *Arbeitsanweisungen*) resolves the source's vagueness further
  than the source does, and adds another *punë* to a file that already has three.
- **UN1/UN3:** the source's small difference is preserved — *çfarë pritet të bëj* ("what I'm
  expected to do") vs. *atë që pritet prej meje* ("what is expected of me"), both on *pritet*.
- **CO1** "self-interest" → *interesin vetjak*, not *personal*: the source says "self-interest"
  (CO1) and "Personal steadiness" (LT3) with different stems, and *personal* is already spoken
  for in LT3 (UNI, applied negatively — as in ro). *Vetjak* (← *vetë* "self") is also the
  closer morpheme-level match.
- **CO1** "sacrifice" → *sakrifikojnë*, not native *flijojnë*, which denotes ritual sacrifice
  and would import a sacral reading English lacks (AMB).
- **CO2** "stick with the group" → *të mbeten me grupin*, following ro *să rămână*. Two words
  were deliberately avoided: any loyalty term (so CO6 stays the group's only loyalty item, as
  ro and fr protect; de did not, using *treu bleiben*), and *qëndrojnë* — the most natural
  Albanian verb here — because it shares its stem with LT3's *qëndrueshmëria* ("steadiness"),
  which the source keeps lexically apart.
- **CO group cohesion:** *mirëqenia e grupit* is identical in CO3 and CO5; *synimet* serves
  CO5 and CO6; *individ-* runs through all six items as *individët* / *individuale* /
  *individual*, matching the source's own recurrence. Albanian *individ* carries none of the
  colloquial pejorative tinge that forced discussion in the Romanian notes.
- **CO2 / MA3:** *vështirësi* and *problemeve të vështira* share a stem, exactly as the
  source's "difficulties" and "difficult problems" do — a link preserved, not repaired.
- **LT form:** the source mixes noun phrases (LT1, LT3, LT4) with gerund phrases (LT2, LT5,
  LT6). Standard Albanian has no infinitive — the Gheg *me punue* is not standard — so the
  gerunds could only be mirrored with the impersonal subjunctive (*Të punosh shumë…*), which
  is formally 2nd person singular. In a questionnaire with a live T/V distinction that risks
  reading as *ti*-address, and the instrument otherwise never addresses the respondent. I
  therefore used verbal nouns for all six (*Vazhdimi*, *Heqja dorë*, *Puna*), following de and
  pl, which likewise nominalize. The cost is the loss of the source's noun/gerund contrast — a
  contrast that is subtle in English (both members are nominalizations) and that it/nl/fr/ro
  could preserve only because they have infinitives.
- **LT1 "Thrift"** → **Kursimi**, parallel to it *Risparmio*, fr *Épargne*, es *Ahorro*. The
  dispositional *Kursimtaria* ("thriftiness") is the exact match for English "Thrift" as a
  virtue name and would parallel de *Sparsamkeit* / nl *Spaarzaamheid*, but it is rare enough
  to make respondents stumble; *Kursimi* is the standard term and the item text (*Menaxhimi i
  kujdesshëm i parave*) stands immediately before the gloss and fixes the sense.
  *Koprraci* ("stinginess") is pejorative and was never in play.
- **LT2 "opposition"** → *rezistencës*, following de *Widerstand*, nl *tegenstand*, pl *opór*.
  The stem-mate of PO4's *kundërshtoj* was unavailable here: the source uses "disagree" (PO4)
  and "opposition" (LT2) as different words, and *kundërshtim* in both would forge a
  cross-group link. *Rezistencë* carries a WWII partisan resonance in Albanian, but so does de
  *Widerstand*, and English "opposition" has its own political sense — the polysemy is
  parallel, hence preserved rather than repaired (LAM).
- **LT2 "Persistence"** → *Këmbëngulja*, kept distinct from LT3's *Qëndrueshmëria*
  ("steadiness"), as the source keeps them.
- **LT3:** *Qëndrueshmëria dhe stabiliteti personal* — *qëndrueshmëri* is feminine and
  *stabilitet* masculine, so no adjective form agrees with both; strict coordination
  agreement (*personalë*) is grammatical but reads as a mistake. The singular *personal* is
  what would actually be written, and scopes over both by default. it and fr had it easier —
  both their nouns are feminine (*personali*, *personnelles*).
- **LT4:** *Planifikimi afatgjatë* shares *afatgjatë* with the LT dimension name, as the
  source shares "long-term".
- **LT6** "Working hard" → *Puna e palodhur* ("tireless work"), cf. de *Harte Arbeit*, pl
  *Ciężka praca*. Slightly amplified, but the alternatives are worse: *punë e rëndë* ("heavy
  work") drifts to manual labor — the trap ro flagged with *munci* — and *punë e vështirë*
  names the work's difficulty rather than the effort spent.
- **UNI on "success":** *sukses* renders every occurrence (CO4, LT5, LT6); "success in the
  future" is *për sukses në të ardhmen* in both LT5 and LT6.
- **MA group:** *burrat/gratë*, not *meshkujt/femrat* ("males/females"), which is clinical.
  *Burrë* and *grua* also mean "husband" and "wife", an ambiguity English "men/women" lacks,
  but that reading needs a possessive (*burri im*) and is not reachable here.
- **MA3** "active, forcible approach" → *një qasje aktive dhe energjike*, matching the corpus
  consensus on "forcible" (de *energisch*, it *energico*, fr *énergique*, nl *krachtdadig*,
  ro *energică*). *I vendosur* ("determined") was rejected on UNI grounds: it shares its stem
  with LT2's *me vendosmëri* ("resolutely"), which the source keeps distinct from "forcible".
- **MA4** "some jobs" → *disa punë*, the kinds-of-work reading the corpus has settled on
  (de *Tätigkeiten*, it *lavori*, pl *prace*; fr was explicitly corrected off *métiers* in
  commit a226e72). *Zanate*/*profesione* ("trades"/"professions") is the rejected reading;
  *veprimtari*/*aktivitete* is the natural calque of de *Tätigkeiten* but in Albanian denotes
  organized events (*veprimtari kulturore*), not kinds of work; *detyra* would collide with
  PO5. *Punë* does share a stem with UN4's *procedurat e punës* and LT6's *Puna* — English
  "work"/"working" links those two as well — and the MA context (MA1's career, MA3's
  problem-solving) fixes the reading.
- **Dimension names** are constructed from standard Albanian management vocabulary:
  *distanca e pushtetit*, *shmangia e pasigurisë*, *orientimi afatgjatë*. All five take the
  definite article, which is the Albanian convention for abstract nouns in headings —
  unlike ro, where the article tracks whether the noun is deverbal.
- **Scale anchors:** *nuk pajtohem aspak* / *pajtohem plotësisht*, structurally the same
  verb-based pair as de (*stimme überhaupt nicht zu* / *stimme voll und ganz zu*) and pl.
  *Pajtohem* was chosen over Albania-colloquial *jam dakord* (← It. *d'accordo*): the native
  verb is standard in both Albania and Kosovo, so anchors stay comparable across the
  respondent pool, and it is the more formal register a scientific instrument wants.
  For `important5`, *shumë e parëndësishme* is the symmetric literal anchor, following de
  (*sehr unwichtig*), nl (*zeer onbelangrijk*), and pl (*zupełnie nieważne*) rather than the
  Romance "very little important" route. The more frequent Albanian bottom anchor is *aspak e
  rëndësishme* ("not at all important"), rejected under CON: it is stronger than the source's
  "very unimportant" and would compress the bottom of the LT scale. This is the one choice in
  the file I would most want a native questionnaire designer to confirm. Both anchors use the
  feminine *e rëndësishme*, which is Albanian's default impersonal predicate form and so does
  not force agreement with the mixed-gender LT items being rated.
