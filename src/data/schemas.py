"""Core training example schemas."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class TrainingExample:
    """Represents one offline desktop-training sample."""

    image_path: Path
    instruction: str
    action_label: str
    metadata: dict[str, str] = field(default_factory=dict)


def validate_example(example: TrainingExample) -> None:
    """Run lightweight validation for a scaffold example."""

    if not isinstance(example.image_path, Path):
        raise TypeError("image_path must be a pathlib.Path")
    if not example.image_path.name:
        raise ValueError("image_path must point to a file")
    if not example.instruction.strip():
        raise ValueError("instruction must be non-empty")
    if not example.action_label.strip():
        raise ValueError("action_label must be non-empty")
    for key, value in example.metadata.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError("metadata keys must be non-empty strings")
        if not isinstance(value, str):
            raise ValueError("metadata values must be strings")
