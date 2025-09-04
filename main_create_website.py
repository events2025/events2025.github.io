from __future__ import annotations

import os
import re
import shutil
from pathlib import Path
from typing import Dict

import pandas as pd
import yaml


# -------------------- CONFIG --------------------

# Master CSV with quotes in the filename (valid on modern filesystems)
MASTER_CSV = Path("data") / 'Add Item to "Events in Context" Knowledge Base_1.csv'

# Output directory for per-row YAML files (created automatically)
YAML_OUT_DIR = Path("data") / "Yaml_files"

# Directories for templates and output Markdown
TEMPLATE_DIR = Path("docs")
OUTPUT_DIR = Path("docs")

# Page routing: which Markdown file consumes which (normalized) Type
# We normalize 'Type' (strip emoji/symbols, lowercase) before matching.
MD_TO_TYPE: Dict[str, str] = {
    "websites.md": "website",
    "datasets.md": "dataset",
    "tools.md": "tool",
    "tutorials.md": "tutorial",
    "methods.md": "paper or method",          # Papers & Methods
    "conferences.md": "conference or journal" # Conferences + Journals bucket
}

# Canonical column list for YAML export (and general expectations)
CANON_COLS = [
    "Timestamp",
    "Type",
    "Title",
    "URL",
    "Description",
    "Contributor Id",
    "Image",
    "Subsection",
]


# -------------------- HELPERS --------------------

def clean_title(title: str) -> str:
    """For image fallback filenames (not the YAML names)."""
    title = re.sub(r"[^\w\s-]", "", str(title))
    return title.replace(" ", "_").lower()


def substitute_placeholders(text: str, row: pd.Series) -> str:
    """
    Replace ((Column Name)) placeholders in template with row values.
    Escapes backslashes and dollar signs to avoid breaking Markdown/HTML.
    """
    placeholders = re.findall(r"\(\((.*?)\)\)", text)
    out = text
    for placeholder in placeholders:
        key = placeholder.strip()
        value = str(row.get(key, ""))
        value = value.replace("\\", "\\\\").replace("$", "\\$")
        out = out.replace(f"(({placeholder}))", value)
    return out


def ensure_image_thumb(row: pd.Series) -> str:
    """
    Ensure Image points to /assets/images/thumb/<cleaned>.jpg.
    If the provided 'Image' already targets that folder, keep it.
    Otherwise, set a deterministic path and copy a default placeholder if available.
    """
    os.makedirs("assets/images/thumb", exist_ok=True)
    img = str(row.get("Image", "")).strip()

    # If already pointing to thumb folder, normalize leading slash and return
    if "assets/images/thumb" in img:
        return img if img.startswith("/") else "/" + img

    title = row.get("Title", "item")
    cleaned = clean_title(title)
    new_rel = f"assets/images/thumb/{cleaned}.jpg"

    # Try copying a default image if it doesn't exist yet (optional)
    src = "assets/images/logo.jpg"  # you can provide this in the repo (optional)
    if not os.path.exists(new_rel) and os.path.exists(src):
        try:
            shutil.copy(src, new_rel)
        except Exception as e:
            print(f"Warning: couldn't copy default image for '{title}': {e}")

    return "/" + new_rel


def _parse_year(y):
    try:
        return int(str(y)[:4])
    except Exception:
        return None


def _standardize_subsection(x: str) -> str:
    """
    Map free-form Subsection into {'conference', 'journal'}; default 'journal'.
    """
    s = str(x).strip().lower()
    if "conference" in s or s in {"conf", "conferences"}:
        return "conference"
    if "journal" in s or s == "journals":
        return "journal"
    return s if s in {"conference", "journal"} else "journal"


