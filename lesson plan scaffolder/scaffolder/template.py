"""
Template module - defines lesson plan structures.
"""

from typing import List, Dict, Any


class LessonTemplate:
    """Base class for lesson plan templates."""

    def __init__(self, duration_minutes: int = 60):
        self.duration = duration_minutes

    def get_structure(self) -> List[Dict[str, Any]]:
        """
        Return the lesson structure as a list of sections.

        Each section is a dict with:
            - name: section name
            - duration: suggested time in minutes
            - description: what happens in this section
        """
        raise NotImplementedError


class StandardLessonTemplate(LessonTemplate):
    """A standard 60-minute lesson template."""

    def get_structure(self) -> List[Dict[str, Any]]:
        # Proportional time allocation
        intro_time = max(5, int(self.duration * 0.10))
        core_time = max(20, int(self.duration * 0.50))
        activity_time = max(10, int(self.duration * 0.25))
        wrap_time = max(5, self.duration - intro_time - core_time - activity_time)

        return [
            {
                "name": "Introduction & Hook",
                "duration": intro_time,
                "description": "Engage students, state learning objectives, connect to prior knowledge.",
            },
            {
                "name": "Core Content Delivery",
                "duration": core_time,
                "description": "Present key concepts, explain definitions, provide examples.",
            },
            {
                "name": "Interactive Activity / Practice",
                "duration": activity_time,
                "description": "Hands-on exercise, discussion, problem-solving, or group work.",
            },
            {
                "name": "Wrap-up & Review",
                "duration": wrap_time,
                "description": "Summarize key takeaways, preview next lesson, Q&A.",
            },
        ]


DEFAULT_TEMPLATE = StandardLessonTemplate
