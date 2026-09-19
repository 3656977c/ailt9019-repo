"""
Placeholder for LLM (Large Language Model) integration.

Future: wire this up to generate richer lesson content, suggest activities,
and personalize plans based on student profiles.
"""

from typing import Any, Dict, Optional
from .base import IntegrationBase


class LLMProvider(IntegrationBase):
    """
    Abstract interface for LLM-powered enhancements.

    Planned providers:
        - OpenAI (GPT-4, GPT-3.5)
        - Anthropic (Claude)
        - Local / self-hosted models (Ollama, llama.cpp)
    """

    name = "llm_provider"

    def validate(self) -> bool:
        # TODO: check API key / endpoint availability
        return False

    def health_check(self) -> Dict[str, Any]:
        return {
            "status": "not_configured",
            "message": "LLM provider not integrated yet.",
        }

    def generate_content(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
    ) -> str:
        """
        Send a prompt to the LLM and return the generated text.

        Args:
            prompt: The input prompt.
            temperature: Sampling temperature (0.0 - 1.0).
            max_tokens: Maximum tokens to generate.

        Returns:
            Generated text string.
        """
        raise NotImplementedError("LLM integration not wired up yet.")

    def suggest_activities(self, topic: str, level: str = "intermediate") -> list:
        """
        Ask the LLM to suggest interactive activities for a topic.

        Args:
            topic: Lesson topic.
            level: Target student level.

        Returns:
            List of activity descriptions.
        """
        raise NotImplementedError("LLM integration not wired up yet.")
