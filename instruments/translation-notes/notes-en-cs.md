# CVscale translation notes: English → Czech

**Source language:** English · **Target language:** Czech (čeština)

Files written to `instruments/`:
- `cvscale-cs.tsv` — 26 items across the five groups
- `dimensions-cs.csv` — dimension names, English kept after " / "
- `scales-cs.csv` — conventional Likert anchors (`rozhodně nesouhlasím`…`rozhodně souhlasím`;
  `zcela nedůležité`…`velmi důležité`)

## Target-language characterization

Czech is a West Slavic language, close to Polish, and several of the Polish translation's
problems recur here — but with Czech-specific twists, and two of them resolve the opposite way.
Four features drove the item-level choices:

- **Register split (the big one).** Czech is genuinely diglossic: *spisovná čeština* (standard
  written Czech) versus *obecná čeština* (Common Czech, the everyday spoken variety of Bohemia
  and of Prague media). This is a sharper split than anything Polish has. Crucially, obecná
  čeština is *regionally* skewed — Moravian and Silesian speakers do not use its markers
  (*-ej* for *-ý*, prothetic *vo-*, unified instrumental *-ma*), and to many of them it reads
  as "Prague speech" rather than as neutral informality. Any obecná form would therefore make
  the instrument land differently on Bohemian and Moravian respondents, which is exactly the
  comparability risk the rules warn about. Everything here is standard written Czech, the
  register Czech questionnaires uniformly inhabit; it is also the only variety that is
  regionally neutral.
- **A false friend where Polish had its anchor word.** Polish rendered "people in higher/lower
  positions" with *stanowisko* (job post). The Czech cognate *stanovisko* exists but means
  **only** "standpoint, position on an issue" — never a job. Czech had to go elsewhere; see
  the PO note below.
