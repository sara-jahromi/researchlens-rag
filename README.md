# ResearchLens

A RAG assistant that ingests AI/ML research papers, retrieves relevant
passages, and answers technical questions with verifiable citations.

## Status
- [x] Phase 0 — Project setup (venv, git, GitHub)
- [x] Phase 1 — PDF ingestion (page-aware text extraction via PyMuPDF)
- [x] Phase 2 — Chunking and metadata design (fixed-size word windows, page-aware)
- [ ] Phase 3 — Embeddings and vector search

## Setup
\`\`\`
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Usage
Extract text from a PDF in \`data/\`:
\`\`\`
python -m src.researchlens.ingest
\`\`\`
Chunk the extracted pages into retrieval units:
\`\`\`
python -m src.researchlens.chunk
\`\`\`

## Project layout
- \`src/researchlens/ingest.py\` — PDF → page-aware cleaned text
- \`src/researchlens/chunk.py\` — pages → citation-ready text chunks
- \`data/\` — raw PDFs (gitignored)
- \`tests/\` — test suite
