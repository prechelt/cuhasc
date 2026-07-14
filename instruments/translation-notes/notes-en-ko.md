# Translation notes: English → Korean (en → ko)

**Source language:** English
**Target language:** Korean (한국어)

## Target-language characterization

- **Register / variety.** Korean has strong speech-level marking, but scientific
  questionnaires have a fixed convention: the plain written declarative in `-다`
  (예: `~해야 한다`, `~이 중요하다`). It is neutral, non-honorific, and stable across
  regions and formality contexts, so all statement items use it. This keeps responses
  comparable and avoids injecting politeness/deference that could bias the Power Distance
  items in particular.
- **Gender.** Korean has no grammatical gender and freely drops pronouns, so gender stays
  invisible everywhere except where the item is explicitly about men vs. women (MA group).
  There `남성`/`여성` (the neutral formal terms) are used consistently rather than the
  colloquial `남자`/`여자`.
- **Honorifics / status.** Korean *could* render "higher/lower positions" with the
  socially loaded pair `윗사람`/`아랫사람` (senior/junior person), which carries personal
  deference. To match the source's more organizational, neutral tone I used
  `지위가 높은 사람` / `지위가 낮은 사람` ("person of high/low position") throughout the PO
  group (CON — avoid amplifying the authority valence).
- **Derivational morphology / UNI.** Sino-Korean roots make uniformity easy to honor:
  "group" → `집단` in every CO item; "success in the future" → `미래의 성공` in LT5/LT6;
  "welfare (of the group)" → `복지` in CO3 and CO5.

## Scales and dimensions

- `scales-ko.csv` uses the standard Korean Likert anchors from published survey research:
  `전혀 그렇지 않다` … `매우 그렇다` (strongly disagree … strongly agree) and
  `전혀 중요하지 않다` … `매우 중요하다` (very unimportant … very important).
- `dimensions-ko.csv` uses the conventional Hofstede terms
  (`권력 거리`, `불확실성 회피`, `집단주의`, `장기 지향`, `남성성`) with the English name kept
  after `/`, mirroring `dimensions-de.csv`/`-ja.csv` (including "Collectivism vs.
  Individualism" for CO).

## Most difficult decisions

### 1. CO6 — "even if individual goals *suffer*" (rules UNI / LAM)

CO1 uses "sacrifice" (`희생`), and `희생되다` is also the most natural Korean rendering of
CO6's "suffer". Reusing it, though, would forge a lexical link the source deliberately
keeps separate (CO1 = deliberate sacrifice; CO6 = incidental detriment).
- **A:** `개인의 목표가 저해되더라도` — "even if individual goals are *hampered/set back*".
- **B:** `개인의 목표가 희생되더라도` — "even if individual goals are *sacrificed*".
Chose **A**: it preserves the source's distinction between the two words and keeps CO1's
`희생` reserved for genuine sacrifice. B reads slightly more naturally but collapses the
contrast (UNI in reverse / LAM).

### 2. PO3 — "social interaction" (rules SEM / CON)

- **A:** `사적인 교류` — "*private/personal* exchange".
- **B:** `사회적 상호작용` — literal "social interaction", but in Korean this is a technical
  sociology term, not everyday socializing.
- **C:** `사교적 교류` — "sociable exchange".
Chose **A**: the item is about informal mixing across ranks; B is register-mismatched and
sounds academic, while A conveys the "socializing outside the work relationship" sense
plainly. The small cost is that A foregrounds "private", but that stays inside the Power
Distance semantic field (SEM).

### 3. UN5 — "Instructions for operations" and the "instructions" thread (rule UNI)

UN1, UN2, and UN5 all use "instructions". The most idiomatic word for UN5 alone would be
`지침` (guideline), but UN1/UN2 use `지시 사항` (instructions/directives).
- **A:** `작업에 대한 지시 사항은 중요하다` — keeps `지시 사항` (uniform with UN1/UN2).
- **B:** `작업 지침은 중요하다` — more idiomatic standalone but breaks the shared root.
Chose **A** to honor UNI across the UN group, accepting marginally less punchy phrasing.
("operations" was read as workplace *tasks/work*, hence `작업`, matching UN4's `업무 절차`.)

## Overall

Apart from the three cases above the translation was largely straightforward: Korean maps
the PO/CO/MA statement items and the LT noun/gerund phrases cleanly, gender stays naturally
invisible, and the Likert and Hofstede terminology have well-established conventional
equivalents.
