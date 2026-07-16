# CVscale translation notes: English → Serbian

**Source language:** English · **Target language:** Serbian (српски / srpski)

Files written to `instruments/`:
- `cvscale-sr.tsv` — 26 items across the five groups
- `dimensions-sr.csv` — dimension names, English kept after " / "
- `scales-sr.csv` — Likert anchors (`уопште се не слажем`…`у потпуности се слажем`;
  `веома неважно`…`веома важно`)

## Script decision (read this first)

Serbian is **digraphic**: the same standard language is written in both Cyrillic and Latin,
and the two are a fully reversible, character-for-character mapping. Cyrillic is the official
and traditional script, so this translation is delivered in **Cyrillic**. A Latin rendering
(*Ljudi na višim položajima…*) is trivially and losslessly derivable and is equally standard in
everyday Serbian practice; no wording choice below depends on the script.

Two further standard choices were fixed for the whole file:
- **Ekavian reflex** (Serbia's dominant standard variety): *увек*, *неизвесност*, *решавање*,
  *успех*, *времена* — as opposed to the ijekavian *uvijek/neizvjesnost/rješavanje* used by
  Croatian/Bosnian. This keeps responses comparable within the Serbian-standard population.
- **The `да` + present construction** for modality (*требало би да доносе*) rather than the
  infinitive (*trebali bi donositi*). This is the natural Serbian pattern and, as a bonus,
  gives an impersonal neuter *требало* that is completely gender-free (see gender note).

## Target-language characterization

Serbian is a South Slavic (Štokavian) standard, closely related to and largely mutually
intelligible with Croatian/Bosnian/Montenegrin, but with its own codified norm. Four features
shaped the choices:

- **Register / variety stability.** Standard written Serbian is not strongly diglossic; the
  neutral written register used in questionnaires is stable across regions. Everything here is
  standard written Serbian, ekavian.
- **Derivational morphology — a UNI win.** Serbian keeps the source's *individuals* / *individual*
  link that Polish and Czech had to break: the noun *појединац* → *појединци* ("individuals",
  CO1/CO2/CO5) and its adjective *појединачни* ("individual, single") share the *појед-* stem, so
  *појединачне награде* (CO3), *појединачни успех* (CO4) and *појединачни циљеви* (CO6) all echo the
  noun, mirroring the source's one repeated word — no loan *индивидуални* needed.
- **Polysemy traps.** *операција* is first surgical/military, not a neutral "thing done" (UN5),
  and *силовит* ("forcible") shares the *сила*-root with *силовати* ("to force/rape"), loading a
  coercive/violent sense the neutral English lacks (MA3). Both were avoided — see below.
- **Gender marking.** Serbian forces gender on *l*-participles and predicate adjectives. Using
  the impersonal *требало би да* + present tense (PO, CO) sidesteps this entirely: *требало* is
  neuter and the following present-tense verb (*доносе*, *жртвују*) is gender-free. The one
  first-person item (UN1) was restructured to a gender-free present-tense *знам* (below). Scale
  anchors use present-tense *слажем се*, also gender-free.

Serbian is a well-resourced language and every source item had a natural, register-stable
equivalent. Three decisions were worth flagging.

## 1. MA3 "forcible" — avoiding the violence-loaded cognate (AMB, CON, SEM)

Variants for "an active, **forcible** approach": **A) активан, енергичан приступ** ("active,
energetic/forceful"); **B) активан, снажан приступ** ("active, strong/powerful"); **C) активан,
силовит приступ** (the direct cognate of "forcible").

C was rejected outright: *силовит* sits in the *сила* → *силовати* ("to force / to rape") family
and reads as coercive and violent — a colouring the neutral English "forcible" (assertive,
getting-things-done) does not carry (AMB/CON). That leaves the choice between енергичан and
снажан. *снажан* leans toward inherent physical strength ("strong"), while *енергичан* captures
the **dynamic, driving** force of the approach, which is what "forcible" means here — force
applied, not force possessed. The one objection is that *активан* and *енергичан* are near-
synonyms; but *активан, енергичан приступ* is an idiomatic Serbian collocation where *активан*
names the taking-of-action and *енергичан* its intensity, exactly the source's active/forcible
pairing. Chose **A** (*енергичан*), with *снажан* as the runner-up if a reviewer prefers a more
lexically distant second adjective.

## 2. PO4 "should not disagree" — the stacked negation (CON)

Variants: **A) не би требало да се **не** слажу са одлукама** ("should not disagree" — literal,
double negation) vs. **B) не би требало да се противе одлукама** ("should not oppose") vs.
**C) требало би да се слажу са одлукама** ("should agree").

Serbian, like Croatian, has no single positive verb for "disagree": *не слагати се* is inherently
*не* + *слагати се* ("to agree"). The literal rendering therefore stacks two *не* particles
(*не би требало … да се **не** слажу*), which reads a little heavy. But the particles attach to
different words (*не би требало* = "should not"; *да се не слажу* = "disagree"), so it is fully
grammatical, not an error. Crucially, only A preserves the source's **mildness**: English
"disagree" is merely holding a contrary view. *Противити се* (B) means actively oppose/resist,
and C ("should agree") demands positive endorsement rather than mere non-dissent — both overshoot
the item's force. CON is decisive → **A**.

