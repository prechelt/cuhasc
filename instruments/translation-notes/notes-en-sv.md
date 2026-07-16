# CVscale translation notes: English → Swedish

**Source language:** English · **Target language:** Swedish (svenska)

Files written to `instruments/`:
- `cvscale-sv.tsv` — 26 items across the five groups
- `dimensions-sv.csv` — dimension names, English kept after " / "
- `scales-sv.csv` — conventional Likert anchors (`instämmer inte alls`…`instämmer helt`;
  `mycket oviktigt`…`mycket viktigt`)

Swedish is a North Germanic language and a close sibling of the Danish already in this set;
the Danish translation was the primary cross-check, with German and Dutch as further structural
references.

## Target-language characterization

- **Register / variety split.** Written Swedish (*rikssvenska*) is highly uniform. Finland-Swedish
  shares the same written standard, so no regional written split affects these items. The formal
  address pronoun *ni* is effectively dead in questionnaire register after the *du*-reform, and in
  any case PO, CO and MA are framed impersonally in the third person; only UN1 and UN3 speak in the
  first person, where *vad som förväntas av mig* is register-neutral.
- **Derivational morphology.** Swedish compounds as freely as German and Danish (*grupplojalitet*,
  *arbetsrutiner*, *egenintresse*), which makes UNI cheap to honor but equally easy to violate by
  welding two source-distinct concepts into one stem. Watched for this in CO2 vs. CO6 and in the
  UN "instructions/procedures" pair.
- **Polysemy / register layering.** Low overall; Swedish has no classical or religious lexical
  layer of the kind that complicates the non-European languages here. The one live trap is modern,
  not archaic: *välfärd* (see CO3), captured by the welfare state exactly as Danish *velfærd* is.
- **Connotation & culture.** Sweden sits at the extreme low end of Hofstede's Power Distance scale,
  and the flat-hierarchy norm is culturally explicit (*Jantelagen*, shared with Denmark). As in the
  Danish notes, a verb of even moderate force in PO (*motsäga* "contradict", *ifrågasätta* "call
  into question") reads as markedly confrontational rather than neutral, so CON pushed toward the
  mildest literal option in PO4.
- **Gender & honorifics.** Swedish marks gender lexically on many nouns but not on *personer* or
  *individer*, so PO, UN and CO stay gender-invisible with no effort. MA1–MA4 name genders in the
  source, so nothing is added there.

Swedish is a high-resource language and no capability caveats apply. The translation was largely
straightforward; three decisions were worth flagging.

## 1. CO3 / CO5 "welfare of the group" (AMB)

The single hardest item, and the trap is identical to the Danish one. The literal cognate of
*welfare* is **välfärd** — but in modern Swedish *välfärd* has been almost entirely captured by
the welfare state (*välfärdsstaten*, *välfärdssamhället*, *välfärdstjänster*). "Gruppens välfärd"
would make a Swedish respondent hear public provision and social benefits, an ambiguity the neutral
English "group welfare" does not carry at all (AMB).

Variants: **A) "gruppens väl"** (the group's good/wellbeing) vs. **B) "gruppens välfärd"** (the
group's welfare) vs. **C) "gruppens bästa"** (the group's best interest) vs.
**D) "gruppens välbefinnande"** (the group's felt wellbeing). B carries the welfare-state reading
and was rejected outright. D denotes felt, personal comfort and is used of individuals, so
"gruppens välbefinnande" is close to a category error. C is the most idiomatic of the four and
reads perfectly naturally, but it shifts a *state* ("welfare") into an *interest* ("what is best
for"), slightly reframing CO3's comparison — the source weighs a condition of the group against
individual rewards, not a preference.

Chose **A**. *Väl* is the exact counterpart of German *Wohl* / Danish *vel* and survives in current
Swedish set phrases (*för allas väl*, *för landets väl*, *till gagn och väl*); it is faintly formal
but well inside questionnaire register, keeps the state-noun form, and is free of the welfare-state
reading. Avoiding an ambiguity the source lacks (AMB) was decisive over C's greater naturalness.
Used identically in CO3 and CO5, mirroring the source's own repetition (UNI).

## 2. PO4 "disagree with decisions" (CON)

Variants: **A) "inte vara oense med de beslut"** (not be in disagreement with the decisions) vs.
**B) "inte motsäga beslut"** (not contradict decisions — the route German took with *widersprechen*)
vs. **C) "inte ifrågasätta beslut"** (not call decisions into question) vs. **D) "inte motsätta sig
beslut"** (not oppose/resist decisions). B, C and D are all syntactically lighter and more idiomatic,
but each shifts from *holding* a dissenting view to *voicing or acting on* it — a real strengthening.
As the characterization notes, that strengthening costs more against Sweden's flat-hierarchy norm:
*motsäga* / *ifrågasätta* / *motsätta sig* read as openly confrontational, so they would have
respondents rating a harsher proposition than the English "disagree". A is a little heavier after
"bör inte", but it preserves the mild "holding a different view" sense exactly. Chose **A**, with CON
decisive over naturalness. (Note the double-negative trap avoided here: "not agree", *inte hålla med*,
would have inverted the item — the source says "not disagree", i.e. should comply, so the verb had to
carry "disagree", not "agree".)

## 3. CO2 "stick with the group" (UNI / SEM)

CO6 is *precisely* the loyalty item ("Group loyalty should be encouraged…"), and the source keeps
CO2 and CO6 lexically apart. German pulls them together (*der Gruppe treu bleiben*), collapsing two
distinct items; Danish deliberately did not, and neither do I (UNI applied negatively).

