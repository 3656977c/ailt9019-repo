#!/usr/bin/env python3
"""
Lesson Plan Scaffolder - Entry Point

Generates a first-draft lesson outline from a topic brief and optional notes.
"""

import argparse
import sys
from pathlib import Path

# Ensure scaffolder package is importable
sys.path.insert(0, str(Path(__file__).parent))

from scaffolder.planner import generate_lesson_plan
from scaffolder.formatter import format_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Generate a first-draft lesson plan from a topic brief."
    )
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="The lesson topic or brief description.",
    )
    parser.add_argument(
        "--notes",
        type=str,
        default=None,
        help="Path to a file containing additional notes.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/lesson_plan.md",
        help="Path to save the generated lesson plan.",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=60,
        help="Lesson duration in minutes (default: 60).",
    )

    args = parser.parse_args()

    # Load optional notes
    notes = None
    if args.notes:
        notes_path = Path(args.notes)
        if notes_path.exists():
            notes = notes_path.read_text(encoding="utf-8")
        else:
            print(f"Warning: Notes file not found: {args.notes}")

    # Generate lesson plan
    print(f"Generating lesson plan for: {args.topic}")
    lesson_plan = generate_lesson_plan(
        topic=args.topic,
        notes=notes,
        duration_minutes=args.duration,
    )

    # Format and save
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    markdown_output = format_markdown(lesson_plan)
    output_path.write_text(markdown_output, encoding="utf-8")

    print(f"Lesson plan saved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
