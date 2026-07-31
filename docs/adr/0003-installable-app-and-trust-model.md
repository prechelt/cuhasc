# Run as an installed application: permissive hosts, external state, declared URL scheme

CuHaSc is installed with `uv tool install cuhasc` and started with `cuhasc run`,
by a Culture Lead who is not a developer and has no source checkout. That forces three
decisions which, read out of context, all look like mistakes a careful reviewer should fix.
They are deliberate, however, and undoing any of them breaks a deployment mode.


## `ALLOWED_HOSTS = ['*']` by default

`cuhasc.deployment.allowed_hosts()` answers for any host name unless `CUHASC_ALLOWED_HOSTS`
says otherwise.

This is safe here because the Host header guards nothing in CuHaSc. There are no accounts and
no login; access to a Team or a Member is by unguessable token in the URL path, plus a cookie
that remembers it. Nothing sends mail, and no security-relevant absolute URL is derived from
the Host header. The usual reason to restrict `ALLOWED_HOSTS` — an attacker poisoning a
password-reset link or a cache key — has no counterpart in this application.

It is also necessary, because none of the deployment modes in README §3 can enumerate its host
names in advance: a LAN address depends on the network the laptop happens to be on, a
`trycloudflare` URL is different on every run, and a tailscale name varies per tailnet. A
restrictive default would produce a `DisallowedHost` error at the first Team Member who opens
the link. 
A public server (mode 3.1) is the one case where the host names *are* known, 
and that is what `CUHASC_ALLOWED_HOSTS` is for.


## `manage.py check --deploy` warnings

The command reports `W004` (HSTS), `W008` (SSL redirect), `W012` and `W016` (secure-only cookies). 
All four are TLS settings, and CuHaSc never terminates TLS, only a tunnel or a reverse proxy does. 
Setting any of them would break the plain-HTTP LAN mode outright. 
They stay unset on purpose; the four warnings are the expected output, not a backlog.


## Mutable state lives outside the install tree, and the settings never write

The database and the generated secret key live in `~/.cuhasc/` — the same path on Linux, macOS
and Windows — or, when running from a source checkout, in the checkout itself. `cuhasc.deployment`
distinguishes the two by looking for `manage.py` next to the package, which exists in a checkout
and never in an installed copy.

State must be outside the install tree because `uv tool upgrade` replaces that tree wholesale. 
A database under `site-packages` would be destroyed by the first upgrade.

The same fixed path on all three operating systems was chosen over the platform-standard directories
(`~/.local/share`, `~/Library/Application Support`, `%LOCALAPPDATA%`) so that one backup
instruction fits every user: copy that one folder.

`cuhasc.deployment` only reads; `cuhasc.cli._create_data_dir()` is the only code that creates
the directory and writes the key. This split matters because settings modules get imported by
pytest, by `manage.py check`, by `django-admin`, and by any WSGI host — a settings module that
created directories and generated keys would do so in all of those situations. In particular, a
key invented per process would invalidate every CSRF token currently sitting in a browser, so a
Team Member halfway through the questionnaire could fail on submit. An installed deployment with
no key file and no `CUHASC_SECRET_KEY` therefore raises `ImproperlyConfigured` and refuses to
start, rather than inventing one.

The checkout marker also keeps development on the database next to `manage.py`, so that
installing CuHaSc does not silently relocate a developer's existing data to `~/.cuhasc`.


## Tunnel mode works through waitress' `url_scheme`, not `SECURE_PROXY_SSL_HEADER`

When `--public-url` is an https URL, `cuhasc run` passes `url_scheme='https'` to
`waitress.serve()`.

The textbook approach (setting `SECURE_PROXY_SSL_HEADER` and letting the proxy send
`X-Forwarded-Proto`) does not work under waitress. Since version 3.0 its
`clear_untrusted_proxy_headers` defaults to `True`, so waitress strips `Forwarded` and every
`X-Forwarded-*` header arriving from a peer that is not a configured `trusted_proxy`. Django
never sees the header, `request.is_secure()` stays false, the browser's `https://…` Origin fails
to match the scheme Django believes it is serving, and `CsrfViewMiddleware` rejects **every**
POST with 403: creating a Team, submitting the questionnaire, switching the language. The
symptom is nasty because the site loads perfectly and then simply refuses to do anything.

Declaring the scheme was preferred over `trusted_proxy='*'`, which would restore the header but
also let any client assert that its own connection was encrypted. Stating the scheme trusts no
client input at all and needs no proxy address.

The consequence is that `url_scheme` applies to every request, so reaching the server directly
over http while `--public-url` is https yields https URLs from `build_absolute_uri`. That is why
tunnel mode is documented with `--host 127.0.0.1`: the tunnel should be the only way in.

`SECURE_PROXY_SSL_HEADER` and `CSRF_TRUSTED_ORIGINS` are nevertheless still set in the settings.
They are inert under `cuhasc run`, and they are what makes mode 3.1 work when
`cuhasc.wsgi:application` is served by gunicorn behind nginx, where the forwarded header is
genuine.
