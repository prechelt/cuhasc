import cuhasc.base as base


def test_join_url_ok():
    assert base.join_url('http://localhost:8037', '/adminpage/abc') == \
        'http://localhost:8037/adminpage/abc'
    assert base.join_url('http://localhost:8037/', '/adminpage/abc') == \
        'http://localhost:8037/adminpage/abc', "a trailing slash must not double up"
    assert base.join_url('https://x.trycloudflare.com///', '/') == 'https://x.trycloudflare.com/'


def test_random_token_ok():
    token = base.random_token(11)
    assert len(token) == 11
    assert token.isalnum() and token.islower()
    assert token[0] not in "abcdef0123456789", \
        "must not start with a hex digit, so that a token is never mistaken for a number"
    assert base.random_token(11) != token
