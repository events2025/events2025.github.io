# 🛰️ Events in Context

A community-driven knowledge base for spatio-temporal **event** data, built with the
[Just the Docs](https://github.com/just-the-docs/just-the-docs) Jekyll theme.

**Source of truth:** one YAML file per item in `data/Yaml_files/`.  
On each push, a small Python script renders the docs pages from YAML **before** Jekyll builds the site.

---

## ✨ What’s inside

- **YAML database**: curated items (datasets, websites, tools, tutorials, papers/methods, conferences/journals).
- **Docs pages** in `docs/` generated from YAML using `docs/*.md.template`.
- **Just-the-Docs site** (Jekyll) served via GitHub Pages.

---

## 🗂️ Repository layout (high-level)

- `data/Yaml_files/` — one YAML file per item (the canonical content).
- `docs/` — Markdown pages; sections between `<!-- START --> … <!-- STOP -->` are auto-generated.
- `main_create_website.py` — builds docs from YAML.
- `_config.yml`, `Gemfile`, `Gemfile.lock` — Jekyll configuration.
- `assets/` — images, styles, etc.
- `requirements.txt` — Python deps for the build script.

---

## 🧱 YAML schema

Each item is a YAML file in `data/Yaml_files/` named like `<type_slug>-<title_slug>.yaml`
(e.g., `dataset_usa-covid-19.yaml`).

**Required fields**
- `Timestamp` — e.g., `2025/09/04 7:20:02 PM GMT+1`
- `Type` — one of: `Dataset`, `Website`, `Tool`, `Tutorial`, `Paper or Method`, `Conference or Journal`
- `Title`
- `URL`
- `Description` — 1–3 lines
- `Contributor Id` — your name or handle
- `Image` — path under `/assets/images/thumb/...` (optional but recommended)
- `Subsection` — rules below

**Subsection rules**
- **Datasets:** `Contexts (Environment & Climate)`, `Contexts (Misc Data & APIs)`,
  `Contexts (Population Data & Mobility)`, `Events`
- **Conferences & Journals:** `conference` or `journal`

**Example**
```yaml
Timestamp: 2025/09/04 7:20:02 PM GMT+1
Type: Dataset
Title: USA COVID-19
URL: https://github.com/nytimes/covid-19-data
Description: County- and state-level time series with dates, cases, and deaths.
Contributor Id: Your Name
Image: /assets/images/thumb/usa_covid_19.jpg
Subsection: Contexts (Misc Data & APIs)
Keywords: covid, usa, health
Year: 2020

