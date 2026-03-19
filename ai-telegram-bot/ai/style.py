from __future__ import annotations


def add_style(text: str, prefix: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return prefix.strip()
    return "\n".join(f"{prefix}{line}" for line in lines)