- **Derivational morphology and one unbreakable stem link.** Shared stems make UNI cheap
  (*skupina* → *skupiny*/*skupině*; *cíl* → *cíle*). The one link Czech cannot reproduce is the
  source's *individuals* / *individual*, and it fails for exactly the Polish reason: the
  sociological noun is *jednotlivec*, but its adjective *jednotlivý* means "single, separate,
  each one", not "pertaining to the individual". The other candidate noun *jedinec* is worse —
  its adjective *jedinečný* means "unique". The adjective must be *individuální*, a different
  stem. Semantics beat morphology; the broken link is accepted (as in Polish).
- **Gender marking.** Czech forces gender on first-person past-tense and conditional verbs and
  on predicate adjectives. Only UN1 is first-person and it needed restructuring (below).
  Elsewhere *lidé* ("people", plural of the referentially neutral *člověk*) and *jednotlivci*
  keep gender invisible, and the scale anchors use present-tense verbs (*souhlasím*), which are
  gender-free.

Three decisions were worth flagging.

## 1. PO4 "should not disagree with decisions" — where Czech and Polish part company (CON)

Variants: **A) "by neměli nesouhlasit s rozhodnutími"** (should not disagree with the
decisions — literal) vs. **B) "by neměli zpochybňovat rozhodnutí"** (should not
question/cast doubt on) vs. **C) "by neměli odporovat rozhodnutím"** (should not
contradict/resist).

The Polish translation rejected its literal option because *nie powinny nie zgadzać się*
stacks two free-standing *nie* particles and reads as a drafting error. Czech does not have
that problem: the negation is carried by a **bound prefix** on each of two different words
(*ne*-měli *ne*-souhlasit), which is ordinary, unremarkable Czech — cf. the everyday *neměl bys
nezaplatit*. The clumsiness argument that decided Polish simply does not transfer.

That matters, because A is the only variant that preserves the source's mildness. English
"disagree" covers merely holding a contrary view; *zpochybňovat* (B) implies voicing doubt
about a decision's validity, and *odporovat* (C) implies active resistance — both overshoot.
Chose **A**: with the naturalness objection gone, CON is decisive and the literal rendering
wins. This is a deliberate divergence from the Polish version's *kwestionować*, driven by a
real grammatical difference between the two languages rather than by taste.

## 2. UN1 — first-person gender marking (gender-neutrality rule)

"…so that I always know what I'm expected to do." The obvious purpose clause takes *abych* +
an *l*-participle, which is unavoidably gendered: **A) "abych vždy věděl"** (masculine) /
*"abych vždy věděla"* (feminine). Czech has no neutral form, and the questionnaire fallback
*"věděl/a"* marks the respondent's gender as salient in an item that has nothing to do with
gender — awkward in an instrument whose MA group *does* measure gender attitudes.

I restructured instead: **B) "…díky čemuž vždy vím, co se ode mě očekává"** ("…thanks to which
I always know what is expected of me"). Present-tense *vím* carries no gender. The cost is a
shift from purpose ("so that") to result ("thanks to which"), which is negligible — the item's
force is that detailed instructions *produce* the knowledge. Chose **B**; gender-neutrality is
an explicit rule and the semantic cost is far smaller than the alternative's. The same clause
*"co se ode mě očekává"* is reused verbatim in UN3, mirroring the source's own repetition of
"what is expected of me" across UN1 and UN3 (UNI).

## 3. UN5 "Instructions for operations" — the *operace* trap (AMB, SEM)

Czech inherits Polish's polysemy problem intact: **B) "Pokyny pro operace"** fails because
*operace* denotes first and foremost a **surgical** operation, secondarily a military one; the
neutral English "a thing done" is not a salient Czech reading. **C) "Návod k obsluze"** is the
fixed term for a *product user manual*, relocating the item out of the workplace (the same trap
Polish's *instrukcja obsługi* posed). **D) "Provozní pokyny"** ("operating instructions") is
idiomatic and was the closest call — but *provoz* means the running of a plant or facility, so
it quietly narrows the item to industrial settings and would read oddly to an office
respondent (SEM).

Chose **A) "Pokyny pro pracovní činnosti jsou důležité."** ("instructions for work activities"),
where *činnosti* is the neutral Czech word for work operations — the same landing point as the
Polish *czynności*. It keeps the source's terseness. *Pokyny* is used across UN1, UN2 and UN5
to preserve the source's within-group repetition of "instructions" (UNI).

## Structural / uniformity notes

- **"people in higher/lower positions"** → *lidé na vyšších/nižších pozicích*, identical in all
  five PO items. With *stanovisko* excluded as a false friend (above), the candidates were
  *pozice*, *funkce* (office) and *pracovní místo* (job slot). *Pozice* is well established in
  Czech workplace usage and, though polysemous in isolation (spatial, chess), is disambiguated
  completely by the collocation *na vyšších pozicích*, so AMB does not bite. *Funkce* skews
  toward formal office-holding; *pracovní místo* is a headcount slot, not a rank. *Lidé*
  (matching "people") was preferred to *osoby*, which reads bureaucratic/legal. *Nadřízení* /
  *podřízení* ("superiors"/"subordinates") was rejected as too narrow: it presumes a direct
  reporting line the source does not.
- **PO3 "social interaction"** → *společenským kontaktům* (socializing). *Společenský styk* is a
  fixed neutral phrase but *styk* alone carries a sexual sense (*pohlavní styk*) the English
  lacks — needless AMB risk. *Sociální interakce* is sociology jargon and would wrongly include
  work interaction (SEM).
- **CO2 vs. CO6:** CO2 "stick with the group" → *držet se skupiny* (cohesion), kept lexically
  clear of the *loajalita* field belonging to CO6, so the two items stay distinct as they do in
  the source.
- **"welfare of the group"** → *dobro skupiny*, identical in CO3 and CO5 (UNI); *blahobyt* was
  rejected as narrowing to material prosperity. CO1 "sacrifice self-interest **for the group**"
  is *ve prospěch skupiny* — *ve prospěch* is a fixed "in favour of" preposition-phrase and does
  not lexically echo *dobro*, so it avoids forging a CO1–CO3/CO5 link the source does not make.
- **CO4 "individual success"** → *individuální úspěch*, not *úspěch jednotlivce*. The latter is
  tempting because *jednotlivec* would restore the *individuals*/*individual* stem link the
  source has and Czech otherwise loses — but it would break the uniformity of the adjective
  across CO3/CO4/CO6, where the source uses one word ("individual") three times. Explicit UNI
  on the adjective outranks an opportunistic partial repair of a link already conceded.
- **"tasks" (PO5) vs. "jobs" (MA4)** are distinct in the source and stay distinct: *úkoly* and
  *práce*. *Činnosti* was unavailable for MA4 — it is UN5's word, and reusing it would forge a
  cross-group link. MA4's "can always do better" → *vždy zvládne lépe* (perfective future),
  since *může* would read as permission — the same reasoning the Polish (*wykona*), French and
  Russian versions applied.
- **"success in the future"** → *pro budoucí úspěch*, identical in LT5 and LT6 (UNI); *úspěch*
  is also the CO4 word, as in the source.
- **LT glosses:** "Thrift" → *šetrnost* (the positively-valenced Czech Hofstede term, matching
  German *Sparsamkeit* / Polish *oszczędność*); "Persistence" → *vytrvalost*, the standard Czech
  Hofstede term. LT3 "steadiness" is *stálost* (constancy), kept clear of *vytrvalost* so the
  source's separation of LT2 and LT3 survives. Glosses are lowercased per Czech orthography (as
  in the Polish and Russian versions).
