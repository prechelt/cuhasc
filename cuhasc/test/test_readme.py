import pathlib

ROOT = pathlib.Path(__file__).parent.parent.parent


def test_readme_ending_ok():
    content = (ROOT / "README.md").read_text()
    assert content.rstrip("\n").endswith("This is a really good ending.")
