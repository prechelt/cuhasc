# CVscale translation notes: English → Slovenian

**Source language:** English · **Target language:** Slovenian (slovenščina)

Files written to `instruments/`:
- `cvscale-sl.tsv` — 26 items across the five groups
- `dimensions-sl.csv` — dimension names, English kept after " / "
- `scales-sl.csv` — Likert anchors (`sploh se ne strinjam`…`popolnoma se strinjam`;
  `zelo nepomembno`…`zelo pomembno`)

## Target-language characterization

Slovenian is a South Slavic language (Latin script), close to but distinct from Croatian.
Its written standard is well codified, and questionnaires use a stable neutral standard register
that reads the same across the country's very numerous dialects, so register/variety stability was
never a problem. Four features shaped the item-level choices:

- **Register / variety stability.** Everything here is standard written Slovenian, the register all
  survey instruments use; it is neutral across the dialect continuum respondents natively speak.
- **Derivational morphology — a UNI win.** The source repeats *individual(s)* right across the CO
  group. Slovenian keeps that link with a single stem: the noun *posameznik* ("individual") as
  subject in CO1/CO2/CO5, and its genitive *posameznika/posameznikov* ("of the individual(s)") in
  CO3/CO4/CO6 — one word throughout, no recourse to the loan *individualen*. Using the genitive
  noun rather than the native adjective *posamezen/posamični* was deliberate (see decision 2).
- **Polysemy traps.** Two words needed care: *operacija* (UN5) reads first as a surgical/military
  operation, not a neutral "thing done at work"; and *silovit* (the direct cognate for "forcible",
  MA3) shares the *sila*-root family with force/violence and reads as vehement/violent, a colouring
  the neutral English lacks. Both were avoided.
- **Gender marking.** Slovenian forces gender on *l*-participles (past/conditional) and predicate
  adjectives. The generic plurals *ljudje* (PO) and *posamezniki* (CO) are grammatically masculine
  but gender-neutral in reference, so their conditional *bi morali* raises no issue. The only
  first-person item, UN1, uses the present-tense *vem* ("I know"), which is gender-free, so no
  gender surfaced there. CO6 was cast impersonally (*bi bilo treba*), also gender-free. Scale
  anchors use present-tense verbs (*strinjam se*), likewise gender-free.

Three decisions were worth flagging.

## 1. PO4 "should not disagree" — the stacked negation (CON, naturalness)

Variants: **A) "se ne bi smeli ne strinjati z odločitvami"** (should not disagree with the
decisions — literal) vs. **B) "ne bi smeli nasprotovati odločitvam"** (should not oppose) vs.
**C) "bi se morali strinjati z odločitvami"** (should agree).

Slovenian has no single positive verb for "disagree": *ne strinjati se* is inherently *ne* +
*strinjati se* ("to agree"). Rendering "should not disagree" literally therefore stacks two
negation particles — *ne bi smeli ne strinjati* — which reads a little heavy. But the two *ne*
attach to different words (*ne bi smeli* = "should not"; *ne strinjati* = "disagree") and the
construction is fully grammatical, so the naturalness cost is mild rather than disqualifying.

That matters because A is the only variant that preserves the source's *mildness*: English
"disagree" is merely holding a contrary view. *Nasprotovati* (B) means actively oppose/resist,
and flipping to "should agree" (C) demands positive endorsement rather than mere non-dissent —
both overshoot the item's force. Chose **A**: with the negation grammatical, CON is decisive.

## 2. CO group "individual(s)" — noun vs. adjective (UNI, AMB)

