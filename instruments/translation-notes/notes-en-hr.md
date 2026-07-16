# CVscale translation notes: English → Croatian

**Source language:** English · **Target language:** Croatian (hrvatski)

Files written to `instruments/`:
- `cvscale-hr.tsv` — 26 items across the five groups
- `dimensions-hr.csv` — dimension names, English kept after " / "
- `scales-hr.csv` — Likert anchors (`uopće se ne slažem`…`u potpunosti se slažem`;
  `vrlo nevažno`…`vrlo važno`)

## Target-language characterization

Croatian is a South Slavic language (Štokavian-based standard, Latin script, ijekavian
reflex: *neizvjesnost*, *izbjegavanje*, *uvijek*, *rješavanje*). It is mutually intelligible
with Serbian/Bosnian/Montenegrin but the written standard is well codified and stable, which
made most items straightforward. Four features shaped the choices:

- **Register / variety stability.** Unlike Czech, Croatian is not sharply diglossic; the
  standard written register is what questionnaires uniformly use and it is comfortably neutral
  across the regional dialects (kajkavian, čakavian) that respondents may speak natively.
  Everything here is standard written Croatian.
- **Derivational morphology — a UNI win Czech could not get.** Croatian keeps the source's
  *individuals* / *individual* link that Czech (and Polish) had to break. The noun is
  *pojedinac* → *pojedinci* ("individuals", CO1/CO2/CO5) and its adjective *pojedinačni*
  ("individual, single") genuinely means "individual (vs. collective/team)", so *pojedinačne
  nagrade* (CO3), *pojedinačni uspjeh* (CO4) and *pojedinačni ciljevi* (CO6) share the *pojedin-*
  stem with the noun, mirroring the source's one repeated word. No recourse to the loan
  *individualni* was needed.
- **Polysemy traps.** Two words needed care: *operacija* (UN5) is first a surgical/military
  operation, not a neutral "thing done" (as in Czech *operace*); and *silovit* ("forcible")
  shares the *sila*-root family with *silovati* ("to rape/force"), carrying a coercive/violent
  load the neutral English "forcible" lacks (MA3). Both were avoided — see notes below.
- **Gender marking.** Croatian forces gender on *l*-participles (past tense, conditional) and on
  predicate adjectives. The generic plurals *ljudi* (PO) and *pojedinci* (CO) are grammatically
  masculine and gender-neutral in reference, so their conditional *trebali bi* raises no issue.
  The only first-person item, UN1, would have forced the respondent's own gender to surface;
  it was restructured (below). Scale anchors use present-tense verbs (*slažem se*), which are
  gender-free.

Three decisions were worth flagging.

## 1. PO4 "should not disagree" — the stacked negation (CON, naturalness)

Variants: **A) "ne bi se trebali ne slagati s odlukama"** (should not disagree with the
decisions — literal) vs. **B) "ne bi se trebali protiviti odlukama"** (should not oppose) vs.
**C) "trebali bi se slagati s odlukama"** (should agree).

Croatian has no single positive verb for "disagree": *ne slagati se* is inherently *ne* +
*slagati se* ("to agree"). Rendering "should not disagree" literally therefore stacks two
negation particles — *ne bi ... ne slagati* — which reads a little heavy, the same objection
that drove Polish away from its literal option. But the two *ne* attach to different words
(*ne bi trebali* = "should not"; *ne slagati* = "disagree") and the construction is fully
grammatical, not a drafting error, so the naturalness cost is mild rather than disqualifying.

That matters because A is the only variant that preserves the source's *mildness*: English
"disagree" is merely holding a contrary view. *Protiviti se* (B) means actively oppose/resist,
and flipping to "should agree" (C) demands positive endorsement rather than mere non-dissent —
both overshoot the item's force. Chose **A**: with the negation grammatical, CON is decisive
and the literal rendering wins.

## 2. UN1 — first-person gender marking (gender-neutrality rule)

"…so that I always know what I'm expected to do." The natural purpose clause is *kako bih uvijek
znao* (masc.) / *znala* (fem.) — the conditional *l*-participle is unavoidably gendered, and the
questionnaire fallback *znao/znala* would spotlight the respondent's gender in an item that has
nothing to do with it (awkward in an instrument whose MA group *does* measure gender attitudes).
I restructured to a result clause with a present-tense verb: **"…tako da uvijek znam što se od
mene očekuje"** ("…so that I always know what is expected of me"). *Znam* carries no gender. The
shift from purpose ("so that") to result ("so that/thereby") is negligible — detailed
instructions *produce* the knowledge. The clause *"što se od mene očekuje"* is reused verbatim in
UN3, mirroring the source's repetition of "what is expected of me" across UN1 and UN3 (UNI).

## 3. UN5 "Instructions for operations" and MA3 "forcible" — two polysemy avoidances (AMB, SEM, CON)

