# CVscale translation notes: English → Thai

**Source language:** English · **Target language:** Thai (ภาษาไทย)

Files written to `instruments/`:
- `cvscale-th.tsv` — 26 items across the five groups
- `dimensions-th.csv` — dimension names, English kept after " / "
- `scales-th.csv` — Likert anchors (`ไม่เห็นด้วยอย่างยิ่ง`…`เห็นด้วยอย่างยิ่ง`; `ไม่สำคัญอย่างยิ่ง`…`สำคัญอย่างยิ่ง`)

## Target-language characterization

Thai suits this instrument structurally but is treacherous lexically.

- **Grammar is friendly.** Thai is analytic and **grammatically genderless**: no inflection, no
  agreement, no obligatory number. Gender stays invisible everywhere except the MA group, where it
  is lexical and intended. Words are stable tokens I can simply repeat, so **UNI is easy to honor**.
- **Register layering is the main hazard.** Thai stacks an **Indic (Pali/Sanskrit) and Khmer learned
  vocabulary** above a native Tai core, plus dedicated **royal and ecclesiastical registers**. The
  natural-sounding word very often carries a Buddhist, royal, or civic-moral secondary sense English
  has no counterpart for. This drove most of the decisions below (AMB, CON).
- **Connotation is the real risk, not accuracy.** For PO and CO especially, the idiomatic Thai term
  is frequently the *morally loaded* one — hierarchy and group loyalty are live civic-education
  vocabulary in Thai. Several near-synonyms would have translated the proposition correctly while
  **amplifying its valence** past the neutral English. Matching the source's flatness took active
  restraint (CON).
- **Politeness/gender particles were avoidable.** Sentence-final ครับ/ค่ะ are gender-marked, but the
  items are plain declaratives that take no particle. The first person in UN1/UN3 was a genuine
  problem (see §4).
- **Register stability across varieties is good.** Isan/Northern/Southern speakers all read Standard
  Thai in writing, so a neutral formal register is comparable across the population the file targets.

**Orthographic note:** Thai does not use a full stop to end sentences — it separates clauses and
sentences with spaces. The PO/UN/CO/MA items are therefore complete sentences **without** a final
period, and the intra-sentence breaks (e.g. MA2's semicolon, UN3's "because") are rendered as spaces.
This is correct Thai, not a missing character. Sentence-vs-phrase form is otherwise preserved: LT
items remain verbless noun phrases.

## 1. CO1–CO6 — "the group" (CON / SEM)

The single most consequential choice in the file. Variants for "the group":

- **A) `กลุ่ม`** — "group". Literal, neutral, colourless.
- **B) `ส่วนรวม`** — "the collective / the common good / the public at large".
- **C) `หมู่คณะ`** — "the collective body / one's company", literary, Pali-derived.

**B is the trap.** `ส่วนรวม` is overwhelmingly the natural-sounding Thai here, because CO1 maps
almost exactly onto **`เสียสละประโยชน์ส่วนตนเพื่อประโยชน์ส่วนรวม`** ("sacrifice self-interest for the
common good") — a set moral maxim drilled through Thai civic education. Choosing it would have made
the item read as a **virtue slogan a respondent is socially obliged to endorse**, not a neutral
proposition to be scored — a serious CON violation that would skew the whole CO scale upward. It
also fails **SEM**: `ส่วนรวม` means *society at large*, whereas Hofstede's collectivism is about
**in-groups** (family, team, employer). C carries a similar communal-loyalty warmth plus polysemy
(`คณะ` = faculty/committee/delegation).

Selected **A** `กลุ่ม` throughout CO1–CO6. **CON was decisive**: the English says "the group" flatly
and the Thai must too, even at the cost of sounding plainer than idiomatic Thai would.
`ประโยชน์ส่วนตน` ("self-interest") is kept in CO1, which deliberately leaves the maxim's first half
intact while breaking its second — the echo is faint enough not to trigger the slogan reading.

## 2. CO6 — "Group loyalty" (CON, register)

Variants for "loyalty":

- **A) `ความภักดี`** — plain loyalty (as in `ความภักดีของลูกค้า`, customer loyalty).
- **B) `ความจงรักภักดี`** — loyalty/allegiance, but in practice **the word for devotion to the
  monarchy and nation** (`จงรักภักดีต่อสถาบันพระมหากษัตริย์`).
- **C) `ความซื่อสัตย์`** — honesty/faithfulness.

