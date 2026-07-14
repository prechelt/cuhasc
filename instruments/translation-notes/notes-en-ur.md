# CVscale translation notes: English → Urdu

**Source language:** English · **Target language:** Urdu (اردو)

Files written to `instruments/`:
- `cvscale-ur.tsv` — 26 items across the five groups
- `dimensions-ur.csv` — dimension names, English kept after " / "
- `scales-ur.csv` — Likert anchors (`پوری طرح غیر متفق`…`پوری طرح متفق`; `بہت غیر اہم`…`بہت اہم`)

## Target-language characterization

Urdu is the Perso-Arabic-script, right-to-left register-sibling of Hindi: the two share
Hindustani grammar and everyday vocabulary, but Urdu draws its formal/abstract layer from
Persian and Arabic rather than Sanskrit. I have solid command of it. Key axes:

- **Grammatical gender is real but avoidable.** Unlike Persian, Urdu marks gender on verbs
  and adjectives. The instrument mostly escapes this because PO/UN/CO use the `…کو … چاہیے`
  deontic construction (infinitive + modal), which is gender-neutral, and the UN first-person
  clauses use gender-invariant present forms (`مجھے معلوم رہے`, `مجھ سے توقع کی جاتی ہے`).
  Only the MA group forces gender, done with the plain pair `مرد` (men) / `عورت` (women),
  where the gendered verb agreement (`کرتے ہیں` / `کرتی ہیں`) is content-driven, not leaked.
- **Register / register-layering (AMB/LAM).** A questionnaire uses standard written Urdu.
  The main watch-point is Persian/Arabic loans whose natural sense carries a secondary
  technical meaning English lacks — the `کام کاج` vs `آپریشن/عملیات` choice at UN5 below.
- **Connotation & culture (CON).** For PO especially, Urdu's authority vocabulary (`اقتدار`,
  `حاکم`) is heavier than the neutral English "positions"; I kept the plain organizational
  word `عہدہ` (post) so the PO items don't amplify the source's neutral valence.
- **Derivational morphology makes UNI easy.** `اہم` renders "important" across UN1/UN2/UN3/UN5;
  `کامیابی` renders "success" across CO4/LT5/LT6; `مسائل` renders "problems" across MA2/MA3;
  `مقاصد` renders "goals" across CO5/CO6; `فلاح` renders "welfare" across CO3/CO5.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. UN5 — "Instructions for operations" (AMB / LAM / UNI)

"operations" here means *carrying out the work*, nothing martial or medical. Variants:
**A) `کام کاج کے لیے ہدایات`** (instructions for the work/doings) vs.
**B) `آپریشن/عملیات کے لیے ہدایات`** (instructions for operations). B is the one-word match,
but in Urdu `آپریشن` reads first as *surgery*, and `عملیات` pulls toward *military operations*
(and, in another register, occult/spiritual practice) — an ambiguity the neutral English lacks
(AMB). I chose **A**, which reads unambiguously as work-procedure instructions and keeps the
`ہدایات` (instructions) stem shared with UN1 and UN2 (UNI). AMB was decisive.

## 2. "People in higher/lower positions" — `عہدہ` vs. `مقام/اقتدار` (CON / SEM)

The whole PO group hinges on "positions". Variants: **A) `اعلیٰ/نچلے عہدوں پر فائز لوگ`**
(people holding higher/lower posts) vs. **B) `بالادست/زیردست`** (superiors/subordinates) or an
`اقتدار`-based "people in authority". Power Distance is *about* authority, so B looks on-topic
for SEM — but the English "positions" is deliberately neutral-positional, and the
authority-loaded options pre-load each sentence with dominance/subordination that the source
doesn't state, over-stating the valence (CON). Since the Power-Distance framing already comes
from the item content (consult, delegate, disagree), I let CON win and used the neutral
organizational `عہدہ` (post/position), identically across all five PO items (UNI). "People"
stays `لوگ`, kept distinct from CO's "individuals" = `افراد`, mirroring the source's own
people/individuals split.

## 3. CO2 vs. CO6 — keeping "stick with" and "loyalty" distinct (SEM / UNI)

CO2 "stick with the group" and CO6 "group loyalty" are related, but the source keeps them
lexically separate and I did too. CO2 became **`گروہ کے ساتھ جڑے رہنا`** (stay joined to /
attached to the group) — a behavioural staying-put — while `وفاداری` (loyalty) was reserved for
CO6, where the source actually says "loyalty". Collapsing both onto `وفاداری` would forge a link
the source avoids. Relatedly, in CO6 "individual goals suffer" became `مقاصد کو نقصان پہنچے`
(goals are harmed/set back) — a mild setback matching "suffer", not the stronger "be
jeopardized"; and in LT5 "giving up today's fun" is `چھوڑنا` (give up), keeping the stronger
`قربانی` (sacrifice) reserved for CO1, where the source says "sacrifice" (CON).

## Structural note

The LT items are kept as verbless phrases with no closing period; their parenthetical glosses
are rendered as the conventional virtue terms `(کفایت شعاری)` for Thrift and `(استقامت)` for
Persistence. In MA3, "active, forcible approach" became `سرگرم اور بھرپور اندازِ عمل`
(active and vigorous/full-force approach); `بھرپور` captures the forcefulness without tipping
into `طاقت کے زور پر` ("by force"), which would overshoot the source's strength (CON) — the
same calibration the Persian and Arabic versions make. Sentences close with the Urdu full stop
`۔` and MA2's clause break uses the Arabic semicolon `؛`.
