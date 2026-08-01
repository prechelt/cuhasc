import unicodedata

import cuhasc.instruments as instruments

DIMENSION_ORDER = ['PO', 'UN', 'CO', 'LT', 'MA']

_SVG_MIN_LEFT = 170   # space for the Dimension labels in the common (mostly-Latin) case
_SVG_LABEL_GAP = 10   # gap between a label's right edge and the plot area
_SVG_LABEL_PAD = 4    # breathing room between a label's left edge and the SVG's own edge
_SVG_LABEL_FONT_SIZE = 13
_SVG_PLOT_W = 310
_SVG_RIGHT = 20
_SVG_TOP = 24
_SVG_ROW_H = 48
_SVG_HEIGHT = _SVG_TOP + len(DIMENSION_ORDER) * _SVG_ROW_H + 12


def culture_profile_svg(profile: dict[str, float], language: str) -> str:
    """Inline SVG of a Culture Profile (ADR-0001): one [1,5] line per Dimension,
    a blue dot at each defined Score, and the localized Dimension label."""
    parts, left = _svg_open(language)
    rows = _svg_grid(parts, language, left)
    for code, y in rows.items():
        if code in profile:
            x = _score_to_x(profile[code], left)
            parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="var(--cuhasc-blue)"/>')
    parts.append('</svg>')
    return '\n'.join(parts)


def team_culture_profile_svg(team_profile: dict, language: str) -> str:
    """Inline SVG of a Team Culture Profile (ADR-0001): the shared Dimension grid with
    a small dot per member on each Dimension line, a larger dot for the per-Dimension
    team mean, and a per-member label (hidden by default, toggled via JS)."""
    parts, left = _svg_open(language)
    rows = _svg_grid(parts, language, left)
    for member in team_profile['members']:
        for code, score in member['profile'].items():
            y = rows[code]
            x = _score_to_x(score, left)
            parts.append(f'<circle class="member-dot" cx="{x:.1f}" cy="{y}" r="4" fill="var(--cuhasc-orange)"/>')
            parts.append(f'<text class="member-label" x="{x:.1f}" y="{y - 8}" text-anchor="middle"'
                         f' font-size="10" fill="var(--cuhasc-chart-text)" visibility="hidden">{member["name"]}</text>')
    for code, score in team_profile['means'].items():
        y = rows[code]
        x = _score_to_x(score, left)
        parts.append(f'<circle class="mean-dot" cx="{x:.1f}" cy="{y}" r="8" fill="var(--cuhasc-blue)"/>')
    parts.append('</svg>')
    return '\n'.join(parts)


def _is_wide_char(character: str) -> bool:
    """Whether ``character`` is rendered roughly one em wide (CJK/Hangul scripts),
    as opposed to the narrower average of Latin, Cyrillic, Greek, Arabic, Thai, etc."""
    return unicodedata.east_asian_width(character) in ('W', 'F')


def _label_width(text: str) -> float:
    """Estimated rendered width of ``text`` at ``_SVG_LABEL_FONT_SIZE``, generous enough
    that real fonts fit inside it: combining marks (stacking diacritics) contribute no
    width of their own, wide (CJK/Hangul) characters count a full em, everything else
    (Latin, Cyrillic, Greek, Arabic, Thai, Devanagari, ...) counts as 0.6 em. There is no
    real font-metrics library available server-side (ADR-0001), so this is a heuristic."""
    width_em = sum(0.0 if unicodedata.combining(ch) else (1.0 if _is_wide_char(ch) else 0.6)
                   for ch in text)
    return width_em * _SVG_LABEL_FONT_SIZE


def _score_to_x(score: float, left: float) -> float:
    return left + (score - 1) / 4 * _SVG_PLOT_W


def _svg_grid(parts: list[str], language: str, left: float) -> dict[str, float]:
    """Append the shared axis ticks, Dimension lines and localized labels to ``parts``.
    Returns the y coordinate of each Dimension row, keyed by code."""
    for score in range(1, 6):
        x = _score_to_x(score, left)
        parts.append(f'<text x="{x:.1f}" y="{_SVG_TOP - 8}" text-anchor="middle"'
                     f' font-size="11" fill="var(--cuhasc-chart-muted)">{score}</text>')
    rows: dict[str, float] = {}
    for i, code in enumerate(DIMENSION_ORDER):
        y = _SVG_TOP + i * _SVG_ROW_H + _SVG_ROW_H // 2
        rows[code] = y
        label = instruments.get_dimension_name(code, language)
        parts.append(f'<line x1="{left:.1f}" y1="{y}" x2="{left + _SVG_PLOT_W:.1f}" y2="{y}"'
                     f' stroke="var(--cuhasc-chart-line)" stroke-width="1"/>')
        parts.append(f'<text x="{left - _SVG_LABEL_GAP:.1f}" y="{y + 4}" text-anchor="end"'
                     f' font-size="{_SVG_LABEL_FONT_SIZE}" fill="var(--cuhasc-chart-text)">{label}</text>')
    return rows


def _svg_open(language: str) -> tuple[list[str], float]:
    """Start the parts list for a chart in ``language``, with the left margin widened
    (beyond ``_SVG_MIN_LEFT``) to fit that language's longest Dimension label, and the
    whole SVG scaled down to fit its container on narrow viewports rather than overflow it.
    Returns the parts list and the left margin (x where the plot area begins)."""
    max_label_width = max(_label_width(instruments.get_dimension_name(code, language))
                          for code in DIMENSION_ORDER)
    left = max(_SVG_MIN_LEFT, max_label_width + _SVG_LABEL_GAP + _SVG_LABEL_PAD)
    width = left + _SVG_PLOT_W + _SVG_RIGHT
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {_SVG_HEIGHT}"'
             f' width="{width:.1f}" height="{_SVG_HEIGHT}" style="max-width: 100%; height: auto;">']
    return parts, left
