"""
Parser module - handles user input parsing.
"""

from pathlib import Path
from typing import Optional


def parse_topic_brief(brief: str) -> dict:
    """
    Parse a raw topic brief into structured components.

    Args:
        brief: Raw topic description string.

    Returns:
        Dictionary with extracted components (title, keywords, etc.).
    """
    # Placeholder: simple extraction
    lines = [line.strip() for line in brief.splitlines() if line.strip()]
    title = lines[0] if lines else brief

    return {
        "title": title,
        "raw": brief,
        "lines": lines,
    }


def load_notes(filepath: str) -> Optional[str]:
    """
    Load notes from a file.

    Args:
        filepath: Path to the notes file.

    Returns:
        File contents as string, or None if file not found.
    """
    path = Path(filepath)
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
