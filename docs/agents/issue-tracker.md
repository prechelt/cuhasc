# Issue tracker: Markdown files

Issues and PRDs for this repo live as Markdown files in directory `issues/`.
Read the write them as plain files; there is no special tool for this.

Filesnames look like `issues/001-topic-of-this-particular-issue`.
We use `001`, `002` etc. in the filenames but mention issues as `#1`, `#2` etc. as usual.
The hind part is the slugified issue title.

Content uses YAML topmatter and looks for instance as follows
```
title: Topic of this particular issue
state: open
labels: ready-for-agent
---

# Topic of this particular issue

Description of the initial issue, can be short or long.

## 2026-07-02, prechelt

Comment (titled by commenting date and author username) of noteworthy event during handling the ticket.
There can be zero or more such sections in any ticket.
```

- `title:` is a descriptive title  
- `state:` is either `open` or `closed`  
- `labels:` is a comma-separated list of mostly standardized labels according to `triage-labels.md`
