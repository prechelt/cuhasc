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

(TODO: decide technical approach, implement, then flesh out description)

### 3.0 Basic install

This is required before each of the subsequent scenarios 3.1 to 3.4.

1. Install the `uv` package manager as described here: https://docs.astral.sh/uv/getting-started/installation/
   If you have some version of it already installed, that will likely work fine as well.
2. `uv tool install cuhasc`
3. Review the output of the following calls:
   - `cuhasc --help`
   - `cuhasc info`
   - `cuhasc run --help`
4. The DBMS is SQLite. This is built-in into Python, so no separate setup is needed at all.
   There is no DB setup step, either. 
   `cuhasc run` is how you start the webserver built into `cuhasc`  and you could do that now.
5. The data directory `~/.cuhasc/` (same path on all OSs) holds the database file `db.sqlite3` and
   the app-local `secret_key`. These files are the entire application state. 
   Back it up by copying it (or use `cuhasc backup` for a DB backup). 
   It survives upgrades and uninstalls.
6. Upgrade `cuhasc` with `uv tool upgrade cuhasc` when desired.
   Database migrations run automatically at every application start.


### 3.1 Running on a proper server

- Simplest: `cuhasc run` as in the basic install, just on a server computer rather than a developer notebook.
  Make sure the port you use is open in the server's firewall.
- The professional variant: 
  `cuhasc run` with a reverse proxy (Apache, nginx, ...) in front that terminates TLS.
  Cuhasc speaks plain HTTP only; encryption is always somebody else's job.
- Alternative: serve `cuhasc.wsgi:application` under gunicorn or another WSGI server.
  Then `CUHASC_HOME` (default: `~/.cuhasc/`), 
  `CUHASC_SECRET_KEY` (a fixed random string), and 
  `CUHASC_ALLOWED_HOSTS` (comma-separated list of target hostnames allowed in requests)
  must be set explicitly (because `cuhasc run` is what otherwise supplies them).
  More complicated, hence recommended only if you have a good reason for it.

Set up a minimal `systemd` unit so the server survives a reboot.

Only one running instance is allowed per data directory.


### 3.2 Running on a developer machine in a joint LAN

- `cuhasc run` and nothing else: it binds all interfaces on port 8037 by default.
- Open the firewall for that port. 
  On Windows, the first start will raise a Windows Defender dialog; 
  `cuhasc` must be allowed for *private* networks.
- Hand the Team Members the "on this LAN" URL that the start-up banner prints.
- No `--public-url` needed here: plain HTTP within one LAN needs no extra configuration.

Be aware that everybody on this LAN can in principle read all traffic to and fro this server now.


### 3.3 Running on a developer machine via `cloudflared` or `ngrok` tunnel (--> temporary public server)

- Install `cloudflared`:
  https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/  
  We will use the 
  ["trycloudflare" free tier](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/).
- _First_ start the tunnel, which prints its public URL immediately:
  `cloudflared tunnel --url http://localhost:8037` or `ngrok http 8037`.
- _Only then_ start cuhasc with that URL:
  `cuhasc run --host 127.0.0.1 --public-url https://<the-printed-cloudflared-url>`.
- `--public-url` is not optional: the tunnel terminates TLS, so the browser
  reports an https origin that Django would otherwise not recognize, and every form submission 
  would fail with a 403.  
  `--host 127.0.0.1` keeps the app off the LAN because the tunnel is meant to be the only way in.

This setup is great if all team members fill the questionnaire within the same half-day or so.
It is inconvenient otherwise:
The URL dies at the next reboot or standby of your "server" machine. 
Both commands above must then be repeated and the hostname will have changed,
so all links need to be sent out again.

`ngrok` uses a similar concept, see here: https://ngrok.com/


### 3.4 Running on a developer machine via a `tailscale` network (--> semi-permanent group-private server)

If you intend to use `cuhasc` for some longer time, this approach may be preferable.
It requires more setup, but produces less hassle then.

- Each Team Member installs tailscale and joins the tailnet, see here:
  https://tailscale.com/docs/how-to/quickstart
- `cuhasc run --public-url http://<machine>.<tailnet>.ts.net:8037`.
- In contrast to the `cloudflared` apporach, the hostname is stable, so the links keep working across reboots.


## 4. Admin/superuser access

If you lost both your team-level URL and the cookie that stored it,
you can retrieve the URL by opening the "admin page" that is indicated in the 
start message of any `cuhasc run` call.

### TODO in README: install section

```
 # Windows — no Python needed; uv brings its own
 powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
 uv tool install cuhasc
 cuhasc run
 # Linux / macOS
 curl -LsSf https://astral.sh/uv/install.sh | sh     # or use pipx, if you have it
 uv tool install cuhasc
 cuhasc run
```

 Individual commands rather than a .ps1: a script you distribute needs unblocking or an execution-policy
