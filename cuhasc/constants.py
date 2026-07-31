import pathlib

TOKEN_LENGTH_TEAM = 11
TOKEN_LENGTH_MEMBER = 10
TOKEN_LENGTH_ADMINPAGE = 20
COOKIE_NAME = 'cuhasc'
HIGH_CUTOFF: float = 4.0  # a Score at or above this is "high"
LOW_CUTOFF: float = 2.0   # a Score at or below this is "low"
HANDBOOK_DIR = pathlib.Path(__file__).resolve().parent / 'data' / 'handbook'
IMAGE_POOL_DIR = HANDBOOK_DIR / 'img'
