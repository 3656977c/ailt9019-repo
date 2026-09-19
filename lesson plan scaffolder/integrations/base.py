"""
Abstract base class for all integrations.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class IntegrationBase(ABC):
    """
    Base class that all service integrations must inherit from.

    Provides a uniform interface so the core app can call integrations
    without knowing implementation details.
    """

    name: str = ""
    enabled: bool = False

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def validate(self) -> bool:
        """
        Check whether the integration is properly configured and reachable.

        Returns:
            True if ready to use, False otherwise.
        """
        ...

    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        """
        Return status info about the integration.

        Returns:
            Dict with keys like: status, message, latency_ms, etc.
        """
        ...
