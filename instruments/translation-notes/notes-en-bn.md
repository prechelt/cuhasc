# CVscale translation notes: English → Bengali

**Source language:** English · **Target language:** Bengali / Bangla (বাংলা)

Files written to `instruments/`:
- `cvscale-bn.tsv` — 26 items across the five groups
- `dimensions-bn.csv` — dimension names, English kept after " / "
- `scales-bn.csv` — Likert anchors (`দৃঢ়ভাবে একমত নই`…`দৃঢ়ভাবে একমত`; `অত্যন্ত গুরুত্বহীন`…`অত্যন্ত গুরুত্বপূর্ণ`)

## Target-language characterization

- **Register / diglossia + regional split.** Bengali has a historical সাধু (literary) vs.
  চলিত (colloquial-standard) divide; the modern written norm is চলিত. It also splits
  lexically between Bangladesh (more Perso-Arabic loans) and West Bengal (more Sanskritic
  তৎসম). A scientific questionnaire calls for standard written চলিত Bengali. I kept to
  Sanskritic-neutral vocabulary that is stable across both regions and both religious
  communities — গুরুত্বপূর্ণ (important), নির্দেশনা (instructions), গোষ্ঠী (group),
  কল্যাণ (welfare), সাফল্য (success), লক্ষ্য (goals), সমস্যা (problems) — avoiding both
  region-marked Perso-Arabic words and over-Sanskritized rarities, so responses stay
  comparable across the varieties respondents span.
- **No grammatical gender → gender is invisible for free.** Unlike German/Hindi, Bengali
  inflects neither verbs nor adjectives for gender, and its pronouns (সে, তিনি) are
  gender-neutral. The impersonal PO/UN/CO/LT items therefore carry no gender at all, and
  even MA2/MA4, where the verb করে / করতে পারে is shared, stay neutral except for the
  explicitly named পুরুষ (men) / নারী (women) — exactly as the source intends.
- **Derivational morphology → UNI is easy.** Shared তৎসম stems let recurring source words
  map to one Bengali word: গোষ্ঠী (group) across all CO items, নির্দেশনা (instructions)
  across UN1/UN2/UN5, পদ্ধতি (procedures) across UN2/UN4, কল্যাণ (welfare) across CO3/CO5,
  সাফল্য (success) across CO4/LT5/LT6, লক্ষ্য (goals) across CO5/CO6, সমস্যা (problems)
  across MA2/MA3. The ব্যক্তি stem also links the noun ব্যক্তি (individuals) with the
  adjective ব্যক্তিগত (individual), mirroring the source's own stem-sharing.
- **Honorifics.** Bengali forces a politeness choice on 2nd/3rd-person verbs and pronouns,
  but the items are impersonal generic statements (উচিত + infinitive) or 1st-person
  (আমি, UN1/UN3), so no honorific level had to be picked.

Overall the translation was largely clean — the absence of grammatical gender and the
rich তৎসম layer made both gender-neutrality and UNI effortless. Three decisions turned on
connotation and were worth flagging.

## 1. CO1 — "self-interest" (CON)

Variants for *self-interest*: **A) `নিজের স্বার্থ`** (one's own interest) vs. **B) bare
`স্বার্থ`**. স্বার্থ is the direct match, but on its own it drifts toward *selfishness* in
ordinary Bengali (the explicit noun for selfishness, স্বার্থপরতা, is built on it). English
"self-interest" is only mildly negative-to-neutral. Under **CON** I used **A**, `নিজের স্বার্থ`
— the possessive নিজের ("one's own") pins the sense to "personal interest", and the fixed
collocation `নিজের স্বার্থ ত্যাগ করা` ("sacrifice one's own interest") is standard and
neutral, without the selfish overtone bare স্বার্থ would add.

## 2. LT5 "giving up" vs. CO1 "sacrifice" (CON / UNI)

The noble verb `ত্যাগ করা` (renounce / sacrifice) fits CO1's "sacrifice self-interest for
the group". The obvious temptation is to reuse it in LT5 "giving up today's fun", but ত্যাগ
carries a quasi-ascetic, self-denying weight that is too heavy for LT5's light, everyday
"giving up fun". Since the source itself uses two different words, **UNI** does not require
one Bengali verb, and **CON** favors splitting them: I kept ত্যাগ in CO1 and used the
plainer `ছেড়ে দেওয়া` (give up / forgo) in LT5. For *fun* I chose আনন্দ (enjoyment) over
colloquial মজা or সুখ (comfort/ease), as the neutral fit for the thing foregone.

## 3. MA3 — "forcible approach" (SEM / CON)

For "an active, forcible approach", *forcible* could be **A) `জোরালো`** (forceful,
vigorous, emphatic) or **B) `বলপ্রয়োগমূলক`** (force-applying, i.e. coercive). B is a
literal rendering of "force" but shifts the meaning toward physical coercion, which the
source — describing an assertive problem-solving *style* stereotyped as male — does not
intend. Under **SEM/CON** I chose **A** `জোরালো`, which keeps the "forceful/assertive"
reading. For *approach* I used `পন্থা` (way/method of tackling) rather than দৃষ্টিভঙ্গি
(attitude/outlook), since the item is about *how* problems are tackled.

## Minor notes

- **PO higher/lower positions** → the compact standard adjectives `উচ্চপদস্থ` /
  `নিম্নপদস্থ` (high-/low-positioned), used uniformly across PO1–PO5.
- **UN3 "rules and regulations"** → `নিয়মকানুন`, Bengali's natural fixed pair, rather than
  the stiffer technical নিয়ম ও বিধি. "expected of me" is kept uniform as প্রত্যাশিত across
  UN1/UN3.
- **MA2 "intuition"** → `স্বজ্ঞা`, the precise term for intuition, over অন্তর্দৃষ্টি
  (insight) or অন্তর্জ্ঞান.
- **Scale anchors** use `দৃঢ়ভাবে` ("strongly/firmly") to match "strongly", with the
  natural agreement word একমত (lit. "of one mind"); the LT anchors use গুরুত্বপূর্ণ /
  গুরুত্বহীন (important / unimportant), the same stem carried by the items.
