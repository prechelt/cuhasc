"""
The ``cuhasc`` command: the entire user interface of an installed CuHaSc.

A Culture Lead is not expected to be a developer, so this command must cover everything an
installed deployment needs -- starting the server, recovering the admin link, backing the data
up -- without a source checkout, a ``manage.py`` or a Django vocabulary. ``cuhasc manage`` is
the escape hatch for the cases that were not foreseen.

Ordering matters in ``main()``: the settings read their configuration from the environment at
import time and refuse to start without a secret key, so all environment variables must be set
and the data directory must exist *before* ``django.setup()`` is called.
"""
import argparse
import contextlib
import datetime
import importlib.metadata
import os
import pathlib
import secrets
import socket
import sqlite3
import sys

import cuhasc.deployment as deployment

DEFAULT_HOST = '0.0.0.0'  # reachable from the LAN; deployments behind a tunnel use 127.0.0.1
DEFAULT_PORT = 8037
SERVER_THREADS = 4  # waitress' own default; ample for SQLite and sub-100ms requests
SECRET_KEY_LENGTH = 50  # bytes of randomness; Django's own checks want a long key
WILDCARD_HOSTS = ('0.0.0.0', '::', '')  # bind addresses that are not usable in a link


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.data_dir:
        os.environ[deployment.DATA_DIR_ENV] = str(args.data_dir)
    if getattr(args, 'public_url', None):
        os.environ[deployment.PUBLIC_URL_ENV] = args.public_url.rstrip('/')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cuhasc.settings')
    _create_data_dir()
    import django
    django.setup()
    return args.execute(args)


def _adminpage(args: argparse.Namespace) -> int:
    from django.core.management import call_command
    call_command('adminpage', base_url=_base_url('localhost', args.port))
    return 0


def _backup(args: argparse.Namespace) -> int:
    source = _database_path()
    if not source.is_file():
        print(f"error: there is no database at {source} yet", file=sys.stderr)
        return 1
    target = args.file or pathlib.Path(f"cuhasc-backup-{datetime.date.today().isoformat()}.sqlite3")
    if target.exists() and not args.force:
        print(f"error: {target} exists; use --force to overwrite it", file=sys.stderr)
        return 1
    _copy_database(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


def _base_url(host: str, port: int) -> str:
    """The URL a browser should use: the public one if configured, else the bind address --
    with wildcard bind addresses replaced, since '0.0.0.0' means 'all of them', not a host."""
    public_url = deployment.public_url()
    if public_url:
        return public_url
    return f"http://{'localhost' if host in WILDCARD_HOSTS else host}:{port}"


def _copy_database(source: pathlib.Path, target: pathlib.Path):
    """Copy via SQLite's own backup API, which is safe while the server is running -- unlike
    a plain file copy, which can catch the database mid-write."""
    with contextlib.closing(sqlite3.connect(f"file:{source}?mode=ro", uri=True)) as origin:
        with contextlib.closing(sqlite3.connect(target)) as copy:
            origin.backup(copy)


def _database_path() -> pathlib.Path:
    from django.conf import settings
    return pathlib.Path(settings.DATABASES['default']['NAME'])


def _create_data_dir() -> pathlib.Path:
    """Create the data directory and, in an installed deployment, its secret key.

    The settings deliberately never write, so this is the one place that does. In a source
    checkout no key file is written: the well-known development key applies there, and a
    checkout should not accumulate deployment state.
    """
    data_dir = deployment.data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)
    keyfile = data_dir / deployment.SECRET_KEY_FILE
    if not keyfile.is_file() and not deployment.is_source_checkout():
        keyfile.write_text(f"{secrets.token_urlsafe(SECRET_KEY_LENGTH)}\n", encoding='utf-8')
        keyfile.chmod(0o600)
    return data_dir


def _info(args: argparse.Namespace) -> int:
    from django.conf import settings
    import cuhasc.handbook as handbook
    import cuhasc.instruments as instruments
    database = _database_path()
    sections = sum(len(chapter) for chapter in handbook.get_sections_by_chapter().values())
    print(f"cuhasc {_version()}")
    print(f"  data directory: {settings.DATA_DIR}")
    print(f"  database:       {database}{'' if database.is_file() else '  (not created yet)'}")
    print(f"  questionnaire:  {_plural(len(instruments.get_languages()), 'language')}")
    print(f"  handbook:       {_plural(sections, 'section')}")
    print(f"  content:        {_stored_content(database)}")
    for label, url in _urls('localhost', args.port).items():
        print(f"  {label + ':':15} {url}")
    return 0


def _lan_url(host: str, port: int) -> str | None:
    """The URL to hand to Team Members on the same LAN, or None when it is not applicable.

    The UDP socket selects a route; it sends nothing and needs no reachable network.
    """
    if host not in WILDCARD_HOSTS or deployment.public_url():
        return None
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as probe:
        try:
            probe.connect(('10.255.255.255', 1))
            return f"http://{probe.getsockname()[0]}:{port}"
        except OSError:
            return None


