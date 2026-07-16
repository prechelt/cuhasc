# CVscale translation notes: English → Hungarian

**Source language:** English · **Target language:** Hungarian (magyar)

Files written to `instruments/`:
- `cvscale-hu.tsv` — 26 items across the five groups
- `dimensions-hu.csv` — dimension names, English kept after " / " (corpus convention:
  CO carries "Collectivism vs. Individualism", MA plain "Masculinity")
- `scales-hu.csv` — Likert anchors (`egyáltalán nem értek egyet`…`teljesen egyetértek`;
  `egyáltalán nem fontos`…`nagyon fontos`)

## Target-language characterization

Hungarian is Uralic, like the Finnish and Estonian translations already in this corpus, and
it shares their two most consequential properties: no grammatical gender and heavy
agglutination/compounding. Four axes drove the item-level choices.

**No grammatical gender.** Hungarian has a single genderless third-person pronoun *ő* and
marks no gender on nouns, adjectives, or verbs. The gender-neutrality instruction is therefore
free everywhere except the MA group, where the source names the sexes and Hungarian simply
says *férfiak* / *nők*. Nothing in PO, UN, CO, or LT exposes a gender. Nor is there a live
T/V (*tegezés*/*magázás*) problem: only UN1 and UN3 speak in the first person, and
*várnak el tőlem* / *mit kell tennem* are neutral.

**Register / variety.** Hungarian's written standard is remarkably uniform regionally — there
is no written-vs-spoken or dialect split of the kind Finnish has — so comparability across
respondents is not at risk from variety choice. The real risk axis is *hivatali nyelv*
(officialese/bureaucratese). Reaching for it would load the normative PO/CO items with an
administrative charge the plain English lacks. This decided the modal: **kellene** (the
conditional "should", what an ordinary Hungarian says), never **kell** ("must", too strong and
categorical for the source's "should"), and never the legalistic passive constructions. It also
kept *betartás* (UN2, the neutral word for complying with instructions) and *eljárás*
(procedure) rather than any deference-laden verb that would bleed UN toward PO.

**Agglutination, compounding, and derivational stems.** Derivation is extremely productive, so
UNI is cheap to honor deliberately (*siker* across CO4/LT5/LT6; *cél* across CO5/CO6; *utasítás*
across UN1/UN2/UN5; *jólét* across CO3/CO5; the *magasabb/alacsonyabb beosztásban lévő emberek*
frame across all five PO items) — but it is also cheap to *violate by accident*, fusing two
items the source keeps separate. This trap, not any single hard word, produced the three most
interesting decisions below (CO2, MA4, PO4).

**Polysemy and connotation.** Hungarian has little of the classical/religious layering that
complicates Romance and Slavic translations. *Hűség* (CO6 "loyalty") is built on *hű*
(faithful) but in modern usage is thoroughly secular — *márkahűség* (brand loyalty),
*házastársi hűség* (marital fidelity) — so it carries no devotional tinge (the same near-miss
Finnish recorded for *uskollisuus*, resolved the same way). Authority and gender terms are
connotationally neutral (*maszkulinitás* is the academic Hofstede term, not the everyday
*férfiasság*; *takarékosság* is neutral-positive like "thrift"). One ambiguity present in the
source is *not* reproducible: LT2 "opposition" → *ellenállás* means resistance, whereas the
political sense English "opposition" faintly carries is *ellenzék* in Hungarian, a wholly
separate word (LAM cost accepted — no Hungarian option carries it, and *ellenállás* is
unambiguously the intended reading).

**Capability caveat.** Hungarian is mid-resource for me. I am confident in the case government,
the agglutinative morphology, and the standardized Hofstede dimension terminology (*hatalmi
távolság*, *bizonytalanságkerülés*). I am somewhat less certain about fine collocational
naturalness in three LT phrasings — *állhatatosság* for "steadiness" (LT3), *működési
utasítások* for "instructions for operations" (UN5), and the nominalized *A mai szórakozásról
való lemondás* (LT5). Those are where a native review would pay off most.

## 1. CO2 "stick with the group" (UNI applied negatively — the agglutination trap)

The natural first reach for "stick with the group even through difficulties" is *ki kellene
tartaniuk a csoport mellett* (*kitart vki mellett* = stand by someone). But *kitart-* is
exactly the stem of LT2's rendering of **Persistence** (*Kitartás*), and the source keeps
"stick with" (CO) and "Persistence" (LT) lexically separate. Using *kitart* here would forge a
cross-dimension link the English does not have.

The obvious escape — *hűnek maradni a csoporthoz* (remain loyal to the group) — is worse: it
imports *hűség*, which is CO6's word for **loyalty**, collapsing the source's deliberate CO2/CO6
distinction ("stick with" vs. "loyalty") *inside* the same group.

- **A) *a csoport mellett kellene maradniuk*** — should stay by the group's side.
- **B) *ki kellene tartaniuk a csoport mellett*** — should stick with / persevere by the group.
- **C) *hűnek kellene maradniuk a csoporthoz*** — should remain loyal to the group.

Chose **A**, *marad* (stay/remain — cf. Estonian *jääma grupi juurde*). *A csoport mellett
marad* is idiomatic and connotationally identical to "stick with", and *marad-* collides with
nothing. The decisive argument was UNI applied twice negatively: A is the only option that
preserves both the CO2/LT2 separation and the CO2/CO6 separation the source has.

## 2. MA4 "some jobs" (SEM / UNI, cross-group distinctness)

The corpus has settled that "jobs" here means kinds-of-work, not professions (German
*Tätigkeiten*, Dutch *taken*, Estonian *tegevused*). Hungarian's candidates each risk a
cross-group collision:

- **A) *tevékenységek*** (activities) — the calque of the corpus solution; collides with
  nothing.
- **B) *feladatok*** (tasks) — but *feladat* is PO5's noun (*fontos feladatokat átruházni*),
  so MA4 would echo the delegation item and drag PO's authority frame into a gender item (SEM).
- **C) *munkák*** (works/jobs) — *munka* is the basic word for work, but it already appears in
  UN4 (*munkaeljárások*) and LT6 (*kemény munka*); the source's "work" links those two, and
  reusing *munka* in MA4 would extend the link to an item the English marks off with the
  *different* word "jobs".
- **D) *dolgok*** (things) — too vague.

Chose **A**, *tevékenységek*. It matches the reading the corpus already fixed and is the only
candidate that avoids both the PO5 *feladat* collision and the UN4/LT6 *munka* link. Rendered
*Vannak bizonyos tevékenységek, amelyeket egy férfi mindig jobban el tud végezni, mint egy nő.*
Note *el tud végezni* (is able to carry out) keys on skill, not physical capacity — English
"can do better" is about competence here (the same *osaa*/*pystyy* distinction Finnish drew).

