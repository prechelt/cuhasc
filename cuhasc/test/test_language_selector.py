import json

import pytest
from django.urls import reverse

import cuhasc.instruments as instruments
import cuhasc.constants as c
from cuhasc.models import Member, Team


# ---- get_languages() filtering tests ----

def test_get_languages_includes_en():
    assert 'en' in instruments.get_languages()


def test_get_languages_includes_de():
    assert 'de' in instruments.get_languages()


def test_get_languages_excludes_language_without_dimensions(monkeypatch):
    # A language with scales+questionnaire but no dimensions file must be excluded.
    saved = dict(instruments._dimensions)
    monkeypatch.setattr(instruments, '_dimensions', {'en': saved.get('en', {})})
    langs = instruments.get_languages()
    assert 'de' not in langs
    assert 'en' in langs


# ---- fixtures ----

@pytest.fixture
def team(db):
    return Team.objects.create(name='LSTeam', token='LSTOKEN111')


@pytest.fixture
def member(team):
    return Member.objects.create(name='LSTester', token='LSMEMBER11', team=team)


def _all_answers(lang='en', value='3'):
    """Return {item: value, ...} for all questionnaire items in the given language."""
    return {item.item: value for item in instruments.get_questionnaire(lang)}


# ---- Language selector visible on GET ----

def test_create_member_shows_language_dropdown(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    response = client.get(url)
    content = response.content.decode()
    assert 'dropdown' in content
    assert 'English' in content


def test_edit_member_shows_language_dropdown(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    response = client.get(url)
    content = response.content.decode()
    assert 'dropdown' in content
    assert 'English' in content


# ---- Language switch on create_member ----

def test_create_member_switch_returns_200(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    assert response.status_code == 200


def test_create_member_switch_does_not_create_member(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(), '_switch_language': 'de'}
    client.post(url, data)
    assert Member.objects.count() == 0


def test_create_member_switch_no_validation_errors(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    content = response.content.decode()
    assert 'text-danger' not in content


def test_create_member_switch_sets_language_cookie(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    cookie_val = response.cookies.get(c.COOKIE_NAME)
    assert cookie_val is not None
    cookie_data = json.loads(cookie_val.value)
    assert cookie_data.get('language') == 'de'


def test_create_member_switch_preserves_answers(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(value='2'), '_switch_language': 'de'}
    response = client.post(url, data)
    content = response.content.decode()
    # All questionnaire answers (value=2) must be pre-selected in re-rendered form
    expected_count = len(instruments.get_questionnaire('de'))
    assert content.count(' checked') == expected_count


def test_create_member_switch_rerenders_in_new_language(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    data = {'name': 'Alice', **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    content = response.content.decode()
    # German questionnaire items should appear in content
    de_items = instruments.get_questionnaire('de')
    assert de_items[0].content in content


def test_create_member_normal_submit_still_validates(client, team):
    url = reverse('create_member', args=[team.id, team.member_token])
    # Submit without answers (incomplete form)
    response = client.post(url, {'name': 'Alice'})
    assert response.status_code == 200
    assert Member.objects.count() == 0
    content = response.content.decode()
    assert 'text-danger' in content


# ---- Language switch on edit_member ----

def test_edit_member_switch_returns_200(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    data = {'name': member.name, **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    assert response.status_code == 200


def test_edit_member_switch_no_validation_errors(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    data = {'name': member.name, **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    content = response.content.decode()
    assert 'text-danger' not in content


def test_edit_member_switch_sets_language_cookie(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    data = {'name': member.name, **_all_answers(), '_switch_language': 'de'}
    response = client.post(url, data)
    cookie_val = response.cookies.get(c.COOKIE_NAME)
    assert cookie_val is not None
    cookie_data = json.loads(cookie_val.value)
    assert cookie_data.get('language') == 'de'


def test_edit_member_switch_preserves_answers(client, member):
    url = reverse('edit_member', args=[member.id, member.token])
    data = {'name': member.name, **_all_answers(value='5'), '_switch_language': 'de'}
    response = client.post(url, data)
    content = response.content.decode()
    expected_count = len(instruments.get_questionnaire('de'))
    assert content.count(' checked') == expected_count