Neutral options: **A) "hålla fast vid gruppen"** (hold on to / stick with the group) vs.
**B) "stanna kvar i gruppen"** (stay in the group) vs. **C) "hålla ihop med gruppen"** (stick
together with the group) vs. **D) "vara solidarisk med gruppen"** (be in solidarity with the group).
D imports a solidarity nuance the plain "stick with" lacks and drifts toward the loyalty field of
CO6. C carries a mutual-cohesion nuance ("hold together") rather than the individual's adherence the
source describes. B (the Danish choice, *blive i gruppen*) is unambiguous but marginally weaker than
"stick with". A takes both abstract and collective objects comfortably in Swedish (*hålla fast vid
ett beslut*, *hålla fast vid gruppen*), matches "stick with" closely, stays squarely in the
Collectivism field (SEM), and remains lexically distinct from CO6's *grupplojalitet*. Chose **A**.

## Structural / uniformity notes

- PO1–PO5 keep a fixed frame: "personer i högre positioner" / "personer i lägre positioner",
  mirroring the source's verbatim repetition. *Positioner* keeps the source's generality; the
  narrower *tjänster/befattningar* ("posts") and *överordnade/underordnade* ("superiors/
  subordinates") were rejected as adding a workplace or direct-reporting specificity the general
  English "positions" lacks (LAM/SEM). Paired with **personer** (not *människor*, which foregrounds
  humanness, nor colloquial *folk*), following de *Personen* / da *personer*.
- PO1 "consulting" → *rådfråga* and PO2 "ask the opinions of" → *fråga … om deras åsikter* are kept
  lexically distinct, as in the source.
- PO3 "social interaction" → *socialt umgänge* (de *sozialer Umgang*, da *social omgang*).
- "instructions" stays a standalone *instruktioner* across UN1, UN2 and UN5, preserving the source's
  within-group repetition. UN5 "instructions for operations" → *Instruktioner för arbetet*; the
  compound *driftinstruktioner* was rejected as plant/machinery-specific.
- UN2 "procedures" → *rutiner* and UN4 "work procedures" → *arbetsrutiner* share the *rutin* stem,
  mirroring the source's shared "procedures" (UNI).
- "what I'm expected to do" (UN1) and "what is expected of me" (UN3) both become *vad som förväntas
  av mig* — the source varies only syntactically.
- "Individuals" is *individer* throughout CO1/CO2/CO5, preserving the stem link to *individuella
  belöningar* (CO3) and *individuell framgång* (CO4) that the source has via individual/individuals.
  The more idiomatic *den enskilde* would have broken that link.
- "success" is *framgång* everywhere it recurs (CO4, LT5, LT6); "success in the future" is
  identically *framgång i framtiden* in LT5 and LT6.
- CO2's *svårigheter* deliberately shares the *svår* stem with MA3's *svåra problem*, because the
  source shares one too (difficulties / difficult).
- "usually" is *vanligtvis* in both MA2 and MA3 (UNI).
- MA4 "jobs" → *arbetsuppgifter*, reading "jobs" broadly as tasks (cf. da *opgaver*, nl *taken*,
  fr *tâches*). Swedish *jobb* was rejected as the occupational slot, and *yrken* ("professions")
  as it would collide with MA1's *yrkeskarriär*. The overlap with PO5's "tasks" (*uppgifter*) is
  cross-group, so UNI does not forbid it, and the source's own "tasks"/"jobs" are near synonyms.
- MA1 "professional career" → *yrkeskarriär*. *professionell karriär* also exists; the amateur/pro
  ambiguity of *professionell* is present in the English "professional" too, so AMB is not engaged,
  and *yrkeskarriär* was chosen simply as the more natural, unambiguous Swedish.
- LT glosses: "Thrift" → **Sparsamhet**, the saving-as-virtue term, over *snålhet* (stinginess,
  negative) and *njugghet* (miserliness), matching de *Sparsamkeit* / da *Sparsommelighed* (CON).
  "Persistence" → **Ihärdighet** (tenacity/perseverance, positive), chosen over *uthållighet*
  (physical endurance, the counterpart of da's rejected *udholdenhed*) and *envishet* (stubbornness,
  negative).
- LT3 "steadiness" → *stadga* (steadiness of character), which overlaps somewhat with LT2's
  *ihärdighet* — but the source's own "steadiness"/"persistence" overlap to the same degree.
- LT2, LT5 and LT6 use a uniform "Att + infinitive" phrase form; LT1, LT3 and LT4 are noun phrases,
  exactly as in the source. The parenthetical glosses in LT1 and LT2 are translated.
- Item form is preserved throughout: PO/UN/CO/MA are complete sentences, LT items are bare phrases.
- `scales-sv.csv`: *instämmer inte alls* / *instämmer helt* is the conventional Swedish Likert pair
  in scientific questionnaires (the direct counterpart of fi *täysin eri mieltä* / *täysin samaa
  mieltä*). For the importance scale, the bipolar *mycket oviktigt* / *mycket viktigt* was kept,
  since the source scale is bipolar.
- `dimensions-sv.csv` uses the established Swedish Hofstede terms: *maktdistans*,
  *osäkerhetsundvikande*, *kollektivism*, *långsiktig orientering*, *maskulinitet*.

## Confidence

Swedish is a high-resource language, structurally close to English and very close to Danish, German
and Dutch, all available as cross-checks. No capability caveats apply. The point a native reviewer
should look at first is CO3/CO5 *gruppens väl*: the choice is deliberate and defended above, but
*väl* is the most formal register note in the instrument, and a reviewer may prefer *gruppens bästa*
if naturalness is weighted over the state/interest distinction.