def normalize_type(s: str) -> str:
    """
    Strip emoji/symbols, lowercase, and map to canonical bucket labels used in MD_TO_TYPE.
    """
    if s is None:
        return ""
    t = re.sub(r"[^\w\s-]", " ", str(s)).lower()  # remove emoji/punct, keep words/spaces
    t = re.sub(r"\s+", " ", t).strip()
    if "website" in t:
        return "website"
    if "dataset" in t:
        return "dataset"
    if "tool" in t:
        return "tool"
    if "tutorial" in t:
        return "tutorial"
    if "paper" in t or "method" in t:
        return "paper or method"
    if "conference" in t or "journal" in t:
        return "conference or journal"
    return t  # fallback (unchanged normalized string)


def simplify_for_filename(text: str, max_len: int = 30) -> str:
    """
    For YAML filenames: remove emoji/symbols, keep word/space/hyphen/underscore,
    collapse spaces to '-', lowercase, then truncate.
    """
    if text is None:
        return "unknown"
    t = str(text).strip().lower()
    t = re.sub(r"[^\w\s\-_]", "", t)
    t = re.sub(r"\s+", "-", t).strip("-_")
    if not t:
        t = "unknown"
    return t[:max_len] or "unknown"


def ensure_unique_path(base_dir: Path, base_name: str) -> Path:
    """
    If base_name exists in base_dir, append -1, -2, ... before extension.
    """
    base_dir.mkdir(parents=True, exist_ok=True)
    root, ext = os.path.splitext(base_name)
    candidate = base_dir / base_name
    k = 1
    while candidate.exists():
        candidate = base_dir / f"{root}-{k}{ext}"
        k += 1
    return candidate


def load_master_csv(path: Path) -> pd.DataFrame:
    """
    Load the master CSV robustly.
    - First try default engine (comma-separated)
    - Fallback to python engine with sep=None to sniff delimiters (comma/tab/semicolon/pipe).
    """
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[])
    except Exception:
        return pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[], engine="python", sep=None)


# -------------------- MAIN WORK --------------------

