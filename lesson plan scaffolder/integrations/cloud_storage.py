"""
Placeholder for cloud storage integration.

Future: enable saving / loading lesson plans from cloud providers.
"""

from typing import Any, Dict, Optional
from .base import IntegrationBase


class CloudStorage(IntegrationBase):
    """
    Abstract interface for cloud storage backends.

    Planned providers:
        - Google Drive
        - Dropbox
        - Microsoft OneDrive
        - AWS S3 (or compatible)
    """

    name = "cloud_storage"

    def validate(self) -> bool:
        # TODO: check OAuth token / credentials
        return False

    def health_check(self) -> Dict[str, Any]:
        return {
            "status": "not_configured",
            "message": "Cloud storage not integrated yet.",
        }

    def upload(self, filepath: str, remote_path: Optional[str] = None) -> str:
        """
        Upload a file to cloud storage.

        Args:
            filepath: Local file path.
            remote_path: Optional destination path in the cloud.

        Returns:
            URL or identifier of the uploaded file.
        """
        raise NotImplementedError("Cloud storage not wired up yet.")

    def download(self, remote_id: str, local_dir: str) -> str:
        """
        Download a file from cloud storage.

        Args:
            remote_id: File identifier in the cloud.
            local_dir: Directory to save the file.

        Returns:
            Local file path.
        """
        raise NotImplementedError("Cloud storage not wired up yet.")

    def list_files(self, folder: Optional[str] = None) -> list:
        """
        List files stored in the cloud.

        Args:
            folder: Optional folder path to filter by.

        Returns:
            List of file metadata dicts.
        """
        raise NotImplementedError("Cloud storage not wired up yet.")
