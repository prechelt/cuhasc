# CVscale translation notes: English → Tamil

**Source language:** English · **Target language:** Tamil (தமிழ்)

Files written to `instruments/`:
- `cvscale-ta.tsv` — 26 items across the five groups
- `dimensions-ta.csv` — dimension names, English kept after " / "
- `scales-ta.csv` — Likert anchors (`முற்றிலும் உடன்படவில்லை`…`முற்றிலும் உடன்படுகிறேன்`; `மிகவும் முக்கியமற்றது`…`மிகவும் முக்கியமானது`)

## Target-language characterization

- **Diglossia.** Tamil has a sharp split between formal written Tamil (செந்தமிழ்) and
  spoken Tamil, and the written standard is stable across Tamil Nadu, Sri Lanka, and the
  diaspora. A scientific questionnaire calls for the written standard, so I used it
  throughout (verb forms like `எடுக்க வேண்டும்`, `தீர்க்கின்றனர்`). This also keeps
  responses comparable across regions.
- **Agglutinative morphology → UNI is easy.** Shared roots let recurring source words map
  to one Tamil word: குழு (group) across all CO items, வெற்றி (success) across CO4/LT5/LT6,
  அறிவுறுத்தல் (instructions) across UN1/UN2/UN5, நடைமுறை (procedures) across UN2/UN4,
  சிக்கல் (problems) across MA2/MA3, இலக்கு (goals) across CO5/CO6.
- **Gender stays invisible.** Generic third-person plural (`உள்ளவர்கள்`, `தனிநபர்கள்`) is
  gender-neutral, so PO/UN/CO/LT needed no gender workarounds. Only MA items name men and
  women, as the source does.
- **Register/polysemy traps.** Several natural words carry a classical/religious secondary
  sense English lacks; those drove two of the decisions below.

Overall the translation was largely clean — Dravidian morphology honored UNI without effort
and the impersonal framing sidestepped gender. Three decisions were worth flagging.

## 1. PO3 — "social interaction" (AMB)

Variants for *social interaction*: **A) `சமூக ரீதியில் பழகுவது`** (interacting/mingling
socially, a verbal noun) vs. **B) `சமூகப் பழக்கம்`** (social association). B is the more
compact noun, but `பழக்கம்` is polysemous — it means *acquaintance/association* **and**
*habit/custom*. Reading PO3 with the "habit" sense ("should avoid the social habit of…")
is a genuine misreading the English "interaction" does not invite. Under **AMB** I chose
**A**: the verbal-noun form `பழகுவது` carries only the "mingle/associate" sense and blocks
the habit reading.

## 2. LT5 — "giving up today's fun" (AMB / CON)

Two traps here. For *giving up*: **A) `விட்டுக்கொடுத்தல்`** (giving up, conceding) vs.
**B) `துறத்தல்`** (renouncing). B is idiomatic but loaded with an ascetic/renunciant
(religious) overtone — `துறவு` is monastic renunciation — which the neutral English "giving
up" lacks; **AMB/CON** rule it out, so I used **A**. For *fun* I used `இன்பங்கள்`
(pleasures/enjoyments) rather than `மகிழ்ச்சி` (happiness, an emotional state): "fun" is
the thing foregone, closer to `இன்பம்` than to a mood.

## 3. CO1 — "self-interest" (CON)

Variants: **A) `தன்னலம்`** (self-interest) vs. **B) `சுயநலம்`** (selfishness). The two are
near-synonyms, but `சுயநலம்` leans distinctly pejorative ("selfishness"), which would
amplify the mildly negative-to-neutral valence of English "self-interest". Under **CON** I
chose **A** `தன்னலம்`, the less morally charged of the pair, and kept "group welfare"
(CO3/CO5) as `குழுவின் நலன்` so the shared நலன் root mirrors the self/group contrast
without forcing the source's separate words into one.

## Minor note

In LT2 (`உறுதியுடன்`, resolutely) and LT3 (`உறுதிப்பாடு`, steadiness) I let the shared
உறுதி ("firmness") stem stand. English "resolute"/"steadiness" are themselves near-synonyms,
so the link is semantically warranted rather than an accidental UNI violation.