## 3. PO4 "disagree with decisions" (CON vs. UNI, two echoes to dodge)

"People in lower positions should not disagree with decisions by people in higher positions."
The most literal "disagree" is the scale anchor *egyet nem ért*, and the natural paraphrase
"be of a different opinion" imports *vélemény* — which is PO2's word (*kikérni a véleményét*).

- **A) *nem kellene ellentmondaniuk a … döntéseinek*** — should not contradict / gainsay the
  decisions.
- **B) *nem kellene egyet nem érteniük a … döntéseivel*** — should not disagree with (reuses the
  scale anchor; also a clumsy double negation).
- **C) *nem kellene más véleményen lenniük*** — should not be of a different opinion (reuses
  PO2's *vélemény*).

Chose **A**, *ellentmond*. In an authority context *ellentmond a főnöke döntésének* is the
ordinary way to say a subordinate voices disagreement with a superior's decision — squarely
PO's semantic field (SEM). It is marginally stronger than a bare "disagree" (CON), but B is
stilted and reuses the response anchor, and C forges the PO2 echo; A is the cleanest of the
three. Estonian accepted the *eriarvamus* (opinion) echo here; Hungarian can avoid it.

## The `important5` low anchor (conventional vs. bipolar)

Like Finnish, Estonian, and Czech, Hungarian has no idiomatic bipolar "very unimportant"
anchor. The conventional questionnaire low-end is *egyáltalán nem fontos* ("not at all
important"), which is what I used against *nagyon fontos* ("very important"). The honest cost,
worth recording: this pair is unipolar (a zero anchor) where the English is bipolar, so the
Hungarian scale's low end is very slightly less negative than the source's. The literal calque
*nagyon lényegtelen* ("very insignificant") overshoots (CON) and is not what Hungarian
questionnaires use.

## Structural / uniformity notes

- **PO frame:** *magasabb / alacsonyabb beosztásban lévő emberek* in all five items. *Beosztás*
  is the native word for one's position/rank in an organization (vs. the loan *pozíció*), and
  the *magasabb/alacsonyabb* pair is the standard hierarchical opposition. *Emberek* is kept in
  every clause (as German keeps *Personen*, Estonian *inimesed*) to preserve the source's
  "people" (PO) vs. "individuals" (CO) lexical contrast → *emberek* / *egyének*.
- **PO1 vs. PO2:** the source uses two distinct verbs, "consulting" and "ask the opinions".
  Rendered *egyeztetés nélkül* (without conferring, PO1) vs. *kikérni a véleményét* (ask for
  the opinion, PO2), preserving the contrast; *egyeztet* is the natural verb for conferring
  before a decision and keeps *vélemény* out of PO1.
- **PO5:** *átruházni … emberekre* rather than *delegálni … embereknek*. Both mean "delegate",
  but *átruház* (govern­ing the sublative *-re*) avoids a double dative — the *-nek* subject and
  a *-nek* recipient would otherwise sit side by side ambiguously. *feladat* (task) lives only
  here, kept clear of MA4 (see §2).
- **UN group:** *utasítás* recurs across UN1/UN2/UN5 and *eljárás* across UN2/UN4, reproducing
  the source's within-group repetition of "instructions" and "procedures". UN4 is *szabványosított
  munkaeljárások* rather than the more frequent *munkafolyamatok* precisely to keep the
  UN2/UN4 "procedures" (*eljárás*) link visible. UN5 "instructions for operations" →
  *működési utasítások*: deliberately vague like the source, keeping the *utasítás* stem
  (recorded overtone: a faint operating-manual flavor, as with *használati utasítás* —
  neutralized by the surrounding UN items).
- **UN1 vs. UN3:** the source distinguishes "what I'm expected **to do**" (UN1) from "what is
  expected of me" (UN3); Hungarian reproduces it at no cost — *mit kell tennem* vs. *mit várnak
  el tőlem* — with distinct "spelled out"/"inform" verbs too (*kifejt* vs. *tájékoztat*).
- **CO group:** *egyének* (individuals) throughout, distinct from PO's *emberek*. *Jólét*
  (welfare) is identical in CO3 and CO5; *siker* (success) in CO4 (and LT5/LT6); *cél* (goal)
  in CO5 and CO6. CO1 "sacrifice" → *feláldoz*, kept distinct from LT5 "giving up" → *lemondás*,
  as the source uses different words.
- **CO3/CO4 "individual X":** *egyéni jutalmak* / *egyéni siker* mirror the *A csoport X …
  egyéni X* parallel exactly.
- **LT form:** the source mixes noun phrases and gerund phrases; Hungarian nominalizes both
  (*kezelése*, *továbbhaladás*, *lemondás*), which is what Hungarian does with such value
  headings. LT5/LT6 end identically in *a jövőbeli siker érdekében*, as the source repeats "for
  success in the future". LT2 "resolutely" → *elszánt* is kept out of MA3, which uses *aktív,
  erőteljes* for "active, forcible" (the source uses distinct words). *erőteljes* (forceful,
  vigorous), not *erőszakos* (violent), matches the strength of "forcible" without overshooting
  (CON).
- **MA2:** the semicolon and the exact two-clause parallelism are preserved, both instruments
  in the instrumental case (*logikai elemzéssel* / *intuícióval*), matching the source's
  repeated "with".
- **Dimension names** use the established Hungarian management-literature terms: *hatalmi
  távolság*, *bizonytalanságkerülés*, *hosszú távú orientáció* (consistent with LT4's *hosszú
  távú tervezés*), *kollektivizmus*, *maszkulinitás*.
- **Modal:** *kellene* throughout PO and CO, never *kell* — see the characterization above.
