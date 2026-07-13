# CVscale translation notes: English → Hindi

**Source language:** English · **Target language:** Hindi (हिन्दी)

Files written to `instruments/`:
- `cvscale-hi.tsv` — 26 items across the five groups
- `dimensions-hi.csv` — dimension names, English kept after " / "
- `scales-hi.csv` — Likert anchors (`पूर्णतः असहमत`…`पूर्णतः सहमत`; `अत्यंत महत्वहीन`…`अत्यंत महत्वपूर्ण`)

## Target-language characterization

- **Register / Sanskrit–Hindustani split.** Written Hindi ranges from a Sanskritized
  (शुद्ध) high register to an everyday Hindustani that shares much vocabulary with Urdu
  (Perso-Arabic loans). A scientific questionnaire calls for standard written Hindi
  (मानक हिन्दी). I kept to that register but avoided over-Sanskritized rarities, preferring
  words stable across the Hindi belt — e.g. महत्वपूर्ण (important), निर्देश (instructions),
  समूह (group). Fully naturalized loans that everyone understands (कायदे, करियर) were used
  where they read more naturally than a stiff Sanskrit coinage.
- **Derivational morphology → UNI is easy.** Shared Sanskritic stems let recurring source
  words map to one Hindi word: समूह (group) across all CO items, निर्देश (instructions)
  across UN1/UN2/UN5, प्रक्रिया (procedures) across UN2/UN4, सफलता (success) across
  CO4/LT5/LT6, लक्ष्य (goals) across CO5/CO6, कल्याण (welfare) across CO3/CO5, समस्या
  (problems) across MA2/MA3. The व्यक्ति stem also links the noun व्यक्ति (individuals) with
  the adjective व्यक्तिगत (individual), mirroring the source's own stem-sharing.
- **Grammatical gender — mostly sidesteppable.** Hindi forces gender agreement on verbs and
  adjectives, but the PO/UN/CO items use the generic plural लोग / व्यक्ति plus the
  gender-invariant modal चाहिए and infinitives (करना, लेने), so no natural gender surfaces.
  First-person UN1/UN3 use the agentless passive (मुझसे क्या अपेक्षा की जाती है), also
  neutral. Only the MA items name पुरुष (men) and महिला (women) and thus carry gendered
  verb forms — exactly as the source intends.

Overall the translation was largely clean: Sanskritic morphology honored UNI effortlessly
and the impersonal framing kept gender invisible outside MA. Three decisions were worth
flagging, all turning on connotation.

## 1. CO1 — "self-interest" (CON)

Variants for *self-interest*: **A) `निजी हित`** (personal/private interest) vs.
**B) `स्वार्थ`** (self-interest, but idiomatically *selfishness*). B is the single most
natural word and the direct dictionary match, but in ordinary Hindi स्वार्थ is distinctly
pejorative — it is the everyday word for "selfishness/being selfish". English "self-interest"
is only mildly negative-to-neutral (economists use it neutrally). Under **CON** I chose **A**
`अपने निजी हित`, which keeps the neutral valence and also lets हित echo the समूह-**कल्याण**
"group welfare" of CO3/CO5 as a self/group contrast without overstating it.

## 2. LT5 — "giving up today's fun" vs. CO1 "sacrifice" (CON / UNI)

The obvious verb for both "giving up" (LT5) and "sacrifice" (CO1) is `त्याग करना`. I
deliberately did **not** unify them. `त्याग` means *renounce / sacrifice* and carries a
noble, quasi-ascetic overtone — right for CO1's "sacrifice self-interest for the group", but
too heavy for LT5's light, neutral "giving up today's fun". The source uses two different
English words here, so **UNI** does not require one Hindi word, and **CON** actively favors
splitting them: I used `त्याग` in CO1 and the plainer `आज के आनंद को छोड़ना` (giving up /
forgoing today's enjoyment) in LT5. For *fun* I chose आनंद (enjoyment) over मज़ा (colloquial)
or सुख (comfort/ease), as the closest neutral fit for the thing foregone.

## 3. LT2 vs. LT3 — "persistence" / "steadiness and stability" (UNI / SEM)

These three near-synonymous notions risk an accidental UNI collision on the दृढ़ / स्थिर
roots. LT2 "persistence" → `दृढ़ता` (firmness/resolve), with the phrase using
`दृढ़तापूर्वक` (resolutely) — the source itself pairs "resolutely/persistence", so that stem
link is warranted. To keep LT3 "personal steadiness and stability" separate, I avoided दृढ़ता
there and used the स्था-root pair `स्थिरता` (steadiness) + `स्थायित्व` (stability/durability),
two distinct but naturally paired words. This preserves the source's distinction between LT2
(pressing on) and LT3 (being settled) rather than blurring them into one "firmness" cluster.

## Minor notes

- **UN3 "rules and regulations"** → `नियम और कायदे`. Hindi's cleanest fixed pair; the
  Sanskritic विनियम (regulation) was avoided as too technical and phonetically close to
  विनिमय (exchange).
- **MA1 "professional career"** → `पेशेवर करियर`, using पेशेवर (occupational "professional")
  rather than व्यावसायिक, which also reads as "commercial/business".
