from __future__ import annotations


def split_message(text: str, max_length: int) -> list[str]:
    if len(text) <= max_length:
        return [text]

    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for word in text.split():
        extra_len = len(word) + (1 if current else 0)
        if current_len + extra_len > max_length:
            chunks.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += extra_len

    if current:
        chunks.append(" ".join(current))

    return chunks
