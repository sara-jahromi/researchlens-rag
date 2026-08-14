# ResearchLens

A RAG assistant that ingests AI/ML research papers, retrieves relevant
passages, and answers technical questions with verifiable citations.

## Status
- [x] Phase 0 — Project setup (venv, git, GitHub)
- [x] Phase 1 — PDF ingestion (page-aware text extraction via PyMuPDF)
- [ ] Phase 2 — Chunking and metadata design

## Setup
## Usage
Extract text from a PDF in `data/`:
## Project layout
- `src/researchlens/ingest.py` — PDF → page-aware cleaned text
- `data/` — raw PDFs (gitignored)
- `tests/` — test suite
