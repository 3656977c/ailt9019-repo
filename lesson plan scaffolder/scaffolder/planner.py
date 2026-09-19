"""
Planner module - core logic for generating lesson plans.
"""

from typing import Optional, Dict, Any
from .parser import parse_topic_brief
from .template import DEFAULT_TEMPLATE


def generate_lesson_plan(
    topic: str,
    notes: Optional[str] = None,
    duration_minutes: int = 60,
) -> Dict[str, Any]:
    """
    Generate a first-draft lesson plan from a topic brief.

    Args:
        topic: The lesson topic or brief.
        notes: Optional additional notes.
        duration_minutes: Total lesson duration.

    Returns:
        Dictionary representing the lesson plan.
    """
    parsed = parse_topic_brief(topic)
    template = DEFAULT_TEMPLATE(duration_minutes)
    structure = template.get_structure()

    lesson_plan = {
        "title": parsed["title"],
        "duration_minutes": duration_minutes,
        "objectives": [],
        "materials": [],
        "structure": structure,
        "notes": notes,
    }

    # Auto-generate placeholder objectives based on title
    lesson_plan["objectives"] = [
        f"Understand the core concepts of {parsed['title']}.",
        f"Apply key principles of {parsed['title']} to simple examples.",
        f"Identify connections between {parsed['title']} and prior knowledge.",
    ]

    # Auto-generate placeholder materials
    lesson_plan["materials"] = [
        "Whiteboard / projector",
        "Handouts (if applicable)",
        "Practice problems or case studies",
    ]

    return lesson_plan