- **MA3 "active, forcible"** → *aktivní, razantní*. *Silový* ("by force") is far too strong and
  carries a coercive, negative colouring the neutral English lacks (the same objection Polish
  raised to *siłowy*); *energický* is a near-synonym of *aktivní* and would make the pair
  redundant. *Razantní* ("vigorous, forceful") carries the assertive-force nuance while staying
  a genuinely distinct second adjective (CON). *Důrazný* was the runner-up but skews toward
  emphasis in *communication* rather than force in action.
- **UN3 agreement note:** *Pravidla a předpisy jsou důležité* — with coordinated neuter
  (*pravidla*) and masculine-inanimate (*předpisy*) subjects and no masculine animate, the
  predicate takes the masculine-inanimate plural *-é*, not the neuter *-á*.
- **Dimension names** use the established Czech Hofstede terminology: *vzdálenost moci*,
  *vyhýbání se nejistotě*, *kolektivismus*, *dlouhodobá orientace*, *maskulinita*.
- **Scale anchors:** *rozhodně nesouhlasím* / *rozhodně souhlasím* is the standard Czech 5-point
  agreement pair, and its present-tense verbs are gender-free. For importance I departed from a
  literal "very unimportant": the conventional Czech importance battery (as used by CVVM and
  Czech survey practice generally) runs *velmi důležité — spíše důležité — spíše nedůležité —
  zcela nedůležité*, so the conventional low anchor is **zcela nedůležité** ("completely
  unimportant"), not *velmi nedůležité*, which sounds wrong to a Czech ear for the same reason
  Polish *bardzo nieważne* does. The skill's instruction to prefer conventional scientific
  anchors decided this over literal symmetry with the source — the same call the Polish
  (*zupełnie nieważne*) and Russian (*совсем неважно*) versions made.

## Confidence

No capability caveat applies: Czech is a well-resourced language and every source item has a
natural, register-stable Czech equivalent. The genuine difficulties were the three flagged
above (a forced gender marking, the *operace* polysemy trap, and the PO4 connotation call),
all of which have defensible resolutions rather than compromises. The most interesting finding
is that Czech's proximity to Polish is partly a trap: *stanovisko* is a false friend of
*stanowisko*, and PO4's stacked negation — decisive against the literal rendering in Polish —
is unproblematic in Czech, so the two translations correctly diverge there.
