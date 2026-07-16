# CVscale translation notes: English → Danish

**Source language:** English · **Target language:** Danish (dansk)

Files written to `instruments/`:
- `cvscale-da.tsv` — 26 items across the five groups
- `dimensions-da.csv` — dimension names, English kept after " / "
- `scales-da.csv` — conventional Likert anchors (`helt uenig`…`helt enig`; `meget uvigtigt`…`meget vigtigt`)

Danish is the first Scandinavian language in this set, so there was no sibling North Germanic
translation to cross-check against; German and Dutch served as the closest structural siblings.

## Target-language characterization

Danish is a North Germanic language with heavy Middle Low German lexical borrowing, which puts
much of the organizational vocabulary of these items within one step of the German and Dutch
versions. The relevant axes:

- **Register / variety split.** Written Danish (*rigsdansk*) is exceptionally uniform — one
  standard, no regional written varieties, and no pluricentric split of the kind Dutch has
  across the Netherlands and Flanders. The written/spoken gap is mostly phonetic, not lexical.
  The old formal address pronoun *De* is effectively dead in questionnaire register, and in any
  case PO, CO and MA are framed impersonally in the third person; only UN1 and UN3 speak in the
  first person, where "hvad der forventes af mig" is register-neutral.
- **Derivational morphology.** Danish compounds as freely as German and Dutch
  (*gruppeloyalitet*, *arbejdsprocedurer*, *egeninteresse*), which makes UNI cheap to honor but
  equally cheap to violate by accident, since any two concepts can be welded into one stem.
  Watched for this in CO2 vs. CO6 and UN2/UN4 vs. UN5.
- **Polysemy / register layering.** Low overall — Danish has no classical or religious lexical
  layer of the kind that complicates Arabic, Persian or Hindi here. Two live traps did surface,
  both from the *modern* layer rather than an archaic one: *velfærd* (see CO3) and the verb
  *blive ved* (see CO2).
- **Connotation & culture.** This is the sharpest axis for Danish. Denmark sits at the extreme
  low end of Hofstede's own Power Distance scale, and the flat-hierarchy norm is culturally
  explicit (*Janteloven*). The effect on PO is the same one the Dutch notes describe, only
  stronger: a Danish verb of even moderate force (*modsige* "contradict", *sætte
  spørgsmålstegn ved* "call into question") reads as markedly confrontational rather than
  neutral, so an over-strong choice would have respondents answering a harsher question than
  the English one. CON therefore pushed consistently toward the mildest literal option in PO.
- **Gender & honorifics.** Danish marks gender lexically on nouns but not on *personer*,
  *mennesker*, or *individer*, so PO, UN and CO stay gender-invisible with no effort. MA1–MA4
  name genders in the source, so nothing is added there.

Danish is a high-resource language and no capability caveats apply. The translation was
largely straightforward; four decisions were worth flagging.

## 1. CO3 / CO5 "welfare of the group" (AMB)

This was the single hardest item, and it is a trap specific to Danish among the Germanic
languages. The literal cognate of *welfare* / *Wohlfahrt* / *welzijn* is **velfærd** — but in
modern Danish *velfærd* has been almost entirely captured by the welfare state
(*velfærdsstaten*, *velfærdssamfundet*, *velfærdsydelser*). "Gruppens velfærd" would make a
Danish respondent hear public provision and social benefits, an ambiguity the neutral English
"group welfare" does not carry at all (AMB).

