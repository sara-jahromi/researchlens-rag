"""PDF ingestion: turn a PDF into page-aware, cleaned text."""

from dataclasses import dataclass
from pathlib import Path

import fitz  # this is PyMuPDF


@dataclass
class Page:
    """One page of a document, with enough metadata to cite it later."""
    source: str      # filename, e.g. "attention.pdf"
    page_number: int # 1-based, human-friendly
    text: str        # cleaned text of this page


def clean_text(raw: str) -> str:
    """Light cleanup. We stay conservative here and do heavier work later."""
    # Collapse runs of spaces/tabs, strip each line, drop blank lines.
    lines = [line.strip() for line in raw.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def ingest_pdf(path: str | Path) -> list[Page]:
    """Extract every page of a PDF as a cleaned, page-numbered Page."""
    path = Path(path)
    pages: list[Page] = []

    with fitz.open(path) as doc:
        for i, page in enumerate(doc):
            raw = page.get_text()          # extract this page's text
            cleaned = clean_text(raw)
            if not cleaned:                # skip fully blank pages
                continue
            pages.append(
                Page(source=path.name, page_number=i + 1, text=cleaned)
            )

    return pages


if __name__ == "__main__":
    # Quick manual test: run this file directly to inspect output.
    result = ingest_pdf("data/attention.pdf")
    print(f"Extracted {len(result)} pages from attention.pdf\n")
    first = result[0]
    print(f"--- Page {first.page_number} of {first.source} ---")
    print(first.text[:600])   # first 600 chars so we can eyeball quality
