"""Tests for training example schema validation."""

from pathlib import Path

import pytest

from data.schemas import TrainingExample, validate_example


def test_validate_example_accepts_non_empty_fields() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/sample.png"),
        instruction="Click submit",
        action_label="click_submit",
    )

    validate_example(example)


@pytest.mark.parametrize(
    ("instruction", "action_label", "expected_error"),
    [
        ("", "click_submit", "instruction must be non-empty"),
        ("Click submit", "", "action_label must be non-empty"),
    ],
)
def test_validate_example_rejects_empty_core_fields(
    instruction: str, action_label: str, expected_error: str
) -> None:
    example = TrainingExample(
        image_path=Path("sandbox/sample.png"),
        instruction=instruction,
        action_label=action_label,
    )

    with pytest.raises(ValueError, match=expected_error):
        validate_example(example)
