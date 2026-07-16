# CVscale translation notes: English → Greek

**Source language:** English · **Target language:** Greek (Ελληνικά)

Files written to `instruments/`:
- `cvscale-el.tsv` — 26 items across the five groups
- `dimensions-el.csv` — dimension names, English kept after " / "
- `scales-el.csv` — Likert anchors (`διαφωνώ απόλυτα`…`συμφωνώ απόλυτα`; `πολύ ασήμαντο`…`πολύ σημαντικό`)

## Target-language characterization

Modern Greek is the standardized Demotic-based written language. The old Katharevousa/Demotic
diglossia is settled, but its residue is the axis that matters here: a large **learned lexical
layer** sits above everyday vocabulary, and many ordinary words carry a **classical or religious
secondary sense** English lacks. The written standard is uniform across regions, so there is no
dialectal variety split a questionnaire must navigate — the live axis is vertical (learned vs.
everyday). Four features drove the item-level choices:

- **Gender is mostly avoidable for free.** Greek adjectives, participles and predicate nouns are
  gendered, but the constructions this instrument needs sidestep that. "Individuals" maps to the
  **neuter** `τα άτομα`, so all CO predicates agree with a neuter noun, not the respondent. The
  agreement anchors are **verbs** (`διαφωνώ`/`συμφωνώ`, 1st-person present), which are gender-free.
  Impersonal `κανείς` ("one", UN2) avoids a subject entirely. No item forces a gender call.
- **Derivational transparency — a UNI gift and an inverse-UNI risk.** `άτομο` (individual) →
  `ατομικός` (individual, adj.) reproduces the source's own *individuals*/*individual* stem tie
  exactly across CO (see §2). Conversely `λύνω` (solve, MA2) → `επίλυση` (solving, MA3) hands the
  source's *solve*/*solving* echo back for free. The risk to steer around: LT2's `αποφασιστικ-`
  (resolute) must not resurface in MA3 "forcible", and LT2's `Επιμονή` (persistence) must not
  bleed into LT3 "steadiness" or LT6 "working hard".
- **Polysemy / religious layering (AMB).** Two natural candidates carry a church sense English does
  not: `λειτουργία` for "operation" is also the **Divine Liturgy / Mass** (UN5, §3), and `πίστη`
  for "loyalty" is also religious **faith** (CO6). Both were avoided.
- **Connotation & culture (CON).** One political-connotation trap fired: `λιτότητα` for "thrift"
  now means government **austerity** in Greece and is strongly negatively charged (LT1, §1). And
  the MA dimension name `Αρρενωπότητα` carries a valorizing "virility" charge the neutral
  dimension label should not amplify (noted below).

Greek matches the source cleanly almost throughout; the three decisions worth explaining are below.

## 1. LT1 "(Thrift)" — the austerity trap (CON / AMB)

The gloss "(Thrift)" names a *virtue* — being economical, positively valenced. Three renderings
were weighed:

- **A) `Λιτότητα`** — the dictionary word for thrift/frugality, but in contemporary Greek it is
  first read as **fiscal austerity** (the memorandum-era `μέτρα λιτότητας`), carrying a heavy
  negative political charge. Using it would invert the source's positive valence. Rejected (CON).
- **B) `Οικονομία`** — "economizing/saving" (`κάνω οικονομία`), positively valenced and everyday,
  but the bare noun `Οικονομία` also means **"the economy"** — an ambiguity the English "Thrift"
  does not have (AMB).
- **C) `Φειδώ`** — the precise, single-word virtue term for thrift/sparingness, positively
  valenced, with no austerity or "economy" reading.

