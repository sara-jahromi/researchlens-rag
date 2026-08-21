"""Chunking: turn page-aware text into retrieval-sized, cited chunks."""

from dataclasses import dataclass

from .ingest import Page, ingest_pdf


@dataclass
class Chunk:
    """A retrieval unit: a slice of text that knows where it came from."""
    source: str
    page_number: int
    chunk_id: str
    text: str


def _window(words: list[str], chunk_size: int, overlap: int) -> list[str]:
    """Slide a fixed-size window over words, stepping by (size - overlap)."""
    assert overlap < chunk_size, "overlap must be smaller than chunk_size"
    step = chunk_size - overlap
    chunks: list[str] = []
    start = 0
    while start < len(words):
        window = words[start:start + chunk_size]
        chunks.append(" ".join(window))
        if start + chunk_size >= len(words):  # last window reached
            break
        start += step
    return chunks


def chunk_pages(
    pages: list[Page], chunk_size: int = 200, overlap: int = 40
) -> list[Chunk]:
    """Chunk each page independently so every chunk maps to one page."""
    chunks: list[Chunk] = []
    for page in pages:
        words = page.text.split()
        for i, text in enumerate(_window(words, chunk_size, overlap)):
            chunk_id = f"{page.source}:p{page.page_number}:c{i}"
            chunks.append(
                Chunk(
                    source=page.source,
                    page_number=page.page_number,
                    chunk_id=chunk_id,
                    text=text,
                )
            )
    return chunks


if __name__ == "__main__":
    pages = ingest_pdf("data/attention.pdf")
    chunks = chunk_pages(pages)
    print(f"{len(pages)} pages -> {len(chunks)} chunks\n")
    sample = chunks[3]  # peek at one chunk
    print(f"--- {sample.chunk_id} (page {sample.page_number}) ---")
    print(sample.text[:400])
