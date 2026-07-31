from django.conf import settings


def test_static_files_are_served_with_debug_off(client):
    # The load-bearing test for the WhiteNoise setup: Django's own staticfiles serving is
    # active only while DEBUG is on, and pytest-django forces DEBUG off, so this exercises
    # exactly what an installed deployment does. If it ever fails, the alternative is to set
    # WHITENOISE_USE_FINDERS = False, set STATIC_ROOT, and run collectstatic at start-up.
    assert not settings.DEBUG, "pytest-django is expected to turn DEBUG off"
    response = client.get('/static/cuhasc/cuhasc.css')
    assert response.status_code == 200
    assert b'body' in b''.join(response.streaming_content)


def test_static_url_is_absolute():
    # A relative STATIC_URL makes {% static %} produce URLs relative to the current page, so
    # /handbook/some-slug would ask for /handbook/static/... and get a 404.
    assert settings.STATIC_URL.startswith('/')
