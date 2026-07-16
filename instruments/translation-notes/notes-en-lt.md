# CVscale translation notes: English → Lithuanian

**Source language:** English · **Target language:** Lithuanian (lietuvių kalba)

Files written to `instruments/`:
- `cvscale-lt.tsv` — 26 items across the five groups
- `dimensions-lt.csv` — dimension names, English kept after " / "
- `scales-lt.csv` — Likert anchors (`visiškai nesutinku`…`visiškai sutinku`;
  `labai nesvarbu`…`labai svarbu`)

## Target-language characterization

Lithuanian is an archaic, heavily inflected Baltic (Indo-European) language with seven cases,
grammatical gender (masculine/feminine) on nouns, adjectives and participles, and no articles.
Four properties drove the item-level choices.

- **Rich case morphology is an asset here, not a hazard.** Where English repeats the
  preposition "with", Lithuanian can use the bare instrumental case, so the exact clause
  parallelism of MA2 ("with logical analysis" / "with intuition") reproduces cleanly as
  *logine analize* / *intuicija* with no added function words. Negated verbs take the genitive
  of negation (*neturėtų pavesti svarbių užduočių*), which is automatic and unremarkable.
- **Register / variety is stable.** Standard written Lithuanian is regionally neutral and is
  the register questionnaires uniformly inhabit; the Aukštaitian/Žemaitian dialect split does
  not surface in the written standard. There is no diglossia comparable to Czech, and no
  T/V problem arises because the only first-person items (UN1, UN3) use the impersonal
  *tikimasi* / *praneša* constructions.
- **Gender is forced by grammar but stays invisible where it must.** Predicate adjectives and
  participles inflect for gender, but the two first-person items resolve without any marking:
  the 1sg conditional *žinočiau* ("I would know", UN1) is gender-free, and *ko iš manęs
  tikimasi* ("what is expected of me", UN3) is impersonal. Generic actors are *žmonės*
  ("people", PO) and *individai* ("individuals", CO), whose default plural is the unmarked
  masculine used generically. Only the MA group names the sexes, exactly as the source intends.
- **Derivational morphology makes UNI cheap.** Shared stems reproduce the source's within-group
  repetitions directly: *nurodymai* across UN1/UN2/UN5, *procedūros* across UN2/UN4, *grupės
  gerovė* across CO3/CO5, *individ-* across CO1/CO2/CO3/CO4/CO6, *sėkmė* across CO4/LT5/LT6, and
  the identical *dėl sėkmės ateityje* ("for success in the future") in LT5 and LT6.

## 1. MA3 "active, forcible approach" — the LT2 collision (UNI, CON)

"Solving difficult problems usually requires an active, forcible approach, which is typical of
men." The natural Lithuanian word for "forcible/forceful/resolute" is *ryžtingas* — but that is
already LT2's word for "resolutely" (*Ryžtingas ėjimas pirmyn*), and the source uses two
*different* words in the two items. Reusing *ryžtingas* would forge a cross-group link the
source does not have (the same trap Finnish found with *päättäväinen* and Czech/Romanian with
their determination words). Candidates for the second adjective:

- **A) *jėgingo*** — forceful, drawing directly on *jėga* "force"; the force nuance of
  "forcible", and clearly distinct from *aktyvus* "active".
- **B) *ryžtingo*** — resolute/determined; the most idiomatic single rendering, but blocked by
  UNI (= LT2).
- **C) *energingo*** — energetic/vigorous; rejected as a near-synonym of *aktyvus*, which would
  make the pair redundant (the *energický* objection from the Czech version).
- **D) *veržlaus*** — dynamic/driving/go-getting; natural, but overlaps semantically with
  "active" and softens the force nuance.

Chose **A**, *jėgingo*. The decisive argument was UNI applied negatively — the source's LT2/MA3
lexical contrast must survive — combined with CON: *jėgingas* keeps the "force" of "forcible"
without overshooting into coercion or drifting into mere energy. Rendered *aktyvaus, jėgingo
požiūrio, kuris būdingas vyrams*.

## 2. The `important5` low anchor: symmetry vs. the "conventional" extreme (CON)

Lithuanian's high importance anchor is fixed: *labai svarbu* ("very important") is idiomatic,
whereas *visiškai svarbu* ("completely important") is not something a Lithuanian says. That
constrains the low anchor. Variants:

- **A) *labai nesvarbu*** — "very unimportant"; symmetric with *labai svarbu*, idiomatic
  (*man tai labai nesvarbu* is ordinary speech), and an exact strength-match for the source's
  "very unimportant".
- **B) *visiškai nesvarbu*** — "completely unimportant"; the extreme most Lithuanian importance
  batteries use, and the choice the Slavic corpus made (Polish *zupełnie nieważne*, Russian
  *совсем неважно*, Czech *zcela nedůležité*). But it is *stronger* than the source's "very",
  and pairing it with the fixed *labai svarbu* yields an asymmetric scale
  ("completely…" ↔ "very…").

Chose **A**. With the high anchor pinned at *labai svarbu*, only *labai nesvarbu* gives the
clean bipolar, equal-strength pair the source has (CON). The agreement scale independently uses
the standard Lithuanian extreme *visiškai nesutinku / visiškai sutinku*, whose present-tense
verbs are gender-free — the two scales follow their own idioms, which is why "visiškai" appears
in one and "labai" in the other.

## 3. CO3/CO4 "individual rewards / individual success" — genitive over adjective (AMB, UNI)

