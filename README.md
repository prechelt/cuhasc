# CuHaSc: Culture Handbook for Scrum

A simple webapp with which agile software development teams can determine their culture profile
and receive advice on plausible agile process execution problems that may arise from it.

Cuhasc is based on Python and Django. 
It uses SQlite3 as the RDBMS and Django's development webserver for HTTP
in order to provide the simplest possible deyployment.
The application itself is also kept extremely simple.


## 1. How it works

1. Culture Lead (often the Scrum Master) sets up a Culture Profiling process for one new Team in Cuhasc.
   (Technically, anybody can set up a new Team at any time.)
2. Cuhasc provides a joint URL for the Team Members to use.
3. Culture Lead sends URL to all Team Members.
   There are no accounts, just confidential tokens in URLs and a cookie that remembers them.
4. Each Team Member visits URL and fills in the Culture Profile Questionnaire.
   The questionnaire is available in 40 languages; Members should use their native language.
5. Cuhasc computes the member's Culture Profile, the team's Overall Culture Profile,
   and the resulting list of likely agile process execution problems.
   The handbook embedded in the app knows about many such problems and will show exactly
   those that are likely to apply to the given team.
6. Culture Lead discusses the individual execution problems with the team.

For the handbook content, see
[handbook/](handbook/).
Each file there is one examples of an agile process execution problem.


## 2. The science behind it

The culture profile is based on the famous 
[Hofstede dimensions](https://en.wikipedia.org/wiki/Hofstede%27s_cultural_dimensions_theory)
of national cultures.

The specific questionnaire used is the psychometrically validated 
[CVscale](https://www.tandfonline.com/doi/pdf/10.1080/08961530.2011.578059),
which transfers the Hofstede dimensions to the level of an individual 
(where Hofstede's original questionnaire applied only at the national level).

CVscale is originally avaiable in English.
The many translations provided here were worked out by 
[Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) 
instructed by a sophisticated 
[prompt](.claude/skills/translate-cvscale/SKILL.md)
that ensures that the meaning of each item is kept the same as much as possible
in each language, despite problems with different registers of language use,
unwanted term parallels or term variations,
lower or higher or different ambiguity of an otherwise-suitable term,
unwanted connotations of otherwise-suitable terms, and other subleties.

This is important, because the meaning of the Overall Culture Profile is well-defined only
if the questionnaire means the same to all members in all its cultural facets.
If you want to scrutinize the difficulties for your target language(s),
review the 
[translation notes](instruments/translation-notes).

The agile execution problems represented in the handbook were found by a
literature search through the rather extensive research literature on agile software development,
looking for those few of the many articles that describe problems with enough detail that they
can be traced to (likely) team-cultural causes.

TODO: The handbook provides pointers to the specific research articles underlying each handbook section.


## 3. Installation/deployment

- Cuhasc runs on any Linux, Windows or macOS system that has Python 3.12 or higher installed. 
- It is meant to be used by a single team only, but can also be used by several teams that trust each other.
- There are four modes in which you can install and run it:
  - 3.1: On a proper server that all users can reach.
  - 3.2: On your developer machine in a LAN if all Team Members are in that LAN and you have opened
    the firewall on your machine.
  - 3.3: On your developer machine, using `cloudflared` or `ngrok` for 
    making it visible as a pseudo-public server via a tunnel.
    This involves some (fairly simple) setup for the operator and uses the free tier of a commercial service.
    Drawback: The URL so-created remains valid only until the next reboot or even standby.
  - 3.4: On your developer machine, using `tailscale` for creating a private network for your team only.
    This involves some (reasonably simple) setup for each team member and 
    also uses the free tier of a commercial service.

### 3.0 Basic install

(TODO: flesh out)

- Python
- pipx(?)
- run: `python manage.py runserver 0.0.0.0:8037`

### 3.1 Running on a proper server

(TODO: flesh out)


### 3.2 Running on a developer machine in a joint LAN

(TODO: flesh out)


### 3.3 Running on a developer machine via `cloudflared` or `ngrok` tunnel (--> temporary public server)

(TODO: flesh out)


### 3.4 Running on a developer machine via a `tailscale` network (--> semi-permanent group-private server)

(TODO: flesh out)


## 4. Admin/superuser access

If you lost both your team-level URL and the cookie that stored it,
you can retrieve the URL by calling 
`python manage.py cuhasc-adminpage`.
It will print the path part of a URL. Append this to the homepage URL in your browser URL bar.
The page will show links to all objects in the database.


## 5. Next development steps

- form: should the scale run right-to-left in a RTL language?

