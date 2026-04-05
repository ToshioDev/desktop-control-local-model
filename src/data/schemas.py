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

    if not example.instruction.strip():
        raise ValueError("instruction must be non-empty")
    if not example.action_label.strip():
        raise ValueError("action_label must be non-empty")
