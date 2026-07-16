# CVscale translation notes: English → Latvian

**Source language:** English · **Target language:** Latvian (latviešu valoda)

Files written to `instruments/`:
- `cvscale-lv.tsv` — 26 items across the five groups
- `dimensions-lv.csv` — dimension names, English kept after " / "
- `scales-lv.csv` — conventional Likert anchors (`pilnīgi nepiekrītu`…`pilnīgi piekrītu`;
  `ļoti nesvarīgi`…`ļoti svarīgi`)

## Target-language characterization

Latvian is a Baltic language (its only close living relative is Lithuanian), heavily
inflected: seven cases, two grammatical genders, no articles, and all prepositions govern
the dative-instrumental in the plural. Four features drove the item-level choices:

- **Register is stable.** Unlike the diglossic Slavic cases, standard written Latvian is a
  single register that questionnaires uniformly inhabit; the one regional variety
  (Latgalian) is not used for instruments. So no comparability risk arose from register,
  and everything here is plain standard Latvian.
- **Verbs are gender-free, adjectives/participles are not.** Crucially, Latvian finite verbs
  do **not** mark gender — first-person `zinu` ("I know"), passive `tiek gaidīts` ("is
  expected") and `cieš` ("suffers") are all gender-neutral. Gender only surfaces on
  adjectives and participles. This let UN1 keep the first person without the gender-marking
  problem that forced restructuring in the Slavic versions; I only had to route around
  agent participles (e.g. CO5 uses passive `ir apsvērta` rather than the masculine
  `apsvēruši`). `cilvēki` ("people") is grammatically masculine but referentially neutral.
- **Derivational morphology makes UNI cheap — and here it even *rescues* a link the Slavic
  versions lost.** Shared stems carry `grupa`→`grupas`/`grupu`/`pie grupas` across all six CO
  items and `risina`(MA2)→`risināšana`(MA3) for "solve"/"solving". More notably, Latvian has
  both the sociological noun `indivīds` and the adjective `individuāls` on **one** Latin stem
  `individu-`, so the source's "individuals"…"individual" thread (present in all six CO items)
  is reproduced intact — where Czech, for instance, had to break it (`jednotlivec` vs.
  `individuální`).
- **Polysemy traps in the international vocabulary.** The Latinate loans that look like free
  wins carry narrowed senses: `operācija` is first a *surgical* (or military) operation, and
  `stāvoklis` ("position/standing") colloquially means "pregnancy". Both were avoided (see
  UN5 and the PO note).

Three decisions were worth flagging; otherwise the mapping was clean.

## 1. PO4 "should not disagree with decisions" — the stacked negation (CON)

Variants: **A)** `nevajadzētu nepiekrist … lēmumiem` (should not disagree-with the decisions —
literal) vs. **B)** `nevajadzētu apstrīdēt lēmumus` (should not dispute/challenge) vs. **C)**
`nevajadzētu iebilst pret lēmumiem` (should not object to).

English "disagree" is mild — merely holding a contrary view. `apstrīdēt` ("dispute,
challenge") and `iebilst` ("object, raise objection") both imply voiced, active pushback and
overshoot the source's valence. The only literal option, A, stacks two negations
(`ne-vajadzētu ne-piekrist`), and the question was whether that reads as clumsy or as a
drafting error — the objection that pushed several other languages off their literal
rendering. It does not: in Latvian the negation is a **bound prefix** on each of two separate
words, which is ordinary negative concord (cf. everyday `nevajadzētu nekavēties`), not a
double-negative slip. With the naturalness objection gone, CON is decisive and the mild,
literal **A** wins.

## 2. UN5 "Instructions for operations" — the `operācija` trap (AMB, SEM)

The tempting cognate rendering **B)** `Norādījumi par operācijām` fails: `operācija` denotes
first a **surgical** operation, secondarily a military one — the neutral English "a thing
done / a task carried out" is not a salient Latvian reading, so B injects an ambiguity the
source lacks (AMB). **C)** `Ekspluatācijas norādījumi` ("operating instructions") is the fixed
term for a *machine/equipment* manual and would narrow the item to industrial settings (SEM).
Chose **A)** `Norādījumi par darbībām` ("instructions for activities/operations"), where
`darbības` is the neutral Latvian word for things-done/work-operations. `Norādījumi`
("instructions/directions") is used across UN1, UN2 and UN5 to preserve the source's
within-group repetition of "instructions" (UNI).

## 3. MA3 "active, forcible approach" — matching force without coercion (CON)

Variants for "forcible": **A)** `spēcīga pieeja` ("forceful/powerful approach") vs. **B)**
`enerģiska pieeja` ("energetic") vs. **C)** `varmācīga pieeja` ("using force, coercive").
C carries an unmistakably negative, coercive colouring the neutral English "forcible" (=
characterized by vigour/force) does not have — it would distort the item's valence (CON). B
is a near-synonym of the item's own first adjective `aktīvs` ("active") and would make the
pair `aktīvu, enerģisku` nearly redundant. Chose **A** `spēcīgu`: it conveys assertive force
while staying a genuinely distinct second adjective and keeping the source's neutral valence.

## Structural / uniformity notes

- **"people in higher/lower positions"** → `cilvēki augstākos/zemākos amatos`, kept uniform
  across all five PO items. `amats` ("post, office") was chosen over `stāvoklis` ("standing"),
  whose colloquial sense "pregnancy" is a needless AMB risk, and over `pozīcija` (spatial).
  The light phrase `cilvēki + amatos` is used for subject and prepositional slots; the two
  genitive-possessor slots (PO2 "opinions of…", PO4 "decisions by…") use the participle
  `esošo` (`…amatos esošo cilvēku`) for a clean genitive.
- **"the group"** → `grupa` in all six CO items (`grupas` / `grupu` / `pie grupas`), and
  **"welfare of the group"** → `grupas labklājība`, identical in CO3 and CO5 (UNI).
- **CO2 "stick with the group"** → `turēties pie grupas` (hold onto), kept lexically clear of
  the `lojalitāte` field belonging to CO6, so the two items stay distinct as in the source.
- **"success"** → `panākumi` throughout (CO4 `individuāli panākumi`; LT5/LT6 `nākotnes
  panākumu labā`, identical for "success in the future"), matching the source's repetition.
- **"solve/solving problems"** → the shared stem `risin-` links MA2 `risina problēmas` and
  MA3 `problēmu risināšana`, as in the source.
- **LT glosses** are lowercased per Latvian orthography: "(taupība)" (thrift, positively
  valenced), "(neatlaidība)" (persistence). LT2's phrase uses `apņēmīga` ("resolute") and the
  gloss `neatlaidība` ("persistence"), keeping the two distinct as the source does.
- **Dimension names** use established Latvian Hofstede terminology: `Varas distance`,
  `Izvairīšanās no nenoteiktības`, `Kolektīvisms`, `Ilgtermiņa orientācija`, `Maskulinitāte`.
- **Scale anchors:** `pilnīgi nepiekrītu` / `pilnīgi piekrītu` is the standard Latvian 5-point
  agreement pair, with gender-free present-tense verbs; `ļoti nesvarīgi` / `ļoti svarīgi` is
  the conventional importance pair.

## Confidence

No capability caveat applies: Latvian is well-resourced and every source item has a natural,
register-stable equivalent. The genuine difficulties were the three flagged above (the PO4
stacked negation, the `operācija` polysemy trap, and the MA3 force-vs-coercion call). The
most interesting finding is a happy one: Latvian's single `individu-` stem serves both the
noun and the adjective, so the "individuals / individual" thread that runs through every CO
item — and that several other languages had to break — is reproduced intact.
