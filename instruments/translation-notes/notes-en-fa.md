# CVscale translation notes: English → Persian

**Source language:** English · **Target language:** Persian (Farsi, فارسی)

Files written to `instruments/`:
- `cvscale-fa.tsv` — 26 items across the five groups
- `dimensions-fa.csv` — dimension names, English kept after " / "
- `scales-fa.csv` — conventional Likert anchors (`کاملاً مخالفم`…`کاملاً موافقم`; `بسیار بی‌اهمیت`…`بسیار مهم`)

## Target-language characterization

Persian fits this instrument well and I have solid command of it. Key axes:

- **Gender is grammatically invisible.** Persian has no grammatical gender and a single neutral
  third-person pronoun (`او`), so PO, UN, CO, and LT stay gender-neutral effortlessly. Only the MA
  group forces explicit marking, done with the plain pair `مردان` (men) / `زنان` (women).
- **Diglossia (register split).** Persian has a strong written-formal vs. colloquial-spoken divide.
  A questionnaire must use the written standard, which is also the variety most stable across the
  Iran/Afghanistan readerships (Tajik's Cyrillic aside), keeping responses comparable. I used formal
  written forms throughout (`مهم‌اند`, `می‌رود`, `بپرهیزند`) and avoided any colloquial contractions.
- **Arabic-loan polysemy / register layering.** Many natural words carry a secondary
  classical/technical sense English lacks — the main AMB/LAM watch-point (see UN5 below).
- **Connotation & culture (CON).** Hierarchy and group loyalty carry culturally weighty overtones;
  I kept the neutral positional vocabulary (`جایگاه`, not the authority-loaded `مقام`) so the items
  don't amplify the source's neutral valence.
- **Derivational morphology.** Shared stems make UNI easy to honor: `موفقیت` (success) recurs
  verbatim in CO4/LT5/LT6, `مسائل` (problems) across MA2/MA3, `اهداف` (goals) across CO5/CO6.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. UN5 — "Instructions for operations" (AMB / LAM / UNI)

"operations" here means *carrying out the work*, not anything martial or medical. Variants:
**A) `دستورالعمل‌های انجام کار`** (instructions for doing the work) vs.
**B) `دستورالعمل‌های عملیاتی`** ("operational instructions"). B is the tighter one-word match, but
`عملیات`/`عملیاتی` in Persian pulls strongly toward *military operations* and, in another register,
*surgery* — an ambiguity the neutral English lacks (AMB). I chose **A**, which reads unambiguously as
work-procedure instructions and preserves the `دستورالعمل` stem shared across UN1, UN2, and UN5
(UNI). AMB was decisive.

## 2. "People in higher/lower positions" — `جایگاه` vs. `مقام` (CON / SEM)

The PO group hinges on how "positions" is rendered. Variants: **A) `جایگاه بالاتر/پایین‌تر`**
(higher/lower standing or position) vs. **B) `مقام بالاتر/پایین‌تر`** (higher/lower office, rank of
authority). Power Distance is *about* authority, so B looks on-topic for SEM — but the English
"positions" is deliberately neutral-positional, and `مقام` loads each sentence with formal
officialdom and prestige that the source doesn't carry, over-stating the authority valence (CON).
Since the Power-Distance framing already comes from the item content itself (consult, delegate,
disagree), I let CON win and chose **A** `جایگاه`, used identically across all five PO items (UNI).

## 3. CO2 vs. CO6 — keeping "stick with" and "loyalty" distinct (SEM / UNI)

CO2 "stick with the group" and CO6 "group loyalty" are related but the source keeps them lexically
separate. The risk was collapsing both onto `وفاداری` (loyalty). For CO2 I used
**`در کنار گروه بمانند`** (stay by the group's side) — the literal "stick with," a behavioural
staying-put — and reserved **`وفاداری به گروه`** (loyalty to the group) for CO6, where the source
actually says "loyalty." This mirrors the source's own distinction rather than forging a link it
doesn't make (an anti-UNI-overreach choice). Relatedly, in CO6 "individual goals suffer" became
`اهداف فردی آسیب ببینند` (goals are harmed/set back) — a mild, passive setback matching "suffer,"
not the stronger `به خطر بیفتند` (be jeopardized).

## Structural note

The LT items are kept as verbless phrases with no closing period, and their parenthetical glosses
are translated as positive virtue terms: `(صرفه‌جویی)` for Thrift and `(پشتکار)` for Persistence
(CON). `موفقیت` renders "success" everywhere it recurs, `رفاه گروه` renders "welfare of the group"
in both CO3 and CO5, and `مسائل` renders "problems" across MA2/MA3 — all to preserve the source's
within-group uniformity (UNI). In MA3, "active, forcible approach" became `رویکردی فعال و قاطع`
(active and firm/assertive); `قاطع` captures the assertive force without tipping into `با اعمال زور`
("by use of force"), which would overshoot the source's strength.
