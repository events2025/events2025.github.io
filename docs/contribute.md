---
title: "🤝 Contribute (Add Item)"
nav_order: 10
layout: home
---

# 🤝 Contribute (Add Item)

1) Fork the repo → add a YAML file under `data/Yaml_files/`.  
2) Follow the schema below.  
3) Open a Pull Request. The site builds automatically.

---

## ✅ Accepted Type values
- `Dataset`
- `Website`
- `Tool`
- `Tutorial`
- `Paper or Method`
- `Conference or Journal`

## 🗂️ File naming
`<type_slug>-<title_slug>.yaml`  
Examples: `dataset_usa-covid-19.yaml`, `methods_neural-tpp.yaml`

## 🧱 Required fields
- `Timestamp` — e.g., `2025/09/04 7:20:02 PM GMT+1`
- `Type` — one of the values above
- `Title`
- `URL`
- `Description` — 1–3 lines
- `Contributor Id` — your name or handle
- `Image` — path under `/assets/images/thumb/...` (optional but recommended)
- `Subsection` — see rules below

## 🧭 Subsection rules
**Datasets:**  
- `Contexts (Environment & Climate)`  
- `Contexts (Misc Data & APIs)`  
- `Contexts (Population Data & Mobility)`  
- `Events`  

**Conferences & Journals:**  
- `conference` or `journal`

## 🖼 Image guidelines
- Place thumbnails under `/assets/images/thumb/` (JPG).  
- Name suggestion: `<title_slug>.jpg` (all lowercase, hyphens).

---

## ✍️ Example YAML

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