The source's adjective "individual" could be rendered by the adjective *individualus*, but in
Lithuanian *individualus* leans toward "individualized, personalized" — an ambiguity the source
lacks (AMB), the same trap Czech noted with *individuální*. The genitive noun *individo* ("of
the individual") says exactly what English means (a reward/ success accruing to the individual),
avoids the AMB, and additionally reproduces the source's own *individuals*/*individual* stem
recurrence, since it shares the stem of *individai* (CO1/CO2). It also mirrors the parallel
precisely: *Grupės gerovė … individo atlygį*, *Grupės sėkmė … individo sėkmę*, *individo tikslai*
(CO6). Chose the genitive throughout; UNI and AMB agree against the adjective.

## Structural / uniformity notes

- **"people in higher/lower positions"** → *aukštesnes/žemesnes pareigas užimantys žmonės*
  ("people holding higher/lower positions"), identical in all five PO items. *Pareigos* (post /
  office / duties) is the natural Lithuanian hierarchy word; *pozicija* (loan) is unidiomatic for
  rank, and *viršininkai/pavaldiniai* (superiors/subordinates) was rejected as too narrow — it
  presumes a direct reporting line the generic source does not.
- **PO1 vs. PO2:** the source uses two distinct verbs, "consulting" and "ask the opinions".
  Preserved as *nesitardami su* (tartis su = to confer/consult, PO's semantic field) vs.
  *klausti … nuomonės* (ask the opinion) — UNI applied negatively.
- **PO4 double negation:** *neturėtų nesutikti su … sprendimais* ("should not disagree with the
  decisions"). Lithuanian carries each negation as a bound prefix (*ne*-turėtų *ne*-sutikti),
  which is ordinary and unremarkable — none of the awkwardness that pushed Polish off its literal
  rendering. *Nesutikti* keeps the item at the mildness of English "disagree" (matching the scale
  anchor *nesutinku*); *prieštarauti* (oppose) would overshoot (CON).
- **"People" vs. "Individuals":** *žmonės* (PO) vs. *individai* (CO), preserving the source's
  lexical opposition.
- **CO1 "self-interest"** → *savo interesus* ("one's own interests"), kept lexically clear of
  LT3's *asmeninis* ("Personal"), which the source likewise keeps distinct from "self-interest".
- **CO2 vs. CO6:** CO2 "stick with the group" → *likti su grupe* (cohesion, no loyalty word), so
  CO6's *grupinis lojalumas* stays the group's only loyalty item — the separation the source has.
- **"welfare of the group"** → *grupės gerovė*, identical in CO3 and CO5 (UNI).
- **UN1 vs. UN3:** the source distinguishes "what I'm expected **to do**" (UN1) from "what is
  expected of me" (UN3); Lithuanian reproduces the distinction at no cost — *ką turiu daryti*
  vs. *ko iš manęs tikimasi*.
- **UN5 "Instructions for operations"** → *Veiklos nurodymai* ("instructions for activity").
  *Operacijos* was rejected: its salient Lithuanian senses are surgical and military (AMB, the
  same trap as Czech/Polish *operace/operacja*). *Veikla* is the neutral, deliberately vague word,
  and keeps the *nurodymai* stem shared with UN1/UN2.
- **LT glosses** (lowercased per Lithuanian orthography): "Thrift" → *taupumas* (the positive
  virtue term; *šykštumas* "stinginess" rejected on CON); "Persistence" → *atkaklumas*, kept
  distinct from LT3 "steadiness" → *pastovumas*. "Opposition" (LT2) → *pasipriešinimo*
  (resistance); the source's faint political-"Opposition" polysemy is not reproducible, since
  Lithuanian uses a separate word *opozicija* for that sense (LAM cost accepted — no option
  carries it, and *pasipriešinimas* is unambiguously the intended reading).
- **LT form:** the source mixes noun phrases (LT1, LT3, LT4) with gerund phrases (LT2, LT5, LT6);
  Lithuanian nominalizes both (*tvarkymas*, *ėjimas*, *atsisakymas*, *darbas*), which is what
  Lithuanian does with such headings.
- **MA1 "professional career"** → *profesinė karjera*, avoiding any *darbo* ("work") wording that
  would drag the *darb-* stem in where the source says "professional". *Profesinis* collocates
  with vocational education (*profesinis mokymas*), a mild AMB, but *profesinė karjera* is a fixed
  collocation that fixes the intended reading.
- **MA4 "some jobs"** → *darbų* ("kinds of work"). This shares the *darb-* stem with LT6's
  *sunkus darbas* ("hard work"), but the link is inert: LT and MA are different, non-competing
  dimensions, and *darbas* is Lithuanian's basic, unavoidable word for work — a Lithuanian no
  more hears an echo here than an English speaker does between "Working hard" and "jobs". The
  competing candidates were worse: *užduočių* is PO5's word (tasks) and *veiklos* is UN5's, so
  either would forge a link with a normative item. "Can always do better" → *visada gali atlikti
  geriau*; *gali* reads unambiguously as ability, not permission, so no perfective-future repair
  (Czech *zvládne*, Polish *wykona*) is needed.
- **Dimension names** use established Lithuanian Hofstede terminology: *galios distancija*,
  *neapibrėžtumo vengimas*, *kolektyvizmas*, *ilgalaikė orientacija* (consistent with LT4's
  *ilgalaikis planavimas*), *maskulinizmas*.

## Confidence

Lithuanian is mid-resource for me. I am confident in the case government, the participle
agreement, and the gender-neutral resolutions, and the dimension terminology is standard. My
one genuine caveat is fine collocational naturalness in two places: MA3's *jėgingo požiūrio*
(the "forcible approach" adjective, chosen under a hard UNI constraint that rules out the most
idiomatic word) and the nominalized LT phrasings (*ėjimas pirmyn*, *malonumų atsisakymas*) — a
native review would pay off most there. Everything else has a natural, register-stable
equivalent.
