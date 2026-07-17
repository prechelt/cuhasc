import cuhasc.instruments as instruments

DIMENSION_ORDER = ['PO', 'UN', 'CO', 'LT', 'MA']

_SVG_WIDTH = 500
_SVG_LEFT = 170     # space for the Dimension labels
_SVG_RIGHT = 20
_SVG_PLOT_W = _SVG_WIDTH - _SVG_LEFT - _SVG_RIGHT
_SVG_TOP = 24
_SVG_ROW_H = 48
_SVG_HEIGHT = _SVG_TOP + len(DIMENSION_ORDER) * _SVG_ROW_H + 12


def _score_to_x(score: float) -> float:
    return _SVG_LEFT + (score - 1) / 4 * _SVG_PLOT_W


def _svg_grid(parts: list[str], language: str) -> dict[str, float]:
    """Append the shared axis ticks, Dimension lines and localized labels to ``parts``.
    Returns the y coordinate of each Dimension row, keyed by code."""
    for score in range(1, 6):
        x = _score_to_x(score)
        parts.append(f'<text x="{x:.1f}" y="{_SVG_TOP - 8}" text-anchor="middle"'
                     f' font-size="11" fill="var(--cuhasc-chart-muted)">{score}</text>')
    rows: dict[str, float] = {}
    for i, code in enumerate(DIMENSION_ORDER):
        y = _SVG_TOP + i * _SVG_ROW_H + _SVG_ROW_H // 2
        rows[code] = y
        label = instruments.get_dimension_name(code, language)
        parts.append(f'<line x1="{_SVG_LEFT}" y1="{y}" x2="{_SVG_WIDTH - _SVG_RIGHT}" y2="{y}"'
                     f' stroke="var(--cuhasc-chart-line)" stroke-width="1"/>')
        parts.append(f'<text x="{_SVG_LEFT - 10}" y="{y + 4}" text-anchor="end"'
                     f' font-size="13" fill="var(--cuhasc-chart-text)">{label}</text>')
    return rows


def culture_profile_svg(profile: dict[str, float], language: str) -> str:
    """Inline SVG of a Culture Profile (ADR-0001): one [1,5] line per Dimension,
    a blue dot at each defined Score, and the localized Dimension label."""
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{_SVG_WIDTH}" height="{_SVG_HEIGHT}">']
    rows = _svg_grid(parts, language)
    for code, y in rows.items():
        if code in profile:
            x = _score_to_x(profile[code])
            parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="var(--cuhasc-blue)"/>')
    parts.append('</svg>')
    return '\n'.join(parts)


def team_culture_profile_svg(team_profile: dict, language: str) -> str:
    """Inline SVG of a Team Culture Profile (ADR-0001): the shared Dimension grid with
    a small dot per member on each Dimension line, a larger dot for the per-Dimension
    team mean, and a per-member label (hidden by default, toggled via JS)."""
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{_SVG_WIDTH}" height="{_SVG_HEIGHT}">']
    rows = _svg_grid(parts, language)
    for member in team_profile['members']:
        for code, score in member['profile'].items():
            y = rows[code]
            x = _score_to_x(score)
            parts.append(f'<circle class="member-dot" cx="{x:.1f}" cy="{y}" r="4" fill="var(--cuhasc-orange)"/>')
            parts.append(f'<text class="member-label" x="{x:.1f}" y="{y - 8}" text-anchor="middle"'
                         f' font-size="10" fill="var(--cuhasc-chart-text)" visibility="hidden">{member["name"]}</text>')
    for code, score in team_profile['means'].items():
        y = rows[code]
        x = _score_to_x(score)
        parts.append(f'<circle class="mean-dot" cx="{x:.1f}" cy="{y}" r="8" fill="var(--cuhasc-blue)"/>')
    parts.append('</svg>')
    return '\n'.join(parts)
