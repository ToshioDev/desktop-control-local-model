"""Offline dataset utilities."""

from __future__ import annotations

import json
from pathlib import Path

from data.schemas import TrainingExample, validate_example


def dataset_root(root: str | Path = "data") -> Path:
    """Return the local dataset root directory."""

    return Path(root)


def load_dataset_manifest(
    manifest_path: str | Path,
    *,
    require_image_files: bool = False,
) -> list[TrainingExample]:
    """Load and validate training examples from a local JSONL manifest.

    Each non-empty line in the manifest must be a JSON object with:
    - image_path (str)
    - instruction (str)
    - action_label (str)
    - metadata (optional dict[str, str])
    """

    path = Path(manifest_path)
    lines = path.read_text(encoding="utf-8").splitlines()

    examples: list[TrainingExample] = []
    for line_number, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if not stripped:
            continue

        try:
            payload = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON in dataset manifest at line {line_number}: {exc.msg}"
            ) from exc

        if not isinstance(payload, dict):
            raise ValueError(f"Manifest line {line_number} must be a JSON object")

        metadata = payload.get("metadata", {})
        if not isinstance(metadata, dict):
            raise ValueError(f"Manifest line {line_number} metadata must be a JSON object")

        try:
            image_path = payload["image_path"]
            instruction = payload["instruction"]
            action_label = payload["action_label"]
        except KeyError as exc:
            raise ValueError(f"Manifest line {line_number} missing required field: {exc.args[0]}") from exc

        if not isinstance(image_path, str):
            raise ValueError(f"Manifest line {line_number} image_path must be a string")
        if not image_path.strip():
            raise ValueError(f"Manifest line {line_number} image_path must be non-empty")
        if not isinstance(instruction, str):
            raise ValueError(f"Manifest line {line_number} instruction must be a string")
        if not isinstance(action_label, str):
            raise ValueError(f"Manifest line {line_number} action_label must be a string")

        image_path_obj = Path(image_path)
        if not image_path_obj.is_absolute():
            image_path_obj = path.parent / image_path_obj

        if require_image_files and not image_path_obj.is_file():
            raise ValueError(
                f"Manifest line {line_number} image file not found: {image_path_obj}"
            )

        example = TrainingExample(
            image_path=image_path_obj,
            instruction=instruction,
            action_label=action_label,
            metadata=metadata,
        )

        try:
            validate_example(example)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid example at manifest line {line_number}: {exc}") from exc

        examples.append(example)

    if not examples:
        raise ValueError("Dataset manifest contains no examples")

    return examples