def _manage(args: argparse.Namespace) -> int:
    from django.core.management import execute_from_command_line
    execute_from_command_line(['cuhasc manage', *args.rest])
    return 0


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='cuhasc', description="Culture Handbook for Scrum.")
    parser.add_argument('--version', action='version', version=f"cuhasc {_version()}")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--data-dir', type=pathlib.Path, default=None,
                        help=f"where database and secret key live "
                             f"(default: ${deployment.DATA_DIR_ENV} or ~/{deployment.DATA_DIR_NAME})")
    subparsers = parser.add_subparsers(dest='command', required=True)

    run = subparsers.add_parser('run', parents=[common], help="start the server")
    run.add_argument('--host', default=DEFAULT_HOST,
                     help=f"address to bind to (default: {DEFAULT_HOST}, i.e. reachable from "
                          f"the LAN; use 127.0.0.1 when only a tunnel should reach it)")
    run.add_argument('--port', type=int, default=DEFAULT_PORT, help=f"default: {DEFAULT_PORT}")
    run.add_argument('--public-url', default=None,
                     help="URL Team Members will use, if a tunnel or proxy makes it differ from "
                          "the bind address; without it, form submissions behind a tunnel fail")
    run.set_defaults(execute=_run)

    adminpage = subparsers.add_parser('adminpage', parents=[common],
                                      help="reset the admin-page token and print its link")
    adminpage.add_argument('--port', type=int, default=DEFAULT_PORT)
    adminpage.add_argument('--public-url', default=None)
    adminpage.set_defaults(execute=_adminpage)

    info = subparsers.add_parser('info', parents=[common],
                                 help="show version, data directory and the URLs to hand out")
    info.add_argument('--port', type=int, default=DEFAULT_PORT)
    info.add_argument('--public-url', default=None)
    info.set_defaults(execute=_info)

    backup = subparsers.add_parser('backup', parents=[common], help="copy the database to a file")
    backup.add_argument('file', nargs='?', type=pathlib.Path, default=None,
                        help="default: cuhasc-backup-<today>.sqlite3 in the current directory")
    backup.add_argument('--force', action='store_true', help="overwrite an existing file")
    backup.set_defaults(execute=_backup)

    restore = subparsers.add_parser('restore', parents=[common],
                                    help="replace the database with a backup")
    restore.add_argument('file', type=pathlib.Path)
    restore.add_argument('--force', action='store_true',
                         help="required once a database exists; the old one is kept alongside")
    restore.set_defaults(execute=_restore)

    manage = subparsers.add_parser('manage', parents=[common],
                                   help="run a Django management command (escape hatch)")
    manage.add_argument('rest', nargs=argparse.REMAINDER)
    manage.set_defaults(execute=_manage)
    return parser


def _restore(args: argparse.Namespace) -> int:
    if not args.file.is_file():
        print(f"error: no such backup file: {args.file}", file=sys.stderr)
        return 1
    target = _database_path()
    if target.is_file():
        if not args.force:
            print(f"error: {target} exists; use --force to replace it", file=sys.stderr)
            return 1
        superseded = target.with_suffix(f".{datetime.datetime.now():%Y%m%d-%H%M%S}.sqlite3")
        _copy_database(target, superseded)
        print(f"kept the previous database as {superseded}")
    _copy_database(args.file, target)
    print(f"restored {args.file} into {target}")
    return 0


def _run(args: argparse.Namespace) -> int:
    import waitress
    from django.core.management import call_command
    import cuhasc.instruments as instruments
    from cuhasc.models import AdminPage
    from cuhasc.wsgi import application
    call_command('migrate', verbosity=0, interactive=False)  # idempotent, so there is no setup step
    if not instruments.get_languages():
        # Turn a silent failure into a loud one: the loaders glob, so a data directory that is
        # missing yields no questionnaire at all rather than an error, and the deployment would
        # look healthy until the first Team Member opened the form.
        print(f"error: no questionnaire data in {instruments.INSTRUMENTS_DIR}", file=sys.stderr)
        return 1
    adminpage = AdminPage.current()
    base_url = _base_url(args.host, args.port)
    _print_banner(args, adminpage.token)
    waitress.serve(application, host=args.host, port=args.port, threads=SERVER_THREADS,
                   # Waitress strips X-Forwarded-Proto from untrusted peers by default, so a
                   # proxy header cannot tell Django that the tunnel terminated TLS. Stating the
                   # scheme here trusts no client input and needs no proxy address.
                   url_scheme='https' if base_url.startswith('https://') else 'http')
    return 0


def _plural(count: int, noun: str) -> str:
    return f"{count} {noun}{'' if count == 1 else 's'}"


def _print_banner(args: argparse.Namespace, adminpage_token: str):
    from django.conf import settings
    print(f"CuHaSc {_version()}")
    print(f"  data directory: {settings.DATA_DIR}")
    for label, url in _urls(args.host, args.port, adminpage_token).items():
        print(f"  {label + ':':15} {url}")
    print("Press Ctrl-C to stop.")
    sys.stdout.flush()  # stdout is block-buffered off a terminal, and waitress then never returns


def _stored_content(database: pathlib.Path) -> str:
    """How much data the deployment holds. Checks the file first, because merely querying
    would make Django create an empty database -- `cuhasc info` must not change anything."""
    from django.db import OperationalError
    from cuhasc.models import Member, Team
    if not database.is_file():
        return "none yet; `cuhasc run` creates the database"
    try:
        return f"{_plural(Team.objects.count(), 'team')}, {_plural(Member.objects.count(), 'member')}"
    except OperationalError:
        return "unreadable; the database exists but has no tables"


def _urls(host: str, port: int, adminpage_token: str = '') -> dict[str, str]:
    import cuhasc.base as base
    base_url = _base_url(host, port)
    urls = {'home page': base_url}
    lan_url = _lan_url(host, port)
    if lan_url:
        urls['on this LAN'] = lan_url
    if adminpage_token:
        urls['admin page'] = base.join_url(base_url, f"/adminpage/{adminpage_token}")
    return urls


def _version() -> str:
    try:
        return importlib.metadata.version('cuhasc')
    except importlib.metadata.PackageNotFoundError:
        return "(source checkout)"
