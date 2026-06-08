# CuHaSc: Culture Handbook for Scrum

A simple webapp with which software teams can determine their culture profile.

## Functional Requirements

### Roles

- Culture Lead: The person starting, leading, and moderating the process. (Often the Scrum Master.)
- Team Member (often shorter called Member): : Any person in the software development team, including the Culture Lead.
- Team: The set of all Team Members.

### Overview Usecase

1. Culture Lead sets up a Culture Profiling process for one new Team in Cuhasc.
2. Cuhasc provides a joint URL for the Team Members to use
3. Culture Lead sends URL to all Team Members
4. Each Team Member visits URL and fills in the Culture Profile Questionnaire.
5. Cuhasc computes the member's Culture Profile
6. Culture Lead shows and explains the Overall Culture Profile to the Team
(7. Cuhasc advises Team about likely consequences of its Overall Culture Profile)

### Usecase: Set up Culture Profiling

1. Culture Lead starts Cuhasc
2. Cuhasc offers to create a new Team
3. Culture Lead creates the Team and gives it a name
4. Cuhasc provides a unique non-guessable Team-URL
5. Culture Lead sends the Team-URL to all Team Members

### Usecase: Fill Culture Questionnaire

1. Team Member receives the Team-URL and visits it
2. Cuhasc shows Team name, asks for member name (or member pseudonym)
3. Cuhasc shows Culture Profile Questionnaire
4. Team Member fills in Culture Profile Questionnaire
5. Cuhasc stores member identity in cookie so the Team Member can revisit their data

### Usecase: View Culture Profile

...


## Analysis Model

```
CultureLead
    name: str
    associates Team

Member
    name: str
    associates Team

Team
    name: str
    associates Members
    associates CultureProfileQuestionnaire
    associates OverallCultureProfile

CultureProfile
    associates Member

CultureProfileQuestionnaire
    questions: list

OverallCultureProfile
    (aggregates the team's CultureProfiles)

```

## Non-Functional Requirements

- Cuhasc runs on any Linux, Windows or macOS system that has Python 3 installed. 


## Architecture

- Cuhasc is based on Python and Django
- It uses SQlite3 as the RDBMS.
- It obeys a `verb_modeltype` naming convention (e.g. `create_team`, `show_team`, `edit_team`) 
  for URLs, view names, view function names, template names, etc.
- It uses no user accounts, authentication, or explicit groups for teams etc.
  Rather, it relies on random tokens for authorization, 
  on the distribution of unguessable URLs via email for group formation, and
  on a cookie for keeping track of the unguessable URLs pertaining to a user.


## Deployment

- Cuhasc is distributed as a single file
- It will often be run on a developer's development machine.
- ...


## Method details

--

## Next development steps

- Internationalization/Localization (I18N/L10N)
  - cvscale.tsv -> cvscale-en.tsv
  - scales.csv -> scales-en.csv
  - instruments.py: load_scales(glob), load_questionnaires(glob), get_languages(), 
    get_questionnaire(name, language) 
  - translate cvscale
  - translate scales
- load_scales() should check consistency of 'levels' with actual number of levels.
- show_team must display an absolute URL with host/port
- NOT NEEDED: forbid cookie separators in names
- add 'version' in cookie?


## Next step

We want to perform I18N for the questionnaires. Do the following: 
1. Rename cvscale.tsv into cvscale-en.tsv. We will have many variants in different languages and
   the parts after the dash will form our languages list.
2. Rename scales.csv into scales-en.csv. Ditto. If the two languages lists thus formed are different,
   use their intersection.
3. in instruments.py, change load_scales(path) into load_scales(glob). Evaluate the glob pattern,
   read each file that matches. Extract the language from the filename as a possible entry for the languages list.
   Store the contents in a dictionary _scales (from ISO code to scales object) as a global variable.
4. change load_questionnaire(path) into load_questionnaires(glob) likewise. Global variable is _questionnaires.
5. introduce get_languages() that returns the intersection of the sets of language codes of these two.
6. Introduce a dataclass Item with fields (item, scale, content). 
7. add get_questionnaire(language) for retrieving a questionnaire as a list of Items. 
8. views.py: Eliminate _scales and _cvscale_items. Move the respective initialization to instruments.py.
   Modify the uses of these variables to call instruments.py instead.