## 3. UN1 first-person, and UN5 "operations" — restructure and polysemy avoidance (gender, AMB, UNI)

**UN1.** "…so that I always know what I'm expected to do." A literal purpose clause (*како bih
увек знао/знала*) uses the conditional *l*-participle, which is unavoidably gendered and would
spotlight the respondent's gender in an item unrelated to it (awkward in an instrument whose MA
group *does* measure gender attitudes). I restructured to a present-tense result clause: **"…тако
да увек знам шта се од мене очекује"** — *знам* carries no gender. The clause *шта се од мене
очекује* is reused verbatim in UN3, mirroring the source's repetition of "what is expected of me"
across UN1/UN3 (UNI).

**UN5.** *операција* in Serbian is first a **surgical**/military operation; the neutral English
"operations" (things done at work) is not a salient reading, so *упутства за операције* would
mislead (AMB). I used **"Упутства за рад"** ("instructions for work/operation"), where *рад*
neutrally covers work and the running of things. *Упутства* ("instructions") is reused across
UN1, UN2 and UN5, matching the source's repeated "instructions" (UNI).

## Structural / uniformity notes

- **"people in higher/lower positions"** → *људи на вишим/нижим положајима*, identical across all
  five PO items. *Положај* ("position, rank") preferred to the loan *позиција*; *надређени/
  подређени* ("superiors/subordinates") rejected as presuming a direct reporting line the source
  does not.
- **PO3 "social interaction"** → *дружење* ("socializing"); the sociological *друштвена
  интеракција* is jargon and would wrongly include work interaction (SEM).
- **"group"** → *група* throughout. Unlike Croatian (where *grupa* is a stigmatised colloquial
  loan and *skupina* is preferred), *група* is the ordinary, standard Serbian word (UNI): CO1 *за
  групу*, CO2 *уз групу*, CO3/CO5 *добробит групе*, CO4 *успех групе*, CO6 *групи*.
- **CO1 "for the group" vs. CO3/CO5 "welfare of the group".** CO1 is *за групу*, deliberately not
  echoing *добробит* ("welfare"), so it does not forge a CO1–CO3/CO5 link the source keeps
  separate. "Welfare of the group" is *добробит групе*, identical in CO3 and CO5 (UNI); *добробит*
  preferred to *благостање*, which narrows toward material prosperity.
- **CO2 "stick with the group"** → *остати уз групу* ("stay by the group"), kept lexically clear of
  the *оданост* ("loyalty") field belonging to CO6, so the two items stay distinct as in the
  source.
- **"individual" stem** → *појединачни* in CO3/CO4/CO6, sharing the *појед-* stem with the noun
  *појединци* (CO1/CO2/CO5), preserving the source's *individuals*/*individual* link (UNI).
- **"goals"** → *циљеви* in CO5 and CO6 (UNI). **"success"** → *успех* in CO4, LT5, LT6 (UNI).
- **PO5 "tasks" vs. MA4 "jobs"** stay distinct: *задаци* vs. *послови*.
- **UN "procedures"** → *поступци* in UN2 (*поступака*) and UN4 (UNI); *упутства* preferred over
  Croatian *упуте*.
- **UN3 agreement:** coordinated neuter *правила* + masculine-inanimate *прописи* → predicate takes
  masculine plural *важни*.
- **LT glosses** are the established Serbian Hofstede terms, lowercased in the parenthetical:
  "Thrift" → *штедљивост*; "Persistence" → *истрајност*. LT2's descriptor is *настављање*
  ("continuing"), which does not share a stem with its own gloss *истрајност* (mirroring the
  source's "going on" ≠ "persistence"). LT3 "steadiness" → *постојаност* (constancy), kept clear of
  *истрајност* so the LT2/LT3 distinction survives. "success in the future" → *за успех у
  будућности*, identical in LT5 and LT6 (UNI).
- **MA4 "can always do better"** → *увек може боље да обави* (да-construction); *може* reads as
  ability, not permission, so no perfective workaround was needed.
- **Dimension names** use established Serbian Hofstede terminology: *дистанца моћи*, *избегавање
  неизвесности*, *колективизам*, *дугорочна оријентација*, *маскулинитет*.
- **Scale anchors:** *уопште се не слажем* / *у потпуности се слажем* is the standard Serbian
  5-point agreement pair (present-tense, gender-free). For importance the source's symmetric
  "very…very" is kept as *веома неважно* / *веома важно*; Serbian survey practice also uses
  *уопште није важно* at the low pole, so a native reviewer may wish to confirm the importance
  anchors against local convention.

## Confidence

No capability caveat applies: Serbian is well resourced and every source item has a natural,
register-stable equivalent. The genuine difficulties were the three flagged above (the MA3
*силовит* violence trap, the PO4 stacked negation, and the UN1 forced gender marking), all with
defensible resolutions. The Serbian *да*+present modality yields a fully gender-neutral impersonal
*требало би да* for the PO and CO "should" items — cleaner on gender than Croatian's participial
*требали би* — and *појединац*/*појединачни* preserves the source's *individuals*/*individual*
stem link across the whole CO group.
