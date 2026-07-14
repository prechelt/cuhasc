# CVscale translation notes: English → Vietnamese

**Source language:** English · **Target language:** Vietnamese (Tiếng Việt)

Files written to `instruments/`:
- `cvscale-vi.tsv` — 26 items across the five groups
- `dimensions-vi.csv` — dimension names, English kept after " / "
- `scales-vi.csv` — Likert anchors (`rất không đồng ý`…`rất đồng ý`; `rất không quan trọng`…`rất quan trọng`)

## Target-language characterization

Vietnamese fits this instrument well. It is **grammatically gender-neutral** (no gendered
nouns, no gender agreement) and **analytic** (no inflection), so gender stays invisible
everywhere except the MA group, and UNI is easy to honor because words are stable tokens I can
simply repeat. Its defining trait is the **Sino-Vietnamese (Hán-Việt) register layer** that
parallels Chinese: an academic/formal vocabulary (`phúc lợi`, `tập thể`, `quy trình`,
`chuẩn hóa`) sits above native words, and choosing the right layer sets the questionnaire's
register. The **written standard is regionally stable**, so I stayed in neutral formal register
and avoided colloquialisms. The main watch-points were **register layering / connotation**
(picking the Sino-Vietnamese term where it reads as neutral-academic rather than heavy) and a
few near-synonym choices where English uses distinct words I did not want to collapse.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. PO4 — "disagree with decisions" (SEM / CON, plus AMB)

Variants for "disagree with": **A) `phản đối`** (object to / oppose openly) vs.
**B) `không đồng ý với`** (literally "not agree with"). B is the most literal gloss of
"disagree," but it directly echoes the response scale (`đồng ý` = agree), and — more decisively —
silent private disagreement is not PO4's target. Within Power Distance the item is about a
subordinate *not openly challenging* a superior's decision, i.e. deference. **A** `phản đối` sits
squarely in that semantic field (SEM); its strength is "object to / oppose," short of `chống lại`
("go against") or `bác bỏ` ("overrule/reject"), which would overshoot on CON. I chose **A**, with
SEM (and the scale-echo problem, an AMB concern) decisive. The same stem reappears as the noun
`sự phản đối` for "opposition" in LT2 — a different dimension, so no within-group UNI conflict, and
the shared root is semantically apt in both.

## 2. UN — "instructions" as `hướng dẫn` (UNI)

"Instructions" recurs in UN1, UN2, and UN5. Candidates: **A) `hướng dẫn`** (guidance /
instructions / manual) vs. **B) `chỉ dẫn`** (directions) vs. **C) `chỉ thị`** (directive /
command). `chỉ thị` imports a top-down command tone the neutral English lacks (CON), so it was
out. Between `hướng dẫn` and `chỉ dẫn`, `hướng dẫn` is the natural word for written operating
instructions and reads unambiguously across all three contexts (`hướng dẫn được trình bày chi
tiết`, `hướng dẫn và quy trình`, `hướng dẫn vận hành`). I used **A** everywhere to honor UNI.
UN5's "operations" became `vận hành` (operating a system/machine) rather than a Sino-Vietnamese
`hoạt động`, keeping the "operating instructions" reading clean.

## 3. CO6 — "individual goals suffer" (CON)

Variants for "suffer": **A) `bị cản trở`** (be hindered / obstructed) vs. **B) `bị ảnh hưởng`**
(be affected) vs. **C) `bị tổn hại`** (be harmed / damaged). B is too neutral — "affected" loses
the negativity of "suffer." C ("harmed") overstates a passive setback. **A** `bị cản trở` is the
natural intransitive collocation for a goal being set back and matches the mild, passive-negative
valence of "suffer" (CON). Chose **A**.

## Structural notes

- **"group" = `tập thể`** (the collective) throughout CO — the ideologically apt term for the
  Collectivism dimension (SEM) — with "welfare of the group" = `phúc lợi của tập thể` uniform in
  CO3 and CO5, and "individual" = `cá nhân` throughout.
- **"success" = `thành công`** uniform in CO4 (×2), LT5, LT6; **"success in the future" =
  `thành công trong tương lai`** identical in LT5 and LT6; **"expected" = `kỳ vọng`** in UN1 and UN3.
- **"should" = `nên`** across all PO and CO prescriptive items.
- PO1 "consulting" (`tham khảo ý kiến`) vs. PO2 "ask the opinions" (`hỏi ý kiến`) are kept
  distinct, mirroring the source's two different verbs.
- **MA group:** gender is marked with the standard formal pair `nam giới` / `nữ giới`, used
  uniformly across MA1–MA4 (the source varies "men/women" vs. "a man/a woman"; Vietnamese keeps a
  single neutral-register pair for comparability).
- **LT items** are kept as phrases (no verb-of-obligation, no closing period); the parenthetical
  glosses are rendered as positive virtue terms — `(Tiết kiệm)` for Thrift, `(Kiên trì)` for
  Persistence — and `Kiên trì` (gloss) is kept distinct from the main verb `kiên quyết`
  (resolutely) in LT2.
- **Scales:** `rất` ("very/strongly") anchors both scales, matching "strongly"/"very" and keeping
  the two five-point scales parallel, consistent with the sibling translations.
