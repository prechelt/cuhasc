# Translation notes: English → Chinese (zh)

- **Source language:** English (en)
- **Target language:** Chinese (zh) — rendered in **Simplified characters, Standard Written
  Chinese (现代标准汉语)**. The `zh` code here deliberately bundles Mandarin with Cantonese, Wu,
  Xiang and other topolects, all of which share the same written standard; so the translation
  targets the written standard, which keeps responses comparable across those varieties. Simplified
  script was chosen because the Mainland speaker base is by far the largest; a Traditional-character
  edition would be character-for-character mappable with no wording changes.

## How Chinese stresses the rules

- **Register / variety split:** the written standard is highly stable across regions (the split is
  mainly script, Simplified vs. Traditional, not wording), so cross-variety comparability is easy to
  honor.
- **Derivational morphology:** Chinese builds words by compounding shared morphemes, which makes UNI
  cheap to honor deliberately (reuse a stem) but also easy to violate by accident. This drove the
  choice of one fixed word per repeated concept: 职位较高/较低的人 for "higher/lower positions"
  (all PO items), 集体 for "group" (all CO items), 未来的成功 for "success in the future" (LT5/LT6).
- **Connotation & culture (CON):** the biggest live issue. Everyday Chinese loads authority and group
  loyalty with a warmer, more approving valence than the neutral English. See CO/PO decisions below.
- **Gender:** Chinese written 他/她 differ but nouns like 男性/女性 are neutral and job words carry no
  grammatical gender, so the MA items translate without forced gendering beyond what the source states.

## Most difficult decisions

### 1. CO group — how to render "group" (CON vs. SEM/UNI)
Candidates: **A 集体** (collective) vs. **B 群体** (a group/aggregate of people).
- B 群体 is the sociologically neutral term — just "a group."
- A 集体 is the word inside 集体主义 ("collectivism"), so it sits squarely in the dimension's
  semantic field (SEM) and is the term the Chinese Hofstede literature uses. Its risk is CON: 集体
  carries a positive, quasi-ideological glow ("the collective") that neutral English "group" lacks,
  which could nudge respondents toward agreement.
Chose **A 集体**. SEM and UNI (one consistent word across all six CO items, matching the dimension
label 集体主义) were decisive, and 集体 is the established convention for this construct; the mild CON
amplification is accepted as the lesser cost. Verbs were kept deliberately plain (CO2 "继续留在集体中",
literally "keep remaining in the collective," rather than idioms like 不离不弃) so as not to add
further loyalty-valence on top of the noun.

### 2. PO group — "people in higher/lower positions" (SEM/CON)
Candidates: **A 职位较高/较低的人** ("people whose position is higher/lower") vs. **B 上级/下级**
("superiors/subordinates").
- B is more idiomatic and concise, but it narrows the scope to a defined organizational
  chain-of-command and adds a rank relationship the English keeps generic and abstract.
- A stays literally at "positions," matching the source's abstraction (SEM) and adding no extra
  hierarchy connotation (CON).
Chose **A**, used identically across PO1–PO5 (UNI), accepting the greater length.

### 3. UN group — keeping "instructions", "procedures", "rules" distinct (LAM/UNI)
English uses three overlapping words the dimension needs kept apart: *instructions* (UN1, UN2, UN5),
*procedures* (UN2, UN4), *rules and regulations* (UN3). Chinese has several near-synonyms
(指示 / 说明 / 程序 / 流程 / 规章制度) that blur easily, which would collapse the distinctions the
source draws (LAM). Fixed mapping: **instructions → 指示** (UN1, UN2, and 操作指示 in UN5),
**procedures → 流程** (UN2 "指示和流程", UN4 "工作流程"), **rules and regulations → 规章制度** (UN3, a
standard fixed compound). This keeps each English term one-to-one with a distinct Chinese term across
the group.

## Minor notes
- **LT items** are phrases, not sentences, so they take no sentence-final 。 (matching the English and
  German phrasings); parenthetical glosses were translated (节俭 "Thrift", 坚持不懈 "Persistence") and
  set in full-width （）.
- **LT3** "Personal steadiness and stability": rendered 稳重与稳定 (composure/steadiness + stability)
  to avoid the tautology that 稳定与稳定 would produce.
- **scales-zh.csv** uses the conventional Chinese Likert endpoints: 非常不同意 … 非常同意 and
  非常不重要 … 非常重要.
- **dimensions-zh.csv** uses the standard academic renderings (权力距离, 不确定性规避, 集体主义,
  长期导向, 男性化) with the English name kept after " / " per the `dimensions-de.csv` model.

Overall the translation was mostly clean; the one recurring judgment call is the CON valence of
authority/collective vocabulary, resolved consistently in favor of the established construct terms.
