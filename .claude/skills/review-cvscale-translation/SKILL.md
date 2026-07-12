---
description: Check the adequacy of a CVscale questionnaire translation
---

Usage e.g. /translate-cvscale cvscale-en.tsv cvscale-de.tsv 

Find and read the definition of the 'translate-cvscale' skill, but do not perform these actions right now.
Find and read the source files and target files given as arguments to the present skill call.
The target files were produced by 
`/translate-cvscale cvscale-en.tsv cvscale-de.tsv` or similar.

Check the quality of the translation:
Consider each item and check whether rules SEM, AMB, LAM, CON, and UNI have been obeyed properly.
They have not been obeyed properly if (and only if) you can think of a different translation that is clearly better.
Report such cases. Provide an argument why your proposal is superior.

If this list of translation mistakes comes out empty (and only then), 
report items where the translation is at least questionable. Explain why.

Write the report into `instruments/translation-reviews/review-en-de.md` 
(using the ISO codes of source language and target language).
