# Switch questionnaire language via a POST round-trip that preserves answers

On the questionnaire form pages (`create_member`, `edit_member`), changing the language
selector submits the form via POST with a marker distinguishing "switch language" from
"submit answers." The view then re-renders the form bound to the posted values in the new
language, suppressing validation errors, and writes the chosen language into the cookie.

This supersedes the README's earlier sketch of a GET `?lang=` round-trip / refresh.
The deciding factor is that a refresh would discard answers already entered, while a pure
client-side text swap would require embedding every language's text in the page and
duplicating the cookie format in JS. The POST round-trip preserves in-progress answers for
free (the radio `value="1..5"` inputs are language-independent; only labels change),
persists the language to the cookie in the same request, and keeps the cookie's JSON shape
owned solely by `CuhascCookie`. A merely-switching POST never shows validation errors;
only a real submit validates.

Initial render picks the language from the cookie, falling back to English. Evaluating the
HTTP Accept-Language header for the initial default is deferred (a separate README next-step).