Variants: **A) "gruppens vel"** (the group's good/wellbeing) vs. **B) "gruppens velfærd"**
(the group's welfare) vs. **C) "gruppens bedste"** (the group's best interest) vs.
**D) "gruppens velbefindende"** (the group's wellbeing). B carries the welfare-state reading and
was rejected outright. D is wrong in kind: *velbefindende* denotes felt, personal comfort and is
used of individuals and animals, so "gruppens velbefindende" is close to a category error. C is
the most idiomatic Danish of the four and reads perfectly naturally, but it shifts a *state*
("welfare") into an *interest* ("what is best for"), which slightly reframes CO3's comparison —
the source weighs a condition of the group against individual rewards, not a preference.

Chose **A**. *Vel* is the exact semantic counterpart of German *Wohl* and survives in current
Danish set phrases (*til fælles vel*, *landets vel*, *til alles vel*); it is faintly formal but
well inside questionnaire register, keeps the state-noun form, and is free of the welfare-state
reading. Avoiding an ambiguity the source lacks (AMB) was decisive over C's greater
naturalness. Used identically in CO3 and CO5, mirroring the source's own repetition (UNI).

## 2. CO2 "stick with the group" (UNI / AMB)

Two separate problems converged here.

First, the loyalty trap the Dutch notes identify: CO6 is *precisely* the loyalty item ("Group
loyalty should be encouraged…"), and the source keeps CO2 and CO6 lexically apart. German goes
the other way — *der Gruppe treu bleiben* ("stay loyal/faithful to the group") — which pulls CO2
into the *troskab/loyalitet* field that belongs to CO6 and collapses two distinct items into one
concept. Danish would invite exactly the same move (*være gruppen tro*), and I followed the
Dutch reading rather than the German one: UNI applied negatively, preserving the source's
separation.

That leaves the neutral options: **A) "blive i gruppen"** (stay in the group) vs.
**B) "blive ved gruppen"** (stay by the group) vs. **C) "holde fast ved gruppen"** (hold on to
the group) vs. **D) "holde sammen med gruppen"** (stick together with the group). B is the
closest literal rendering of "stick with" — and is disqualified by a Danish-specific ambiguity:
*blive ved* is also the ordinary verb for "to keep on, to continue" (*blive ved med at gøre
noget*), so "Individer bør blive ved gruppen" briefly garden-paths as "individuals should keep
on…" (AMB). C takes abstract objects far more comfortably than human collectives (*holde fast
ved sin beslutning*), and reads slightly off with *gruppen*. D imports a solidarity nuance the
plain English "stick with" does not carry — the same reason Dutch rejected *solidair blijven*.

Chose **A**: "Individer bør blive i gruppen, selv når der er vanskeligheder." It is marginally
weaker than "stick with", but it is unambiguous, stays squarely inside the Collectivism field
(SEM), and remains lexically distinct from CO6's *gruppeloyalitet*.

## 3. PO1–PO5 "positions" (LAM / SEM)

The whole PO group hangs on this word, so it was settled once and applied verbatim across all
five items. Variants: **A) "positioner"** (positions) vs. **B) "stillinger"** (posts, employment
positions) vs. **C) "overordnede/underordnede"** (superiors/subordinates).

C is what idiomatic Danish actually reaches for and would produce the most natural sentences by
some margin — but it is a lexicalized narrowing: it names a *direct reporting relationship*,
whereas the source deliberately uses a descriptive periphrasis about relative standing. It would
also destroy the source's verbatim "people in higher/lower positions" frame. Rejected on SEM.

B is the native Danish word and reads slightly more naturally than A, but *stilling* specifically
denotes an employment post. The CVscale measures a person's values generally, and the hierarchy
in PO need not be an employer's — so B adds a workplace specificity the general English
"positions" does not have (LAM). A is a well-established loan in exactly this sense (*en ledende
position*), keeps the source's generality, and matches the de/nl precedent (*Positionen*,
*posities*).

Chose **A**. Paired with **personer** rather than *mennesker* (which foregrounds humanness,
irrelevant here) or *folk* (colloquial), following German *Personen*.

## 4. PO4 "disagree with decisions" (CON)

Variants: **A) "ikke være uenige i beslutninger"** (not be in disagreement with decisions) vs.
**B) "ikke modsige beslutninger"** (not contradict decisions — the route German took with
*widersprechen*) vs. **C) "ikke sætte spørgsmålstegn ved beslutninger"** (not call decisions into
question). B and C are syntactically lighter and more idiomatic, but both shift from *holding* a
dissenting view to *voicing* it — a real strengthening. As the characterization above notes, that
strengthening costs more in Danish than in German: against Denmark's flat-hierarchy norm,
*modsige* reads as openly confrontational, so B would have respondents rating a harsher
proposition than the English. A is a little clunky after "bør ikke", but is the exact match for
the source's mild "disagree". Chose **A**, with CON decisive over naturalness.

## Structural / uniformity notes

- PO1–PO5 keep a fixed frame throughout: "personer i højere positioner" / "personer i lavere
  positioner", mirroring the source's verbatim repetition.
