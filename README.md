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

TeamCultureProfile
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

- review code of changes
- create_member: language switching does not work with unfilled form
- edit_member: visible comment on page?
- perform changes and close issues
- close parent issue #1
- load_scales() should check consistency of 'levels' with actual number of levels.
- show_team must display an absolute URL with host/port
- Breadcrumb navigation, edit links on show page
- forms: center labels below radio buttons, make buttons more visible (gray50)
- Evaluate HTTP header for default language
- superuser page and management command for getting its URL (fresh token each time)
- NOT NEEDED: forbid cookie separators in names
- add 'version' in cookie?


## Next step

We build an admin-page via which one can get back the teams and members links if
cookies are lost.

Introduce a model AdminPage, with token (str) as the only attribute.
Only one instance of this will ever exist.
It is created when the app's deployer calls
python manage.py cuhasc-adminpage
and the token initialized with a TOKEN_LENGTH_ADMINPAGE=20 random string.
If it exists already, that management command will set a new token each time.
It further prints the resulting full link to the admin page of the form
http://localhost:port/adminpage/<token>

The adminpage template shows a 
"home" link at the top,
followed by a heading "Teams and members",
followed by a two-level nested list of Teams and each team's members.
Teams are shown by their team name (link to show_team), "edit" link, "new member link" link.
Members are shown by their member name (link to show_member), "edit" link.