The source hammers one word across the whole CO group: *individuals* (CO1/CO2/CO5), *individual
rewards* (CO3), *individual success* (CO4), *individual goals* (CO6). Two ways to honour UNI in
Slovenian: **A)** the noun *posameznik* everywhere (subject in CO1/CO2/CO5, genitive "of the
individual(s)" in CO3/CO4/CO6) vs. **B)** the noun as subject but the native adjective
*posamezen/posamični* for the "individual X" phrases.

B was rejected on AMB grounds: *posamezen/posamični* primarily means "single, isolated, sporadic",
so *posamične nagrade* would drift toward "isolated/occasional rewards" — an ambiguity the source's
"individual (vs. group)" does not carry. A keeps the exact "of the individual vs. of the group"
contrast the items are built on (*nagrade posameznikov* vs. *dobrobit skupine*; *uspeh posameznika*
vs. *uspeh skupine*), is unambiguous, and preserves one stem *posamezn-* right across the group —
the strongest possible UNI. Chose **A**.

## 3. UN5 "operations" and MA3 "forcible" — two polysemy avoidances (AMB, SEM, CON)

**UN5 "Instructions for operations".** *Operacija* in Slovenian is first a **surgical** operation,
secondarily military; the neutral English "operations" (things done at work) is not a salient
reading, so *navodila za operacije* would mislead. I used **"Navodila za delo"** ("instructions for
work/operation"), where *delo* neutrally covers work and the doing of tasks, keeping the source's
terseness. *Navodila* ("instructions") is reused across UN1, UN2 and UN5, matching the source's
repeated "instructions" (UNI).

**MA3 "active, forcible approach".** Two distinct adjectives are needed. *Aktiven* = "active". For
"forcible" the direct cognate *silovit* was rejected: it belongs to the *sila*-root family and
reads as vehement/violent, a coercive colouring the neutral English lacks (CON). *Energičen*
("energetic") would be a near-synonym of *aktiven*, making the pair redundant. Slovenian *prodoren*
("assertive, incisive, go-getting, pushing through") carries the forceful nuance while staying a
genuinely distinct second adjective and non-violent (CON). Chosen: **"aktiven, prodoren pristop"**.
*Reševanje težkih problemov* also shares the *reš-* stem with *rešujejo probleme* in MA2, mirroring
the source's "solve"/"solving" repetition (UNI).

## Structural / uniformity notes

- **"people in higher/lower positions"** → *ljudje na višjih/nižjih položajih*, identical across all
  five PO items. *Položaj* ("position, rank") was preferred to the loan *pozicija*; *nadrejeni/
  podrejeni* ("superiors/subordinates") was rejected as too narrow — it presumes a direct reporting
  line the source does not.
- **"should" vs. "should not".** Positive obligation is *bi morali* (PO1, PO3, CO1, CO2, CO5);
  prohibition is *ne bi smeli* ("ought not", PO2, PO4, PO5), the natural Slovenian negative. CO6's
  "should be encouraged" is the impersonal *bi bilo treba spodbujati*, which also stays gender-free.
- **PO3 "social interaction"** → *druženje* ("socializing"). Sociological *družbena interakcija* is
  jargon and would wrongly include work interaction (SEM).
- **CO "group"** → *skupina* throughout (native), not the colloquial loan *grupa*.
- **CO1 "for the group" vs. CO3/CO5 "welfare of the group".** CO1 is *žrtvovati … za skupino* ("for
  the group"), deliberately *not* echoing *dobrobit* ("welfare"), so it does not forge a CO1–CO3/CO5
  link the source keeps separate. "Welfare of the group" is *dobrobit skupine*, identical in CO3 and
  CO5 (UNI); *dobrobit* ("wellbeing") was preferred to *blaginja*, which narrows toward material
  prosperity.
- **CO2 "stick with the group"** → *ostati ob skupini* ("stay by the group"), kept lexically clear of
  the *zvestoba* ("loyalty") field belonging to CO6, so the two items stay distinct as in the source.
- **"goals"** → *cilji* in CO5 and CO6 (UNI). **"success"** → *uspeh* in CO4, LT5, LT6 (UNI);
  "success in the future" → *uspeh v prihodnosti*, identical in LT5 and LT6.
- **PO5 "tasks" vs. MA4 "jobs"** stay distinct: *naloge* vs. *dela*.
- **UN "instructions/procedures".** *Navodila* ("instructions") across UN1/UN2/UN5; *postopki*
  ("procedures") across UN2/UN4 — mirroring the source's repeated words (UNI).
- **LT glosses** are the established Slovenian Hofstede terms: "Thrift" → *varčnost*; "Persistence" →
  *vztrajnost*. In LT2 the descriptor was phrased *odločno nadaljevanje* ("resolute continuing")
  rather than *vztrajanje*, so the descriptor does not share a stem with its own gloss *vztrajnost*
  (as the source's "going on" ≠ "persistence"). LT3 "steadiness" → *stanovitnost* (constancy), kept
  clear of *vztrajnost* so the LT2/LT3 distinction survives.
- **MA4 "can always do better"** → *vedno … opravi bolje*. The perfective present *opravi* reads as
  ability, not permission, so no workaround was needed.
- **UN3 agreement:** coordinated neuter (*pravila*) + masculine-inanimate (*predpisi*) subjects take
  the masculine plural predicate *pomembni*.
- **Dimension names** use established Slovenian Hofstede terminology: *distanca moči*, *izogibanje
  negotovosti*, *kolektivizem*, *dolgoročna usmerjenost*, *maskulinost*.
- **Scale anchors:** *sploh se ne strinjam* / *popolnoma se strinjam* is the standard Slovenian
  5-point agreement pair (present-tense, gender-free). For importance the source's symmetric
  "very…very" maps cleanly to *zelo nepomembno* / *zelo pomembno*.

## Confidence

No capability caveat applies: Slovenian is well resourced and every source item has a natural,
register-stable equivalent. The genuine difficulties were the three flagged above (the PO4 stacked
negation, the CO *posameznik* noun-vs-adjective choice, and the *operacija*/*silovit* polysemy
avoidances), all with defensible resolutions. The most satisfying result is the CO-group UNI win:
Slovenian's *posameznik* preserves the source's repeated *individual* across the whole group with a
single, unambiguous stem.
