# CuHaSc: Culture Handbook for Scrum

A simple webapp with which software teams can determine their culture profile.

## Functional Requirements

### Roles

- Culture Lead: The person starting, leading, and moderating the process. Often the Scrum Master.
- Team Member: Any person in the software development team, including the Culture Lead.
- Team: The set of all Team Members.

### Overview Usecase

1. Culture Lead sets up a Culture Profiling process in Cuhasc.
2. Cuhasc provides a URL for the Team Members to use
3. Culture Lead sends URL to all Team Members
4. Each Team Member visits URL and fills in the Culture Profile questionnaire.
5. Cuhasc computes the culture profile
6. Culture Lead shows and explain the culture profile to the Team
(7. Cuhasc consults Team about likely consequences of its Culture Profile)

### Usecase: Set up Culture Profiling

1. Culture Lead starts Cuhasc
2. Cuhasc offers to create a new Team
3. Culture Lead creates the Team and gives it a name
4. Cuhasc provides a unique non-guessable Team-URL
5. Culture Lead sends the Team-URL to all Team Members

### Usecase: Fill Culture Questionnaire

1. Team Member receives the Team-URL and visits it
2. Cuhasc shows Team name, asks for member name (or member pseudonym)
3. Cuhasc shows Culture Questionnaire
4. Team Member fills Culture Questionnaire

### Usecase: View Culture Profile

...


## Non-Functional Requirements

- Cuhasc runs on any Linux, Windows or macOS system that has Python 3 installed. 



## Architecture

- Cuhasc is based on Python and Django
- It uses SQlite3 as the RDBMS.
- ...

## Deployment

- Cuhasc is distributed as a single file
- It will often be run on a developer's development machine.
- ...