B is the fuller, more "correct-sounding" dictionary equivalent and a Thai writer might reach for it
first — but it is quasi-sacred and politically charged, and would have imported a register the
neutral English "group loyalty" nowhere suggests (CON, and an AMB-grade register intrusion). C is
the wrong sense (SEM: honesty ≠ loyalty). Selected **A** `ความภักดีต่อกลุ่ม`. Same logic as §1:
**refuse the loaded term even when it is the idiomatic one.**

For "suffer" (`even if individual goals suffer`) I used **`ได้รับผลกระทบ`**. In English "be
affected" would be too neutral a gloss for "suffer" — but Thai `ผลกระทบ` (`กระทบ` = to strike,
impinge) is **default-negative**: `ผู้ได้รับผลกระทบ` means *those adversely affected*. It therefore
carries "suffer"'s mild passive negativity without the overshoot of `เสียหาย` ("be damaged") or
`ต้องเสียสละ` ("must be sacrificed" — which would also forge a false link to CO1's `เสียสละ`).

## 3. CO3 / CO5 — "welfare" (AMB)

Variants: **A) `สวัสดิภาพ`** (welfare/well-being, as in `สวัสดิภาพเด็ก`, child welfare) vs.
**B) `สวัสดิการ`** (welfare *benefits* — employee perks, social-welfare programmes) vs.
**C) `ความเป็นอยู่ที่ดี`** (well-being, descriptive) vs. **D) `ผลประโยชน์`** (interests/benefit).

A and B differ by one syllable and are easily confused, but B is a false friend: it names an
**institutional benefits package**. In CO3 — "Group welfare is more important than individual
rewards" — B would read as *the group's benefits vs. individual bonuses*, turning a values item into
a compensation question (AMB). D shifts the sense to "interests" and would echo CO1's
`ประโยชน์ส่วนตน`, forging a link the source lacks. C is accurate but a multi-word phrase that sits
oddly on an abstract "group". Selected **A**, uniform in CO3 and CO5. **AMB was decisive.** A's
residual lean toward "safety" is the accepted cost; `สวัสดิภาพ` is the standard non-institutional
equivalent of abstract "welfare".

## 4. UN1 / UN3 — the first person (gender)

Thai's ordinary polite "I" is **gender-marked**: `ผม` (male) / `ดิฉัน` (female). The instrument
cannot ask a respondent to self-mark gender in PO/UN/CO items. Options: **A) `ฉัน`** — neutral in
written Thai (female-leaning in speech only), standard in translated questionnaires;
**B) `ข้าพเจ้า`** — formally gender-neutral but legal/official-document register, which would lift
UN1/UN3 above the register of every other item; **C) pro-drop** — grammatical in Thai, but UN1/UN3
are explicitly *about the respondent personally* ("what **I'm** expected to do"), so dropping the
pronoun dilutes the item.

Selected **A** `ฉัน`. It satisfies the skill's gender-neutrality requirement while holding the
register level across the file.

## 5. MA1 — "a professional career" (SEM / LAM)

Thai has **no clean noun for "career" as distinct from "job"**: `อาชีพ` is occupation/employment.
The English "professional career" is ambiguous between (i) *a career in a profession*
(doctor/lawyer) and (ii) *a serious working career, as opposed to not working*. No Thai option
preserves both readings, so LAM could not be honored and the tie fell to SEM:

- **A) `อาชีพการงานที่ก้าวหน้า`** — "an advancing career" → reading (ii).
- **B) `อาชีพในสายวิชาชีพ`** — "an occupation in a professional field" → reading (i).

Within Masculinity the item's target is plainly **men-have-careers vs. women-don't** — reading (ii).
Selected **A**; **SEM decisive**. `ที่ก้าวหน้า` ("advancing") is a deliberate small addition: it is
what carries the English "career"-not-merely-"job" contrast that bare `อาชีพ` would lose.

## Structural notes

- **PO group:** "people in higher/lower positions" = `ผู้ที่อยู่ในตำแหน่งสูงกว่า` /
  `ผู้ที่อยู่ในตำแหน่งต่ำกว่า`, uniform across PO1–PO5 (UNI). Rejected `ผู้บังคับบัญชา` /
  `ผู้ใต้บังคับบัญชา` ("superiors/subordinates") — it names the roles the source only describes, in a
  bureaucratic-military register.
- **PO4 "disagree with decisions"** = `คัดค้าน` (object to / oppose). The literal `ไม่เห็นด้วยกับ`
  was rejected on AMB: it echoes the response anchor `เห็นด้วย` ("agree"), producing a double
  negative ("should not not-agree"), and private non-agreement is not PO4's target — open deference
  is. This matches the sibling translations (vi `phản đối`, ko `반대`). LT2's "opposition" uses a
  *different* stem, `การต่อต้าน`, keeping the two groups lexically separate.
