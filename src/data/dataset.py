"""Offline dataset utilities."""

from pathlib import Path


def dataset_root(root: str | Path = "data") -> Path:
    """Return the local dataset root directory."""

    return Path(root)


def load_dataset_manifest(*_args, **_kwargs) -> list[dict[str, str]]:
    """Placeholder manifest loader.

    TODO: Load validated dataset metadata from a local manifest file.
    """

    raise NotImplementedError("Dataset manifest loading is not implemented yet.")
