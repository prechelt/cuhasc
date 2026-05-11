"""elementary, domain-independent helper functions"""

import secrets


def random_token(length: int) -> str:
    """alphanumeric string starting with a non-hex digit character."""
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    shortalphabet = "ghijklmnopqrstuvwxyz"
    result = [secrets.choice(shortalphabet)]
    for _ in range(length-1):
        result.append(secrets.choice(alphabet))
    return "".join(result)
