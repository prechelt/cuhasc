# CVscale translation notes: English → Portuguese

**Source language:** English · **Target language:** Portuguese (português)

Files written to `instruments/`:
- `cvscale-pt.tsv` — 26 items across the five groups
- `dimensions-pt.csv` — dimension names, English kept after " / "
- `scales-pt.csv` — conventional Likert anchors (`discordo totalmente`…`concordo totalmente`; `muito pouco importante`…`muito importante`)

## Target-language characterization

The dominant issue for Portuguese is the **European (pt-PT) vs. Brazilian (pt-BR) variety split**. The 1990 Orthographic Agreement unifies most spelling that used to diverge (`interação`, `objetivos`, `coletivismo` are now shared), so most items are variety-stable. What still splits the varieties is (a) a handful of lexical items (`planeamento`/`planejamento`), (b) clitic-pronoun placement (enclisis in pt-PT, proclisis in pt-BR), and (c) adverb placement. I targeted **European Portuguese as the ISO-`pt` base**, but wrote defensively so most items read naturally in both varieties, and I flag the genuine forks below.

Derivational morphology made UNI easy: shared stems let me keep `posições superiores/inferiores` uniform across all five PO items, `bem-estar` across CO3/CO5, `sucesso … no futuro` across LT5/LT6, and `objetivos` across CO5/CO6. Gender is grammatically forced but stays effectively invisible through the generic plural.

The translation was largely straightforward. Three decisions were worth flagging.

## 1. UN3 — "they inform me of what is expected of me" (variety-stable clitic)

The natural rendering of "inform me" needs an object clitic, and clitic placement is exactly where pt-PT (`informam-me`, enclisis) and pt-BR (`me informam`, proclisis) diverge — no single form is neutral. Variants: **A) `porque me esclarecem o que se espera de mim`** (restructure with a verb that keeps the sense — "because they clarify for me what is expected of me") vs. **B)** commit to one variety's clitic order (`informam-me` / `me informam`). I chose **A**: `esclarecer` preserves the "inform" sense while sidestepping the enclisis/proclisis fork entirely, keeping the item comparable across varieties. It also reuses the `o que se espera de mim` phrase from UN1 (UNI).

## 2. CO — "Individuals" (SEM vs. gender-neutrality)

Same dilemma as the Spanish notes. Variants: **A) `os indivíduos`** (generic masculine, unmarked) vs. **B) `as pessoas`** ("people," grammatically feminine but neutral in reference). The CO dimension is *Collectivism vs. Individualism*, and `indivíduo` sits squarely in that semantic field while `pessoas` dilutes it. I chose **A** on SEM; the generic-masculine plural keeps gender effectively invisible in the generic reading (Portuguese convention), and the `individ-` stem lets me honor UNI with `individuais`/`individual` in CO3/CO4.

## 3. LT4 — "Long-term planning" (variety fork with no neutral form)

Variants: **A) `Planeamento`** (pt-PT) vs. **B) `Planejamento`** (pt-BR). Unlike UN3, there is no restructuring that avoids the choice — the noun itself differs. This is the one item that genuinely can't be made variety-neutral. I chose **A** consistent with the European-Portuguese base; a Brazilian edition should read `Planejamento a longo prazo`. (`Padronizados` in UN4 is the milder analogue — understood pan-lusophone, though pt-PT also says `normalizados`.)

## Minor connotation checks

- **LT1 "Thrift" → `Poupança`** (saving), the positively-valenced virtue term, over `Frugalidade`, which risks an austerity/self-denial overtone the neutral English lacks (CON). Matches Spanish `Ahorro`, German `Sparsamkeit`.
- **LT2 "resolutely" → `com firmeza`** rather than the stronger `com determinação inabalável`, to match the source's strength (CON). "Persistence" gloss → `Persistência`.
- **UN2 "closely follow" → `seguir de perto`** rather than `seguir à risca` ("to the letter") / `seguir rigorosamente`, which overshoot the source's strength (CON) — same call as the Spanish `seguir de cerca`.
- **MA2** repeats "solve problems" in both clauses just as the source does (`costumam resolver os problemas …`), rather than using an object clitic in the second clause — this both mirrors the source's parallelism and avoids the pt-PT/pt-BR clitic fork.
