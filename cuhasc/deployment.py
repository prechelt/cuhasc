"""
Reads the deployment environment: where mutable state lives and how the server is reached.

CuHaSc is installed as a package and started by its own ``cuhasc`` command, so the Django
settings can no longer assume a source checkout. Everything that differs between a checkout
and an installed deployment is resolved here, from environment variables that ``cuhasc.cli``
sets before ``django.setup()``.

This module only *reads*. The data directory and the secret key file are created by
``cuhasc.cli``, so that merely importing the settings -- during pytest, ``manage.py check``,
or any ``django-admin`` invocation -- never writes to disk.
"""
import os
import pathlib

from django.core.exceptions import ImproperlyConfigured

ALLOWED_HOSTS_ENV = 'CUHASC_ALLOWED_HOSTS'  # comma-separated; only a public server needs it
DATA_DIR_ENV = 'CUHASC_HOME'                # also settable as `cuhasc --data-dir`
DEBUG_ENV = 'CUHASC_DEBUG'                  # '1' turns Django's debug mode on; manage.py sets it
PUBLIC_URL_ENV = 'CUHASC_PUBLIC_URL'        # also settable as `cuhasc --public-url`
SECRET_KEY_ENV = 'CUHASC_SECRET_KEY'        # for running cuhasc.wsgi under a foreign WSGI host

DATA_DIR_NAME = '.cuhasc'  # below the user's home directory, on every operating system
DB_FILE = 'db.sqlite3'
SECRET_KEY_FILE = 'secret_key'
REPO_MARKER = 'manage.py'  # exists in a source checkout, never in an installed package

# The key a source checkout uses when no other one is configured. Public by definition, hence
# the name: it must never become the key of a deployment that is reachable by others.
DEV_SECRET_KEY = 'django-insecure-^okyqa6)-+a#!*vfd9yr6hoc*!v8mkfxz$&&h-0^9h70$k#6g^'


def allowed_hosts() -> list[str]:
    """Host names Django will answer for; everything unless configured otherwise.

    Deliberate: CuHaSc has no accounts, sends no mail and derives no absolute URLs from the
    Host header, so that header is not a security boundary here -- the unguessable tokens in
    the URLs are. Meanwhile none of the supported deployments (LAN address, tunnel hostname,
    tailscale name) can enumerate its host names in advance. See docs/adr/0003.
    """
    configured = os.environ.get(ALLOWED_HOSTS_ENV, '')
    return [host.strip() for host in configured.split(',') if host.strip()] or ['*']


def data_dir() -> pathlib.Path:
    """Directory holding everything the application cannot regenerate: database and secret key.

    Kept out of the install tree, which pipx and uv replace wholesale on every upgrade.
    """
    configured = os.environ.get(DATA_DIR_ENV)
    return pathlib.Path(configured).expanduser() if configured else _default_data_dir()


def debug() -> bool:
    """Django's debug mode: off unless explicitly asked for, which manage.py does."""
    return os.environ.get(DEBUG_ENV) == '1'


def is_source_checkout() -> bool:
    return (_repo_root() / REPO_MARKER).is_file()


def public_url() -> str:
    """The URL under which Team Members reach this server, if it differs from the bind address.

    Needed whenever a tunnel or proxy terminates TLS: the browser then sends an https Origin
    that Django would otherwise reject on every POST.
    """
    return (os.environ.get(PUBLIC_URL_ENV) or '').rstrip('/')


def secret_key() -> str:
    """From the environment, else the file that ``cuhasc run`` writes into the data directory,
    else -- in a source checkout only -- the well-known development key.

    An installed deployment with none of these is a configuration error rather than a reason to
    invent a key at import time: a key that differed per process would invalidate every
    outstanding CSRF token, so every questionnaire submission in flight would fail.
    """
    from_environment = os.environ.get(SECRET_KEY_ENV)
    if from_environment:
        return from_environment
    keyfile = data_dir() / SECRET_KEY_FILE
    if keyfile.is_file():
        return keyfile.read_text(encoding='utf-8').strip()
    if is_source_checkout():
        return DEV_SECRET_KEY
    raise ImproperlyConfigured(
        f"no secret key: expected {keyfile} to exist or ${SECRET_KEY_ENV} to be set. "
        f"Normally `cuhasc run` creates that file; set ${SECRET_KEY_ENV} when running "
        f"cuhasc.wsgi under a different WSGI server.")


def _default_data_dir() -> pathlib.Path:
    """The checkout itself when running from a source tree, so that development keeps using the
    database next to manage.py; otherwise a single predictable directory in the user's home,
    identically named on Linux, macOS and Windows so that one backup instruction fits all."""
    if is_source_checkout():
        return _repo_root()
    return pathlib.Path.home() / DATA_DIR_NAME


def _repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent
