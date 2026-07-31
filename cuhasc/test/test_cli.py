import argparse
import contextlib
import sqlite3

import pytest

import cuhasc.cli as cli
import cuhasc.deployment as deployment
from cuhasc.models import AdminPage


def test_base_url_ok(monkeypatch):
    monkeypatch.delenv(deployment.PUBLIC_URL_ENV, raising=False)
    assert cli._base_url('0.0.0.0', 8037) == 'http://localhost:8037', \
        "0.0.0.0 means 'every interface' and is not usable in a link"
    assert cli._base_url('', 8037) == 'http://localhost:8037'
    assert cli._base_url('127.0.0.1', 9000) == 'http://127.0.0.1:9000'
    monkeypatch.setenv(deployment.PUBLIC_URL_ENV, 'https://x.trycloudflare.com')
    assert cli._base_url('0.0.0.0', 8037) == 'https://x.trycloudflare.com', \
        "a configured public URL wins over the bind address"


def test_lan_url_ok(monkeypatch):
    monkeypatch.delenv(deployment.PUBLIC_URL_ENV, raising=False)
    assert cli._lan_url('0.0.0.0', 8037).startswith('http://')
    assert cli._lan_url('127.0.0.1', 8037) is None, "a loopback bind is not reachable from a LAN"
    monkeypatch.setenv(deployment.PUBLIC_URL_ENV, 'https://x.trycloudflare.com')
    assert cli._lan_url('0.0.0.0', 8037) is None, "behind a tunnel the LAN URL only confuses"


def test_urls_ok(monkeypatch):
    monkeypatch.delenv(deployment.PUBLIC_URL_ENV, raising=False)
    urls = cli._urls('127.0.0.1', 8037, adminpage_token='tok3n')
    assert urls['home page'] == 'http://127.0.0.1:8037'
    assert urls['admin page'] == 'http://127.0.0.1:8037/adminpage/tok3n'
    assert 'on this LAN' not in urls
    assert 'admin page' not in cli._urls('127.0.0.1', 8037), "no token, no admin link"


def test_main_ok(capsys):
    for argv in (['--version'], ['--help'], ['run', '--help']):
        with pytest.raises(SystemExit) as exit_info:
            cli.main(argv)
        assert exit_info.value.code == 0, f"`cuhasc {' '.join(argv)}` must succeed"
    with pytest.raises(SystemExit) as exit_info:
        cli.main([])
    assert exit_info.value.code != 0, "a subcommand is required"


def test_run_serves_and_reports_the_urls(db, monkeypatch, capsys):
    served = {}
    monkeypatch.setattr('waitress.serve', lambda app, **kwargs: served.update(kwargs))
    monkeypatch.setattr('django.core.management.call_command', lambda *args, **kwargs: None)
    monkeypatch.delenv(deployment.PUBLIC_URL_ENV, raising=False)
    assert cli._run(argparse.Namespace(host='0.0.0.0', port=8037)) == 0
    assert served['host'] == '0.0.0.0' and served['port'] == 8037
    assert served['url_scheme'] == 'http'
    token = AdminPage.objects.get().token
    banner = capsys.readouterr().out
    assert 'http://localhost:8037' in banner
    assert f"/adminpage/{token}" in banner


def test_run_declares_https_when_behind_a_tunnel(db, monkeypatch):
    # Waitress strips X-Forwarded-Proto from untrusted peers by default, so the scheme has to be
    # stated outright; otherwise Django considers the request insecure and rejects every POST.
    served = {}
    monkeypatch.setattr('waitress.serve', lambda app, **kwargs: served.update(kwargs))
    monkeypatch.setattr('django.core.management.call_command', lambda *args, **kwargs: None)
    monkeypatch.setenv(deployment.PUBLIC_URL_ENV, 'https://x.trycloudflare.com')
    cli._run(argparse.Namespace(host='127.0.0.1', port=8037))
    assert served['url_scheme'] == 'https'


