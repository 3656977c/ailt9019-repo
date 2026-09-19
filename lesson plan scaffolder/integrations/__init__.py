"""
Integration layer for external services.

This package contains hooks for future integrations such as:
- LLM providers (OpenAI, Anthropic, local models)
- Cloud storage (Google Drive, Dropbox, OneDrive)
- Learning Management Systems (Canvas, Moodle, Blackboard)
- Calendar / scheduling services

None of these are wired up yet. See README.md for integration plans.
"""

from .base import IntegrationBase
from .config import IntegrationConfig

__all__ = ["IntegrationBase", "IntegrationConfig"]
