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

- /review-cvscale-translation by GPT-5.4 and Sonnet 4.6 -> 
  git show 186580bf     after review by GPT 5.4
  git show b942053b1    after review by Sonnet 4.6
- translate scales  -> scales-de.csv
- install Matt Pocock skills
- add language selection pulldown:
    - language mapping (i18n.py): code -> (name, rtl_flag)
    - URL param (sets cookie), fallback to cookie, fallback to English
    - using pulldown -> write cookie, refresh
- load_scales() should check consistency of 'levels' with actual number of levels.
- show_team must display an absolute URL with host/port
- NOT NEEDED: forbid cookie separators in names
- add 'version' in cookie?


## Next step

We have two functional areas open:

1. L10N of the questionnaire forms based on the `i18n.py` module and the different language versions
of `cvscale-*.tsv` and `scales-*.csv` in `instruments/`: 
The respective forms pages should show a language selector pulldown at the top. 
Using it should immediately update the page with the questionnare (but not the rest of the page)
in the chosen language. 
The setting is also stored in the cookie and used as the default for future visits of any such page.

2. Questionnaire evaluation and display at the individual level and team level.
Individual evaluation means computing the mean for each items group of QResults, resulting in 5 values in the
interval [1,5].
Displaying this means showing a plot with an [1,5] x-axis
and five thin gray lines with x=1..5 at y=1 to y=5 that each show one fat blue dot for the user's group mean
for that group and show a group (Hofstede dimension) label.
Team evaluation means collecting the individual evaluations for all members of a team.
Displaying this means showing a plot like for individuals but with a smaller dot for each invidual
on each line plus a larger one for the group mean.
We need to decide whether to use matplotlib for the plots or some JavaScript solution.
(We will later add more explanatory elements to this plot, because we need to attach
handbook sections to certain constellations of results.)