**UN5.** *Operacija* in Croatian is first a **surgical** operation, secondarily military; the
neutral English "operations" (things done at work) is not a salient reading. *Upute za operacije*
would mislead. I used **"Upute za rad"** ("instructions for work/operation"), where *rad*
neutrally covers work and the running/operating of things, keeping the source's terseness.
*Upute* ("instructions") is reused across UN1, UN2 and UN5, matching the source's repeated
"instructions" (UNI).

**MA3.** "active, forcible approach" needs two distinct adjectives. *Aktivan* = "active".
For "forcible" the direct cognate *silovit* was rejected: it shares the *sila*-root with
*silovati* ("to force/rape") and reads as coercive/violent, a colouring the neutral English
lacks (the same trap Czech saw in *silový*). *Energičan* would be a near-synonym of *aktivan*,
making the pair redundant. Croatian *razantan* ("forceful, vigorous, hard-hitting") carries the
assertive-force nuance while staying a genuinely distinct second adjective and non-violent (CON)
— the same landing point as the Czech *razantní*. Chosen: **"aktivan, razantan pristup"**.

## Structural / uniformity notes

- **"people in higher/lower positions"** → *ljudi na višim/nižim položajima*, identical across
  all five PO items. *Položaj* ("position, rank") was preferred to the loan *pozicija*; the
  false-friend risk that bit Czech (*stanovisko* ≠ job) does not arise. *Nadređeni/podređeni*
  ("superiors/subordinates") was rejected as too narrow — it presumes a direct reporting line the
  source does not.
- **PO3 "social interaction"** → *druženje* ("socializing"). *Društveni kontakt* is fine but
  wordier; sociological *društvena interakcija* is jargon and would wrongly include work
  interaction (SEM).
- **CO "group"** → *skupina* throughout (native), not the colloquial loan *grupa*.
- **CO1 "for the group" vs. CO3/CO5 "welfare of the group".** CO1 is *žrtvovati … za skupinu*
  ("for the group"), deliberately *not* echoing *dobrobit* ("welfare"), so it does not forge a
  CO1–CO3/CO5 link the source keeps separate. "Welfare of the group" is *dobrobit skupine*,
  identical in CO3 and CO5 (UNI); *dobrobit* ("wellbeing") was preferred to *blagostanje*, which
  narrows toward material prosperity.
- **CO2 "stick with the group"** → *ostati uz skupinu* ("stay by the group"), kept lexically
  clear of the *odanost* ("loyalty") field belonging to CO6, so the two items stay distinct as in
  the source.
- **"goals"** → *ciljevi* in CO5 and CO6 (UNI). **"success"** → *uspjeh* in CO4, LT5, LT6 (UNI).
- **PO5 "tasks" vs. MA4 "jobs"** stay distinct: *zadaci* vs. *poslovi*.
- **LT glosses** are the established Croatian Hofstede terms, lowercased per Croatian orthography:
  "Thrift" → *štedljivost*; "Persistence" → *ustrajnost*. In LT2 the descriptor was phrased
  *odlučno nastavljanje* ("resolute continuing") rather than *ustrajanje*, so the descriptor does
  not share a stem with its own gloss *ustrajnost* (as the source's "going on" ≠ "persistence").
  LT3 "steadiness" → *postojanost* (constancy), kept clear of *ustrajnost* so the LT2/LT3
  distinction survives. "success in the future" → *za uspjeh u budućnosti*, identical in LT5 and
  LT6 (UNI).
- **MA4 "can always do better"** → *uvijek može … obaviti bolje*. Here *može* reads as ability,
  not permission (the *bolje obaviti* collocation blocks the permission reading), so no perfective
  workaround was needed. *Poslovi* ("jobs") is distinct from PO5's *zadaci* ("tasks").
- **UN3 agreement:** coordinated neuter (*pravila*) + masculine-inanimate (*propisi*) subjects
  with no masculine animate → predicate takes masculine plural *važni* (not neuter *važna*) —
  the same rule the Czech note flagged for *pravidla a předpisy*.
- **Dimension names** use established Croatian Hofstede terminology: *distanca moći*, *izbjegavanje
  neizvjesnosti*, *kolektivizam*, *dugoročna orijentacija*, *maskulinitet*.
- **Scale anchors:** *uopće se ne slažem* / *u potpunosti se slažem* is the standard Croatian
  5-point agreement pair (present-tense, gender-free). For importance I kept the source's
  symmetric "very…very" as *vrlo nevažno* / *vrlo važno*, which is faithful and acceptable;
  Croatian survey practice also uses *uopće nije važno* or *posve/potpuno nevažno* at the low pole,
  so a native reviewer may wish to confirm the importance anchors against local convention.

## Confidence

No capability caveat applies: Croatian is well resourced and every source item has a natural,
register-stable equivalent. The genuine difficulties were the three flagged above (the PO4
stacked negation, the forced UN1 gender marking, and the *operacija*/*silovit* polysemy
avoidances), all with defensible resolutions rather than compromises. The most satisfying result
is a UNI win Czech and Polish could not achieve: Croatian's *pojedinac* / *pojedinačni* preserves
the source's *individuals* / *individual* stem link across the whole CO group.