def test_run_error_when_the_questionnaire_data_is_missing(db, monkeypatch, capsys):
    # The failure this guards against is silent: the loaders glob, so a missing data directory
    # yields no questionnaire rather than an error, and the server would look perfectly healthy.
    monkeypatch.setattr('django.core.management.call_command', lambda *args, **kwargs: None)
    monkeypatch.setattr('cuhasc.instruments.get_languages', lambda: [])
    assert cli._run(argparse.Namespace(host='0.0.0.0', port=8037)) == 1
    assert 'no questionnaire data' in capsys.readouterr().err


def test_run_keeps_the_admin_link_across_restarts(db, monkeypatch):
    monkeypatch.setattr('waitress.serve', lambda app, **kwargs: None)
    monkeypatch.setattr('django.core.management.call_command', lambda *args, **kwargs: None)
    cli._run(argparse.Namespace(host='0.0.0.0', port=8037))
    first = AdminPage.objects.get().token
    cli._run(argparse.Namespace(host='0.0.0.0', port=8037))
    assert AdminPage.objects.get().token == first, \
        "a Culture Lead who saved the admin link must not lose it by restarting the server"


def test_backup_and_restore_round_trip(tmp_path, monkeypatch, capsys):
    database = tmp_path / 'db.sqlite3'
    _write_database(database, 'before')
    monkeypatch.setattr(cli, '_database_path', lambda: database)
    backup_file = tmp_path / 'backup.sqlite3'
    assert cli._backup(argparse.Namespace(file=backup_file, force=False)) == 0
    assert _read_database(backup_file) == 'before'

    _write_database(database, 'after')
    assert cli._restore(argparse.Namespace(file=backup_file, force=True)) == 0
    assert _read_database(database) == 'before', "the backup must have replaced the database"
    superseded = [p for p in tmp_path.glob('db.*.sqlite3')]
    assert len(superseded) == 1 and _read_database(superseded[0]) == 'after', \
        "restoring must keep the replaced database rather than destroy it"


def test_backup_error(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, '_database_path', lambda: tmp_path / 'absent.sqlite3')
    assert cli._backup(argparse.Namespace(file=tmp_path / 'out.sqlite3', force=False)) == 1
    assert 'no database' in capsys.readouterr().err


def test_restore_error(tmp_path, monkeypatch, capsys):
    database = tmp_path / 'db.sqlite3'
    _write_database(database, 'precious')
    monkeypatch.setattr(cli, '_database_path', lambda: database)
    assert cli._restore(argparse.Namespace(file=tmp_path / 'absent.sqlite3', force=True)) == 1
    assert 'no such backup file' in capsys.readouterr().err

    backup_file = tmp_path / 'backup.sqlite3'
    _write_database(backup_file, 'other')
    assert cli._restore(argparse.Namespace(file=backup_file, force=False)) == 1, \
        "replacing an existing database must require --force"
    assert _read_database(database) == 'precious'


def test_create_data_dir_ok(tmp_path, monkeypatch):
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path / 'fresh'))
    monkeypatch.setattr(deployment, 'is_source_checkout', lambda: False)
    data_dir = cli._create_data_dir()
    keyfile = data_dir / deployment.SECRET_KEY_FILE
    assert data_dir.is_dir() and keyfile.is_file()
    assert keyfile.stat().st_mode & 0o777 == 0o600, "the secret key must not be world-readable"
    key = keyfile.read_text()
    cli._create_data_dir()
    assert keyfile.read_text() == key, \
        "a key that changed per start would invalidate every CSRF token in flight"


def test_create_data_dir_writes_no_key_in_a_source_checkout(tmp_path, monkeypatch):
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path))
    monkeypatch.setattr(deployment, 'is_source_checkout', lambda: True)
    cli._create_data_dir()
    assert not (tmp_path / deployment.SECRET_KEY_FILE).exists(), \
        "development uses the well-known key; a checkout collects no deployment state"


def _read_database(path) -> str:
    with contextlib.closing(sqlite3.connect(path)) as database:
        return database.execute("select mark from marker").fetchone()[0]


def _write_database(path, mark: str):
    with contextlib.closing(sqlite3.connect(path)) as database:
        database.execute("create table if not exists marker (mark text)")
        database.execute("delete from marker")
        database.execute("insert into marker values (?)", (mark,))
        database.commit()