Chose **C**. Decisive: it is the only candidate that keeps the positive valence *and* is
unambiguous. It is a slightly learned word, but a one-word virtue label (Hofstede's own register)
tolerates that, and `φειδωλός` ("thrifty") keeps it in common recognition. The everyday `Οικονομία`
would have been the natural spoken choice, but its "the economy" sense is exactly the kind of
ambiguity the AMB rule exists to block.

## 2. "Individuals" / "individual" (CO group) — a stem tie kept (UNI)

English ties *individuals* (CO1, CO2, CO5) to *individual* (CO3 rewards, CO4 success, CO6 goals)
by a shared stem. Greek reproduces this for free: the noun **`άτομο`** ("individual/person",
neuter) and the adjective **`ατομικός`** share the `ατομ-` stem, so `τα άτομα` … `ατομικές
ανταμοιβές` / `ατομική επιτυχία` / `ατομικοί στόχοι` carries the source's morphology intact. This
also keeps "People" (PO group, `άνθρωποι`) lexically distinct from "Individuals" (`άτομα`), exactly
as the source keeps them. "Self-interest" (CO1) was rendered `προσωπικό συμφέρον` (personal
interest), deliberately **not** `ιδιοτέλεια` ("selfishness"), which would add a pejorative charge
the neutral source "self-interest" lacks (CON), and not `ατομικό συμφέρον`, which would wrongly
pull the "self" onto the "individual" stem the source keeps separate here.

## 3. UN5 "operations" — the liturgy trap (AMB)

"Instructions for operations are important." The obvious literal candidates both fail on ambiguity
English does not share:

- **B) `λειτουργίες`** — "operations/functions", but `λειτουργία` is first of all the **Divine
  Liturgy (Mass)**, and secondarily a machine's/organ's functioning. A live religious reading the
  source has no trace of (AMB).
- **C) `επιχειρήσεις`** — "operations" in the military/business sense, but also plainly
  **"businesses/companies"** — doubly ambiguous (AMB).

Chose **A) `εκτέλεση των εργασιών`** ("carrying out of the work/tasks"). It renders the intended
"operations = things done at work" sense with no religious, military or corporate shadow, and stays
lexically clear of `διαδικασίες` ("procedures", UN2/UN4), a distinction the source makes. `Οδηγίες`
("instructions") is held constant across UN1, UN2 and UN5, mirroring the source's own repetition
(UNI).

## Structural / uniformity notes

- **`θα πρέπει να` for "should" (CON).** Used uniformly for all ten "should" items (all of PO, plus
  CO1/CO2/CO5/CO6), with `δεν θα πρέπει να` for "should not". This is the ordinary deontic "should"
  — weaker than bare `πρέπει` ("must") and stronger than a hedged `θα ήταν καλό να`, matching the
  source's strength and keeping the modal uniform across positive and negative PO items as the
  source does.
- **"people in higher/lower positions"** → `άνθρωποι σε ανώτερες/κατώτερες θέσεις`, identical in all
  five PO items. `ανώτερος/κατώτερος` ("higher/lower in rank") lands squarely in the Power-Distance
  semantic field (SEM); with `θέσεις` ("posts") the reading is hierarchical rank, not "seats".
- **PO3 "social interaction"** → `κοινωνική συναναστροφή` (social mixing/keeping company), not
  `κοινωνική επαφή` (bland "social contact") or `κοινωνική αλληλεπίδραση` (sociology jargon that
  would wrongly sweep in work interaction). `συναναστροφή` names the informal, non-work socializing
  the item is about (SEM).
- **PO4 "disagree"** → `διαφωνούν`, which deliberately echoes the scale anchor `διαφωνώ` — mirroring
  the source's own echo between "strongly **disagree**" and PO4's "should not **disagree**".
- **UN1 vs. UN3.** The source's subtle split is preserved: UN1 "what I'm expected **to do**" →
  `τι αναμένεται να κάνω`; UN3 "what is expected **of me**" → `τι αναμένεται από εμένα`. Same verb
  `αναμένεται` in both, as in the source (UNI), with the do/of-me difference kept.
- **PO5 "delegate"** → `αναθέτουν` (assign/entrust tasks), not the bureaucratic `εκχωρούν`, which
  collocates with *authority*, not tasks. "tasks" → `καθήκοντα` (duties), kept distinct from MA4
  "jobs" → `δουλειές`, as the source keeps "tasks"/"jobs" distinct.
