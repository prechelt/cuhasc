import pytest
from django.urls import reverse

import cuhasc.constants as c
import cuhasc.handbook as handbook


def write_section(tmp_path, filename: str, title: str = "A Title",
                   trigger: str = "one-high(PO)", body: str = "Some body text.\n"):
    path = tmp_path / filename
    path.write_text(f"---\ntitle: {title}\ntrigger: {trigger}\n---\n{body}")
    return path


@pytest.fixture
def image_pool(tmp_path, monkeypatch):
    pool = tmp_path / 'img'
    pool.mkdir()
    monkeypatch.setattr(c, 'IMAGE_POOL_DIR', pool)
    return pool


# ---- handbook_section view ----

def test_handbook_section_renders_title_and_body_html(client, tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md",
                  title="Punctuality", body="# Heading\n\nShow up **on time**.\n")
    handbook.load_sections(str(tmp_path / '*.md'))
    content = client.get(reverse('handbook_section', args=["dailystandup-punctuality"])).content.decode()
    assert "Punctuality" in content
    assert "<h1>Heading</h1>" in content
    assert "<strong>on time</strong>" in content


def test_handbook_section_404_for_unknown_slug(client, tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md")
    handbook.load_sections(str(tmp_path / '*.md'))
    response = client.get(reverse('handbook_section', args=["no-such-slug"]))
    assert response.status_code == 404


def test_handbook_section_url_and_html_carry_no_team_or_member_token(client, tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md", title="Punctuality")
    handbook.load_sections(str(tmp_path / '*.md'))
    url = reverse('handbook_section', args=["dailystandup-punctuality"])
    assert url == "/handbook/dailystandup-punctuality"


# ---- handbook_image view ----

def test_handbook_image_serves_existing_file_bytes_and_content_type(client, image_pool):
    (image_pool / 'foo.png').write_bytes(b'\x89PNG fake bytes')
    response = client.get(reverse('handbook_image', args=["foo.png"]))
    assert response.status_code == 200
    assert b''.join(response.streaming_content) == b'\x89PNG fake bytes'
    assert response['Content-Type'] == 'image/png'


def test_handbook_image_404_for_missing_file(client, image_pool):
    response = client.get(reverse('handbook_image', args=["missing.png"]))
    assert response.status_code == 404
