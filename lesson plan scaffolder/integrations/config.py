"""
Configuration management for integrations.
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG_PATH = Path(__file__).parent / "config.json"


class IntegrationConfig:
    """
    Loads and provides access to integration settings.

    Looks for config in this order:
    1. Environment variables (INTEGRATION_<NAME>_KEY)
    2. config.json file in this directory
    3. Default empty values
    """

    def __init__(self, config_path: Optional[Path] = None):
        self._path = config_path or DEFAULT_CONFIG_PATH
        self._data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if self._path.exists():
            import json
            return json.loads(self._path.read_text(encoding="utf-8"))
        return {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value by dot-notation key, e.g. 'llm.openai.api_key'."""
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value

    def get_env(self, name: str, default: Any = None) -> Any:
        """Read a value from an environment variable."""
        env_key = f"INTEGRATION_{name.upper().replace('.', '_')}"
        return os.getenv(env_key, default)

    def save(self, data: Dict[str, Any]) -> None:
        """Persist config to disk."""
        import json
        self._path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        self._data = data
