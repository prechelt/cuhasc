import pathlib

import pytest
from django.core.exceptions import ImproperlyConfigured

import cuhasc.deployment as deployment


def test_data_dir_ok(monkeypatch, tmp_path):
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path))
    assert deployment.data_dir() == tmp_path
    monkeypatch.setenv(deployment.DATA_DIR_ENV, '~/somewhere')
    assert deployment.data_dir() == pathlib.Path.home() / 'somewhere', "~ must be expanded"


def test_data_dir_defaults_to_the_checkout_when_developing(monkeypatch):
    # The marker keeps development on the database next to manage.py, so that installing
    # cuhasc does not silently move the developer's data to ~/.cuhasc.
    monkeypatch.delenv(deployment.DATA_DIR_ENV, raising=False)
    assert deployment.is_source_checkout()
    assert deployment.data_dir() == pathlib.Path(deployment.__file__).resolve().parent.parent


def test_data_dir_defaults_to_the_home_directory_when_installed(monkeypatch):
    monkeypatch.delenv(deployment.DATA_DIR_ENV, raising=False)
    monkeypatch.setattr(deployment, 'is_source_checkout', lambda: False)
    assert deployment.data_dir() == pathlib.Path.home() / deployment.DATA_DIR_NAME


def test_allowed_hosts_ok(monkeypatch):
    monkeypatch.delenv(deployment.ALLOWED_HOSTS_ENV, raising=False)
    assert deployment.allowed_hosts() == ['*'], "no accounts, so the Host header guards nothing"
    monkeypatch.setenv(deployment.ALLOWED_HOSTS_ENV, 'cuhasc.example.org, 10.0.0.5 ,')
    assert deployment.allowed_hosts() == ['cuhasc.example.org', '10.0.0.5']


def test_public_url_ok(monkeypatch):
    monkeypatch.delenv(deployment.PUBLIC_URL_ENV, raising=False)
    assert deployment.public_url() == ''
    monkeypatch.setenv(deployment.PUBLIC_URL_ENV, 'https://x.trycloudflare.com/')
    assert deployment.public_url() == 'https://x.trycloudflare.com', "trailing slash must go"


def test_debug_ok(monkeypatch):
    monkeypatch.delenv(deployment.DEBUG_ENV, raising=False)
    assert deployment.debug() is False, "an installed deployment must not run with DEBUG on"
    monkeypatch.setenv(deployment.DEBUG_ENV, '1')
    assert deployment.debug() is True


def test_secret_key_ok(monkeypatch, tmp_path):
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path))
    monkeypatch.delenv(deployment.SECRET_KEY_ENV, raising=False)
    assert deployment.secret_key() == deployment.DEV_SECRET_KEY, "checkout fallback"
    (tmp_path / deployment.SECRET_KEY_FILE).write_text("from-the-file\n", encoding='utf-8')
    assert deployment.secret_key() == 'from-the-file', "the key file wins over the fallback"
    monkeypatch.setenv(deployment.SECRET_KEY_ENV, 'from-the-environment')
    assert deployment.secret_key() == 'from-the-environment', "the environment wins over both"


def test_secret_key_error(monkeypatch, tmp_path):
    # An installed deployment without a key must refuse to start rather than invent one per
    # process, which would invalidate every CSRF token that is currently in a browser.
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path))
    monkeypatch.delenv(deployment.SECRET_KEY_ENV, raising=False)
    monkeypatch.setattr(deployment, 'is_source_checkout', lambda: False)
    with pytest.raises(ImproperlyConfigured, match=deployment.SECRET_KEY_ENV):
        deployment.secret_key()


def test_importing_settings_writes_nothing(monkeypatch, tmp_path):
    # The guarantee that makes it safe for pytest, `manage.py check` and django-admin to import
    # the settings: reading configuration never creates the data directory or the key file.
    monkeypatch.setenv(deployment.DATA_DIR_ENV, str(tmp_path / 'not-created'))
    deployment.data_dir()
    deployment.secret_key()
    assert not (tmp_path / 'not-created').exists()
