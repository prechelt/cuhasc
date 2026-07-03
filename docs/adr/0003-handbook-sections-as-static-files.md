# Handbook Sections as static Markdown files, not a DB model

Handbook Sections (title + trigger + Markdown advice body) are stored as files under
`handbook/`, parsed at startup and held in memory — the same pattern `instruments.py`
already uses for questionnaire content — rather than as a Django model editable through
an admin UI. Section content is authored by the developer/researcher, not submitted by
Culture Leads or Team Members, so there is no runtime need to create, edit, or store it
in the database. This keeps all "instrument-like" content (scales, questionnaire items,
Dimension names, and now advice) loaded the same way, and avoids building admin tooling
for content that changes at the pace of code changes, not at the pace of team usage.
