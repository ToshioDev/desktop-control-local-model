from pathlib import Path

from data.schemas import TrainingExample, validate_example


def test_validate_example_accepts_valid_sample() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/screenshot.png"),
        instruction="Open settings",
        action_label="click_settings",
        metadata={"source": "manual"},
    )

    validate_example(example)


def test_validate_example_rejects_empty_instruction() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/screenshot.png"),
        instruction=" ",
        action_label="click_settings",
    )

    try:
        validate_example(example)
    except ValueError as exc:
        assert "instruction" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty instruction")


def test_validate_example_rejects_empty_action_label() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/screenshot.png"),
        instruction="Open settings",
        action_label=" ",
    )

    try:
        validate_example(example)
    except ValueError as exc:
        assert "action_label" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty action_label")


def test_validate_example_rejects_invalid_image_path_type() -> None:
    example = TrainingExample(
        image_path="sandbox/screenshot.png",  # type: ignore[arg-type]
        instruction="Open settings",
        action_label="click_settings",
    )

    try:
        validate_example(example)
    except TypeError as exc:
        assert "pathlib.Path" in str(exc)
    else:
        raise AssertionError("Expected TypeError for invalid image_path type")


def test_validate_example_rejects_empty_image_path_name() -> None:
    example = TrainingExample(
        image_path=Path("."),
        instruction="Open settings",
        action_label="click_settings",
    )

    try:
        validate_example(example)
    except ValueError as exc:
        assert "image_path" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty image path name")


def test_validate_example_rejects_non_string_metadata_value() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/screenshot.png"),
        instruction="Open settings",
        action_label="click_settings",
        metadata={"turn": 1},  # type: ignore[dict-item]
    )

    try:
        validate_example(example)
    except ValueError as exc:
        assert "metadata values" in str(exc)
    else:
        raise AssertionError("Expected ValueError for non-string metadata value")


def test_validate_example_rejects_blank_metadata_key() -> None:
    example = TrainingExample(
        image_path=Path("sandbox/screenshot.png"),
        instruction="Open the settings menu",
        action_label="click_settings",
        metadata={"   ": "manual"},
    )

    try:
        validate_example(example)
    except ValueError as exc:
        assert "metadata keys" in str(exc)
    else:
        raise AssertionError("Expected ValueError for blank metadata key")
