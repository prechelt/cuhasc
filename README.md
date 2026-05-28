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


## Analysis Model (to be moved farther down)

```
CultureLead
    name: str
    associates Team

TeamMember
    name: str
    associates Team

Team
    name: str
    associates TeamMembers
    associates CultureProfileQuestionnaire
    associates OverallCultureProfile

CultureProfile
    associates TeamMember
    remembered via a cookie

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
- ...

## Cookie

- Encapsulated in class `cookies.CuhascCookie` in `cuhasc/cookies.py`.
- Initialize as `CuhascCookie(request)`
- Add a `Team` or `Member` by `cookie.add(myteam)`, `cookie.add(mymember)`.
- Internal representation is one object per line as a semicolon-separated 3-tuple of `modeltype;id;token`,
  e.g. `Team;2;aow7ftmd7wn3`
- Serialize as `cookie.cookietext` property.
- Access Teams as `cookie.teams` property, which is a list of `Team` objects, retrieved by `id`.
  Add a `url` property to each that is the URL of the object's `edit_team` page.
  Add a `fullurl` property that is the corresponding URL with scheme and host/port.
  Note these in the property's doc comment.
- Likewise for `cookie.members`.



## Deployment

- Cuhasc is distributed as a single file
- It will often be run on a developer's development machine.
- ...


## Method details

### Scales to be used for the CVscale items

Long-term orientation: 1 = “very unimportant” to 5 = “very important” 

All others: 1 = “strongly disagree” to 5 = “strongly agree”


## Next development steps

- `show_team`, `edit_team`
- Model for `Member`
- `CuhascCookie`
- `create_member`, `show_member`, `edit_member`
- Model for `QResult`
- Form for `QResult`
- View for `QResult`
- I18N (discussion)

## Next development steps details

Create a view team_created. Redirect a successful POST from team_create to this view. 
Use the URL /team_created/{id}/{token}, where id is the id of the just-created Team and token is its token.
Render the page based on templates/cuhasc/team_created.html.
This template should show the following link: /team_member/{id}/{token}.


## Next step

The `verb_modeltype` naming convention is currently violated, 
e.g. `team_created` should be `show_team`.
Throughout the app, list the violations and the correct replacement names.
Let me sign them off.
Rename the respective elements.