- **UN group "instructions"** (UN1, UN2, UN5) = `คำแนะนำ` uniformly (UNI). Rejected `คำสั่ง`
  ("orders/commands"): it imports authority and would drag Uncertainty Avoidance items into **Power
  Distance's semantic field** (SEM) — the dimension is about wanting clarity, not about being
  commanded. `คำแนะนำ`'s slight lean toward "advice" is the accepted cost; it is the standard Thai
  for written instructions (`คำแนะนำการใช้งาน` = operating instructions).
- **"procedures"** = `ขั้นตอน` in UN2 and UN4 (UNI); "expected" = the `คาดหวัง` stem in UN1 and UN3,
  while preserving the source's distinction between "what I'm expected to do" (`ฉันถูกคาดหวังให้ทำ
  อะไร`) and "what is expected of me" (`มีสิ่งใดที่ถูกคาดหวังจากฉัน`).
- **"individual"** = the `บุคคล` stem throughout CO: `บุคคล` as the noun (CO1, CO2, CO5) and
  `ส่วนบุคคล` adjectivally (CO3, CO4, CO6) — UNI honored via shared stem. CO5's "their goals"
  (`เป้าหมายของตน`) is kept distinct from CO6's "individual goals" (`เป้าหมายส่วนบุคคล`), mirroring
  the source. "success" = `ความสำเร็จ` uniform in CO4 (×2), LT5, LT6; "success in the future" =
  `ความสำเร็จในอนาคต` identical in LT5 and LT6. "should" = `ควร` across all PO and CO items.
- **LT glosses:** `(ความประหยัด)` for Thrift — chose the transparent everyday term over the formal
  `ความมัธยัสถ์` for register stability. `(ความพากเพียร)` for Persistence — chose it over
  `ความเพียร`, which carries a **Buddhist resonance** (`วิริยะ`, one of the perfections) that the
  secular English gloss lacks (AMB). LT5 "giving up" = `การยอมสละ` (willingly forgo), kept clear of
  CO1's `เสียสละ` ("sacrifice").
- **MA group:** gender marked with `ผู้ชาย` / `ผู้หญิง` uniformly across MA1–MA4 (the source varies
  "men/women" vs. "a man/a woman"; Thai keeps one neutral-register pair for comparability). Rejected
  `เพศชาย`/`เพศหญิง` (clinical form-speak) and `บุรุษ`/`สตรี` (elevated Sanskrit). MA2 "intuition" =
  `สัญชาตญาณ` — despite its "instinct" lean, `สัญชาตญาณของผู้หญิง` *is* the Thai for "women's
  intuition"; `ญาณหยั่งรู้` would have imported Buddhist supernatural insight (AMB). MA3 "typical of
  men" = `ลักษณะทั่วไปของผู้ชาย` ("a general characteristic"), not `ลักษณะเฉพาะ` ("a distinctive/
  exclusive characteristic"), which would overshoot "typical" (CON).
- **MA4 "jobs"** = `งาน`, the broad work/task reading rather than `อาชีพ` (occupations) — consistent
  with the convention visible across the sibling files (de `Tätigkeiten`, fr `tâches`, ko `일`).
  Thai `งาน` carries the same job/task breadth as the English (LAM).
- **Scales:** `อย่างยิ่ง` ("strongly/extremely") anchors both scales, matching "strongly"/"very" and
  keeping the two five-point scales parallel, consistent with the sibling translations.
  `ไม่เห็นด้วยอย่างยิ่ง`/`เห็นด้วยอย่างยิ่ง` is the conventional Thai Likert agreement pair used in
  scientific questionnaires.
- **Dimensions:** used the established Thai Hofstede renderings — `ระยะห่างเชิงอำนาจ`,
  `การหลีกเลี่ยงความไม่แน่นอน`, `กลุ่มนิยม`, `การมุ่งเน้นระยะยาว`, `ความเป็นชาย`.

## Confidence

Thai is a well-resourced language and I am reasonably confident in this translation. The residual
risk is **not** comprehension but **connotation calibration** (§1, §2): Thai's civic-moral and
royal-Buddhist register layers sit very close to this instrument's PO and CO vocabulary, and I have
consistently chosen the flatter, plainer term over the more idiomatic loaded one. A Thai native
reviewer should specifically re-check that `กลุ่ม` (§1) does not read as *too* bare, and confirm
`สวัสดิภาพ` (§3) over `ความเป็นอยู่ที่ดี`.
