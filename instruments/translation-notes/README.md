# CVscale translation notes

## Translation method

These translations were produced fully automatically by an LLM,
specifically Claude Opus 4.8 called via Claude Code as  
`/translate-cvscale cvscale-en.tsv cvscale-<targetlanguage>.tsv`

The translation instructions are provided in file
`.claude/skills/translate-cvscale/SKILL.md`.


## Important technical terms used in the translation notes

### "register"

_Opus 4.8 explains the term as follows:_  
The standard definition comes from Halliday: 
**register is language variation according to use,** 
contrasted with dialect, which is variation according to user. 
Your dialect is a property of who you are; your register is a property of the situation you're in. 
A single speaker commands many registers and normally only one or two dialects.

Halliday decomposes any situation into three parameters that jointly predict the register:

- **Field** — the social action underway and its subject matter (what's being talked about, and to what end).
- **Tenor** — the relations among participants: relative status, social distance, degree of formality.
- **Mode** — the role language is playing: spoken/written, planned/spontaneous, 
  constitutive of the action or ancillary to it.

The important technical refinement, from Biber's corpus work, is that 
**registers are probabilistic, not categorical**.
They're distinguished by the relative frequencies of ordinary linguistic features — pronoun density, 
passives, nominalization rate, subordination — not by features unique to them. 
There's no word that only occurs in legal register; there are words massively overrepresented there. 
This is what makes register empirically tractable: it's a distributional fact about texts, 
measurable by feature counts, which is why Biber's multidimensional analysis can locate texts in 
a feature space rather than sorting them into bins.