erride anyway, cannot be cheaply signed, and is opaque to the person running it — three visible
 lines are auditable and far easier to support over email.

### TODO in README: other

Intro ¶3: "uses Django's development webserver" is no longer true.
§1: the handbook link moves to cuhasc/data/handbook/. §2: the instruments/translation-notes
nk is deliberately unchanged — worth saying so, so nobody tidies those files into the package.
 - §3.0: flags and env vars; where ~/.cuhasc is and that db.sqlite3 + secret_key are the
 entire application state (back up that folder; cuhasc backup for a live copy).
 - §3.1: cuhasc run behind nginx, or cuhasc.wsgi:application under gunicorn — the latter
 needs CUHASC_HOME, CUHASC_SECRET_KEY, CUHASC_ALLOWED_HOSTS set explicitly.
 - §3.2 LAN: cuhasc run binds 0.0.0.0:8037; open the firewall — on Windows the first run
 raises a Defender dialog that must be allowed for private networks; share the printed LAN URL.
§3.3 tunnel: the order matters — start the tunnel, copy the URL, then cuhasc run --host 127.0.0.1 --public-url https://…. Omitting --public-url kes every form submission fail with
 403; --host 127.0.0.1 keeps the app off the LAN when only the tunnel should reach it.
 - §3.4 tailscale: --public-url http://<machine>.<tailnet>.ts.net:8037.
 - New "Upgrading and backing up": uv tool upgrade cuhasc; migrations run on the next
 cuhasc run; ~/.cuhasc survives.
§4: python manage.py cuhasc-adminpage → cuhasc adminpage; it now prints a complete URL,
 not a path to paste after the homepage, and cuhasc run prints the current link at startup.
 Retitle — there is no superuser and no Django admin.
 - §5: move runserver under a "Development" heading with poetry install and pytest.

### New ADR 003

New ADR (docs/adr/0003-installable-app-and-trust-model.md) — three non-local decisions that
 will look like bugs to a future reader: ALLOWED_HOSTS = ['*'] and why the token model makes it
fe here; mutable state outside the install tree with settings that never write; and waitress
l_scheme='https' rather than SECURE_PROXY_SSL_HEADER as what actually makes tunnel mode work.
 Also worth revisiting ADR-0001's "distributed as a single file" NFR — a wheel is a single file,
 but the sentence reads like a self-contained executable, so it should say what is now true.

### Risks

- Waitress header stripping (verified: clear_untrusted_proxy_headers defaults to True as of
3.0.0) — mitigated by url_scheme, but it only manifests as a browser 403 behind a real tunnel,
never in curl. Test it there before releasing.
The .gitignore handbook trap — guarded by the wheel-content grep above.
- Whitenoise finders mode is the one design choice I could not exercise here (whitenoise is not
installed in your venv). The Step 4 test is the gate; the fallback is one setting plus one line.
- Your existing data does not move. /ws/gh/cuhasc/db.sqlite3 stays the checkout's database; an
installed cuhasc starts empty in ~/.cuhasc. cp db.sqlite3 ~/.cuhasc/ if you want it.
- One instance per data directory — two cuhasc run on the same ~/.cuhasc will hit sqlite
database is locked. Use --data-dir for a second.
- Bootstrap comes from the jsdelivr CDN (cuhasc/templates/cuhasc/base.html:14,26), so an
air-gapped LAN or tailscale deployment renders unstyled. Not caused by this change but exposed by
it; vendoring Bootstrap into cuhasc/static/cuhasc/vendor/ costs ~250 KB in the wheel and
deserves its own ADR. Flagging, not doing.
- cuhasc/templates/cuhasc/show_team.html prints the member link as a relative path in the link
text, so a Culture Lead who copies the text gets /create_member/1/abc…. cuhasc/cookies.py:86,108
already compute a fullurl via build_absolute_uri that no template uses. One-line fix, and it
only yields the right scheme once Step 3 and Step 6 are in place.
- The admin URL is printed on every cuhasc run and grants read access to every Team, Member
and answer — it lands in scrollback, tmux logs and journals. Recovery is the documented use case
so I would keep it, but record the trade-off in the ADR.

### Deliberately not in scope

 Trimming django.contrib.{admin,auth,contenttypes,sessions,messages} from INSTALLED_APPS. The
 admin URL has been commented out since forever, cuhasc/admin.py is an empty stub, and nothing
 reads request.session or uses messages — but the gain is a few unused tables (the admin's 1.8 MB
 of static assets live in the Django wheel, not ours), and the change is unrelated to packaging. If
 you want it, it is cleanly separable and belongs after everything above is green.