- **CO2 vs. CO6.** CO2 "stick with the group" → `παραμένουν στην ομάδα` (cohesion), kept clear of
  the loyalty field that belongs to CO6 → `αφοσίωση` ("devotion/loyalty"). `αφοσίωση` was chosen
  over `πίστη`, which in Greek is first of all religious **faith** (AMB), and over `νομιμοφροσύνη`,
  which is political allegiance (to state/law), too narrow.
- **"welfare of the group"** → `ευημερία της ομάδας`, identical in CO3 and CO5 (UNI). "success" →
  `επιτυχία` throughout (CO4, LT5, LT6), matching the source's shared word.
- **CO6 "suffer"** → `θίγονται` (are compromised/harmed), the natural verb for goals being
  undercut; `υποφέρουν` (literally "suffer") is used of sentient beings and would read oddly of
  goals.
- **LT2 "resolutely / (Persistence)"** → `Αποφασιστική συνέχιση … (Επιμονή)`. `Επιμονή` is the
  standard positive persistence term. LT2's `αποφασιστικ-` is kept out of MA3, and `Επιμονή` out of
  LT3/LT6, so the source's separation of these items survives (inverse UNI).
- **LT3 "steadiness and stability"** → `σταθερότητα και ευστάθεια`, two distinct near-synonyms
  matching the source's own doublet.
- **LT5 "giving up"** → `Παραίτηση από` (renunciation), kept distinct from CO1 "sacrifice" →
  `θυσιάζουν`, as the source keeps "giving up"/"sacrifice" distinct.
- **MA1 "professional career"** → `επαγγελματική σταδιοδρομία` (native term) rather than the
  loanword `καριέρα`; both are current, the native term is register-neutral.
- **MA3 "active, forcible"** → `ενεργητική, δυναμική`. `δυναμική` ("forceful/assertive") matches
  the source's "forcible" strength; `επιθετική` ("aggressive") or `βίαιη` ("violent") would
  overshoot (CON), and `αποφασιστική` would forge the LT2 link. `επίλυση` (MA3 "solving") echoes
  `λύνουν` (MA2 "solve") via the `λυ-/λυσ-` stem, matching the source (UNI).
- **MA2** uses the Greek semicolon (ano teleia, `·`) for the source's semicolon, per Greek
  punctuation.
- **Dimension names** use established Greek Hofstede terminology: `Απόσταση εξουσίας`, `Αποφυγή
  αβεβαιότητας`, `Μακροπρόθεσμος προσανατολισμός`, and the loan `Κολεκτιβισμός` (parallel to German
  `Kollektivismus`). For MA I kept the established `Αρρενωπότητα` ("masculinity/manliness"); it does
  carry a mild valorizing/virility charge the neutral dimension label ideally would not (CON), but
  Greek has no crisp neutral technical loan for this dimension, and the retained English
  "/ Masculinity" disambiguates.
- **`important5` anchors** → `πολύ ασήμαντο … πολύ σημαντικό`. The `σημαντικό`/`ασήμαντο` pair
  reproduces the source's important/unimportant antonymy via the α-privative, mirroring English
  un-. `διαφωνώ απόλυτα … συμφωνώ απόλυτα` are the standard verb anchors of Greek scientific
  questionnaires — conventional *and* gender-free, so convention and neutrality do not conflict
  here (unlike the Slavic versions).

## Confidence

No capability caveat applies: Greek is well-resourced for me, and every source item has a natural,
register-stable Greek equivalent. The translation was largely straightforward; the three genuine
difficulties (the austerity trap in LT1, the individual-stem tie in CO, the liturgy trap in UN5)
each have clean resolutions rather than compromises. The Greek-specific hazard worth remembering is
the **learned/classical-religious secondary sense**: plausible everyday words (`λειτουργία`,
`πίστη`, `λιτότητα`) carry a second meaning — liturgical, religious, or fiscal-political — that
English lacks, and each had to be checked against contemporary usage rather than trusted from a
dictionary gloss.