- PO1 "consulting" → *rådføre sig med* and PO2 "ask the opinions of" → *spørge … om deres mening*
  are kept lexically distinct, as in the source.
- "instructions" stays a standalone *instruktioner* across UN1, UN2 and UN5, preserving the
  source's within-group repetition. UN5 "instructions for operations" → "Instruktioner til
  arbejdsopgaver"; the compound *driftsinstruktioner* was rejected as plant/machinery-specific,
  and *arbejdsgange* ("workflows") was rejected because it would forge a link to the
  *procedurer* of UN2/UN4 that the source keeps separate.
- "what I'm expected to do" (UN1) and "what is expected of me" (UN3) both become "hvad der
  forventes af mig" — the source varies only syntactically, not conceptually.
- "Individuals" is *individer* throughout CO1/CO2/CO5, preserving the stem link to *individuelle
  belønninger* (CO3) and *individuel succes* (CO4) that the source has via individual/individuals
  (UNI). The more idiomatic Danish *den enkelte* would have broken that link.
- "success" is *succes* everywhere it recurs (CO4, LT5, LT6); "success in the future" is
  identically "succes i fremtiden" in LT5 and LT6.
- "usually" is *som regel* in both MA2 and MA3 (UNI).
- MA3 "difficult problems" → *vanskelige problemer* deliberately shares a stem with CO2's
  *vanskeligheder*, because the source shares one too (difficult / difficulties).
- MA4 "jobs" → *opgaver*, reading "jobs" broadly as tasks, in line with nl *taken* and fr
  *tâches*. This reuses *opgaver* from PO5's "tasks", but the overlap is cross-group rather than
  within-group, so UNI does not forbid it, and the source's own "tasks"/"jobs" are near synonyms.
  Danish *job* was rejected precisely because it would read as the occupational slot; *stillinger*
  was additionally unavailable, since it would have collided with the PO frame.
- LT glosses: "Thrift" → **Sparsommelighed**, the saving-as-virtue term, chosen over *nærighed*
  (stinginess, plainly negative) and *nøjsomhed* (frugality, contentment with little); this
  matches the de *Sparsamkeit* / nl *Spaarzaamheid* choice (CON). "Persistence" →
  **Vedholdenhed**, the standard Danish Hofstede term, over *stædighed* (stubbornness, negative)
  and *udholdenhed* (physical endurance).
- LT3 "steadiness" → *standhaftighed*, which overlaps somewhat with LT2's *vedholdenhed* — but
  the source's own "steadiness"/"persistence" overlap to the same degree, so this is faithful
  rather than a defect (the Dutch notes record the same judgment).
- LT2, LT5 and LT6 use a uniform "At + infinitive" phrase form; LT1, LT3 and LT4 are noun
  phrases, exactly as in the source.
- MA1 "professional career" → *professionel karriere*. The amateur/professional reading of
  *professionel* exists in Danish, but it exists in the English source too, so AMB is not
  engaged and the compound *erhvervskarriere* was not needed.
- Item form is preserved throughout: PO/UN/CO/MA are complete sentences, LT items are bare
  phrases; the parenthetical glosses in LT1 and LT2 are translated.
- `scales-da.csv`: *helt uenig* / *helt enig* is the conventional Danish Likert pair in
  scientific questionnaires and is the direct counterpart of nl *helemaal mee oneens* / *eens*.
  For the importance scale, the bipolar *meget uvigtigt* / *meget vigtigt* was kept in preference
  to the commoner unipolar Danish anchor *slet ikke vigtigt* ("not at all important"), since the
  source scale is bipolar.
- `dimensions-da.csv` uses the established Danish Hofstede terms: *magtdistance*,
  *usikkerhedsundgåelse* (with *undgåelse* "avoidance", not *undvigelse* "evasion"),
  *kollektivisme*, *langsigtet orientering*, *maskulinitet*.

## Confidence

Danish is a high-resource language, structurally close to English and very close to German and
Dutch, both of which were available as cross-checks. No capability caveats apply to this
translation. The one point a native reviewer should look at first is CO3/CO5 *gruppens vel*: the
choice is deliberate and defended above, but *vel* is the most formal register note in the
instrument, and a reviewer may prefer *gruppens bedste* if naturalness is weighted over the
state/interest distinction.