def build_pages_from_master(df_all: pd.DataFrame) -> None:
    """
    Render each Markdown page using its template and the filtered rows from df_all.
    """
    # Ensure required columns exist
    for col in CANON_COLS:
        if col not in df_all.columns:
            df_all[col] = ""

    # Normalize Type once and ensure images
    df_all["_NormType"] = df_all["Type"].apply(normalize_type)
    df_all["Image"] = df_all.apply(ensure_image_thumb, axis=1)

    for markdown_filename, want_type in MD_TO_TYPE.items():
        print(f"\n==> Building {markdown_filename} from master CSV (type == {want_type})")

        page_df = df_all[df_all["_NormType"] == want_type].copy()

        # Load template
        template_path = TEMPLATE_DIR / f"{markdown_filename}.template"
        try:
            with open(template_path, "r", encoding="utf-8") as f:
                md = f.read()
        except FileNotFoundError:
            print(f"Template not found: {template_path}. Skipping.")
            continue

        start_c = "<!-- START -->"
        stop_c = "<!-- STOP -->"
        i1 = md.find(start_c)
        i2 = md.find(stop_c, i1)
        if i1 == -1 or i2 == -1:
            print(f"No START/STOP markers in {markdown_filename}. Skipping.")
            continue

        block = md[i1 + len(start_c): i2].strip()
        generated = ""

        # --- Per-page grouping logic (mirrors your original code) ---

        if markdown_filename == "datasets.md":
            # by known subsections in a fixed order
            if "Subsection" not in page_df.columns:
                page_df["Subsection"] = "Contexts (Environment & Climate)"

            sections_to_show = [
                "Contexts (Environment & Climate)",
                "Contexts (Misc Data & APIs)",
                "Contexts (Population Data & Mobility)",
                "Events",
            ]
            for section in sections_to_show:
                sub_df = page_df[page_df["Subsection"] == section].copy()
                if not sub_df.empty:
                    sub_df = sub_df.sort_values(["Title"]).reset_index(drop=True)
                    generated += f'\n\n<p class="dataset-subsection">{section}</p>\n\n'
                    for _, row in sub_df.iterrows():
                        generated += substitute_placeholders(block, row) + "\n\n"

        elif markdown_filename == "methods.md":
            # group by Year (old → new), then Title
            if "Year" not in page_df.columns:
                page_df["Year"] = ""
            page_df["_YearInt"] = page_df["Year"].apply(_parse_year)
            page_df = page_df.sort_values(by=["_YearInt", "Title"], ascending=[True, True])

            years = [y for y in page_df["_YearInt"].dropna().unique()]
            for y in years:
                sub_df = page_df[page_df["_YearInt"] == y].copy()
                if not sub_df.empty:
                    generated += f"\n\n<p class=\"paper-year\">{int(y)}</p>\n\n"
                    for _, row in sub_df.iterrows():
                        generated += substitute_placeholders(block, row) + "\n\n"

            unk_df = page_df[page_df["_YearInt"].isna()].copy()
            if not unk_df.empty:
                generated += "\n\n<p class=\"paper-year\">Unknown Year</p>\n\n"
                unk_df = unk_df.sort_values(["Title"]).reset_index(drop=True)
                for _, row in unk_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"

        elif markdown_filename == "conferences.md":
            # Subsection ∈ {conference, journal}
            if "Subsection" not in page_df.columns:
                page_df["Subsection"] = "journal"
            page_df["Subsection"] = page_df["Subsection"].apply(_standardize_subsection)
            order = ["conference", "journal"]
            labels = {"conference": "Conferences", "journal": "Journals"}
            for sec in order:
                sub_df = page_df[page_df["Subsection"] == sec].copy()
                if not sub_df.empty:
                    sub_df = sub_df.sort_values(["Title"]).reset_index(drop=True)
                    generated += f'\n\n<p class="venue-subsection">{labels[sec]}</p>\n\n'
                    for _, row in sub_df.iterrows():
                        generated += substitute_placeholders(block, row) + "\n\n"

        else:
            # Default: simple stream in Title order
            page_df = page_df.sort_values(["Title"]).reset_index(drop=True)
            for _, row in page_df.iterrows():
                generated += substitute_placeholders(block, row) + "\n\n"

        # Write back into the START/STOP block and save to docs/<markdown_filename>
        new_block = f"{start_c}\n{generated.strip()}\n{stop_c}"
        md = md[:i1] + new_block + md[i2 + len(stop_c):]
        out_path = OUTPUT_DIR / markdown_filename
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"Updated {out_path}")
        except Exception as e:
            print(f"Error writing {out_path}: {e}")


def export_yaml_rows(df_all: pd.DataFrame) -> None:
    """
    Emit one YAML file per CSV row using filename:
        <simplified(Type)>_<simplified(Title)>.yaml
    Only the canonical columns are included in the YAML content.
    """
    print("\n==> Writing per-row YAML files")
    # Ensure required columns exist (defensive)
    for col in CANON_COLS:
        if col not in df_all.columns:
            df_all[col] = ""

    for _, row in df_all.iterrows():
        type_part = simplify_for_filename(row.get("Type", "unknown"), max_len=30)
        title_part = simplify_for_filename(row.get("Title", "unknown"), max_len=30)
        base_name = f"{type_part}_{title_part}.yaml"
        out_yaml = ensure_unique_path(YAML_OUT_DIR, base_name)

        data = {col: row.get(col, "") for col in CANON_COLS}
        with open(out_yaml, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

    print(f"YAML rows written to: {YAML_OUT_DIR}")


def main():
    if not MASTER_CSV.exists():
        raise FileNotFoundError(f"Master CSV not found: {MASTER_CSV}")

    print(f"Loading master CSV: {MASTER_CSV}")
    df_all = load_master_csv(MASTER_CSV)

    # Build pages
    build_pages_from_master(df_all)

    # YAML per-row export
    export_yaml_rows(df_all)

    print("\nAll tasks completed successfully.")


if __name__ == "__main__":
    main()
