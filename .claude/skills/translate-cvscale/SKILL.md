---
description: Translate a CVSCALE questionnaire tsv file from English into some other language
---

Usage e.g. /translate-cvscale cvscale-en.tsv cvscale-de.tsv


# Overall meaning

Translate the contents of the existing input file cvscale-en.tsv ('en' is the ISO code for English,
the source language)
and write the not-yet-existing output file cvscale-de.tsv in the target language German,
recognizing the target language by the ISO code 'de' for Deutsch/German in the target file name.

The input file codifies the CVSCALE questionnaire for determining a person's profile 
with respect to the five Hofstede cultural values dimensions.


# File format

Input and output file use the same tab-separated values (tsv) format with three columns
Item, Scale, Content (as declared by the header row, which remains untranslated).

In each row (called "item"), Item and Scale remain untranslated.
Your task is translating each item, which specifically means translating its Content.

Item consists of a group code and a number, e.g.,
Items PO1, PO2, PO3, PO4, PO5 together form group PO, which stands for the items 
of the Power Distance dimension.

There are five such groups:
PO: Power Distance,
UN: Uncertainty Avoidance,
CO: Collectivism (vs. Individualism),
LT: Long-term Orientation,
MA: Masculinity (vs. Femininity).


# Translation rules

When translating, always keep in mind the purpose of the items: Characterizing a preference
along one of the Hofstede dimensions, namely the one that is designated by the group.

Whenever you can think of two different translations A and B for the item,
apply the following rules for deciding which is better:

SEM: If A is closer to the semantic field of the group than B, use A.

AMB: If B posesses an ambiguity that is not present in the source language version of the item, use A.

LAM: If B lacks an ambiguity that is present in the source language version of the item, use A.

CON: Use whichever is closer to the source language version in terms of direction and strength 
of the positivity or negativity of its connotation, if any.

UNI: If several items in a group refer to the same concept and use the same word or word stem for it
in the source language, the translated items should also have this uniformity property.

Use the perspective of a native speaker of the source language for the source language version
and the perspective of a native speaker of the target language for the translated version.


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
