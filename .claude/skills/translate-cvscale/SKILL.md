---
description: Translate a CVscale questionnaire tsv file from English into some other language
---

Usage e.g. `/translate-cvscale cvscale-en.tsv cvscale-de.tsv`


# Overall meaning

Translate the contents of the existing input file `cvscale-en.tsv` ('en' is the ISO code for English,
the source language)
and write the not-yet-existing output file `cvscale-de.tsv` in the target language German,
recognizing the target language by the ISO code 'de' for Deutsch/German in the target file name.
Both files live in the `instruments/` directory.

The input file codifies the original CVscale questionnaire for determining a person's profile 
with respect to the five Hofstede cultural values dimensions.

Also translate the related files `dimensions-en.csv` (codifying the names of the Hofstede dimensions)
and `scales-en.csv` (codifying the levels of the ordinal scales used for the individual questionnaire items).


# File format for `cvscale-*.tsv`

Input and output file use the same tab-separated values (tsv) format with three columns
Item, Scale, Content (as declared by the header row, which remains untranslated).
The capital letters indicate the column names.

In each row (called "item"), Item and Scale remain untranslated.
Your task is translating each item, which specifically means translating its Content.

Each Item consists of a group code and a number, e.g.,
The Items PO1, PO2, PO3, PO4, PO5 together form group PO, which stands for the items 
of the Power Distance dimension.

There are five such groups:
PO: Power Distance,
UN: Uncertainty Avoidance,
CO: Collectivism (vs. Individualism),
LT: Long-term Orientation,
MA: Masculinity (vs. Femininity).


# Translation rules

When translating, always keep in mind the purpose of the items: Characterizing a person's preference
along one of the Hofstede dimensions, namely the one that is designated by the group.

Respondents answer each item on a five point scale.
For LT, this scale runs from 'very unimportant' to 'very important'.
For PO, UN, CO, and MA, it runs from 'strongly disagree' to 'strongly agree'.

Whenever you can think of two different translations A and B for the item,
apply the following rules for deciding which is better:

SEM: If A is closer to the semantic field of the group than B, use A.
The goal is that the sentence meaning stays within the dimension's conceptual scope.

AMB: If B posesses an ambiguity (of whichever type) that is not present in the source language version of the item, use A.

LAM: If B lacks an ambiguity (of whichever type) that is present in the source language version of the item, use A.

CON: Use whichever is closer to the source language version in terms of direction and strength 
of the positivity or negativity of its connotation, if any.

UNI: If several items in a group refer to the same concept and use the same word or word stem for it
in the source language, the translated items should also have this uniformity property.

In case you cannot follow all rules at once for a given item, use your best judgment.

Use the perspective of a native speaker of the source language for the source language version
and the perspective of a native speaker of the target language for the translated version.

If gender cannot be kept invisible, go for a gender-neutral form.
Keep the overall form of the Content as a complete sentence vs. a mere phrase.
Translate parenthetical glosses, if any.


# Procedural hint: Characterize the target language first

Before translating, briefly characterize how the target language differs from English
on the axes that stress the rules above, and let that analysis drive item-level choices:

- Register / variety split: does the written standard differ from everyday speech, or
  vary by region? Prefer wording stable across the varieties respondents span, so
  responses stay comparable.
- Derivational morphology: do shared roots/stems make UNI easy to honor — or easy to
  violate by accident, forging a link across items the source keeps separate?
- Polysemy / register layering: is the natural word likely to carry a classical,
  religious, or literary secondary sense English lacks? (AMB / LAM)
- Connotation & culture: for PO, CO, and MA especially, does ordinary usage load
  authority, group loyalty, or gender roles with a stronger positive or more obligatory
  valence than the neutral English? Match the source's valence, don't amplify it. (CON)
- Gender & honorifics: does grammar force gender or social-status marking English leaves
  unmarked? Seek neutral forms; fall back to convention consistently.


## File format for `dimensions-*.csv` and `scales-*.csv`

Translate these two according to the same rules as the main `cvscale-*.tsv` file.
The file format, however, is semicolon-separated CSV.

For `scales-*.csv`, there will be conventional translations in most languages, that are used
in scientific questionnaires. Use these.

For `dimensions-*.csv`, include not only the translated name of each dimension,
but keep the original name after a " / " separator as well (in the same field of course)
as shown in `dimensions-de.csv`.


# Reporting

When done, report the full name of the source and target languages,
and explain the two or three most difficult decisions in the translation process:
- Which Item?
- Which rule or rules made it problematic?
- Which variants A and B (and perhaps more) did you consider? What do they mean in English?
  Explain the subtlety involved.
- Which one did you select? Which argument did you find the most decisive for doing so?

If the translation was straightforward throughout (because the target language allows to
match each source item very well), say so instead of blowing up minor difficulties.


# Language-specific notes

# When translating into Arabic

