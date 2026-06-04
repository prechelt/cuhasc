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

### Scales to be used for the CVscale items

Long-term orientation: 1 = “very unimportant” to 5 = “very important” 

All others: 1 = “strongly disagree” to 5 = “strongly agree”


## Next development steps

- scales.csv, cvscale.tsv
- Model for `QResult`
- Form for an entire questionnaire set of `QResult`
- View for `QResult` (extension of create_member/edit_member)
- I18N (discussion)
- show_team must display an absolute URL with host/port
- NOT NEEDED: forbid cookie separators in names

## Next development steps details

--

## Next step

Next we want to extend create_member and edit_member by a questionnaire form (below what is already there).
The questionnaire to be used is that from cvscale.tsv, but we want to be able to use arbitrary questionnaires with the
mechanism we will build, so make this a parameter.

Column "Scale" in cvscale.tsv refers to a row from the semicolon-separated scales.csv:
column 1 is the scale name, column2 is the number of levels of this (ordinal) scale, columns 3 and up are the text labels
for these levels (many of them blank).

The form, called QuestionnaireForm, should show these text labels at radio buttons displayed horizontally.
The data values returned by these radio buttons are always 1, 2, 3...
Create a Model QResult that stores member, Item name, scale name, and response scale value for one questionnaire item.
Build a Form dynamically with as many items as rows in the questionnaire file (cvscale.tsv in our case).
Each item is mandatory.
Store questionnaire results in QResult rows in the database.
