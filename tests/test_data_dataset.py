import json
from pathlib import Path

from data.dataset import dataset_root, load_dataset_manifest


def test_dataset_root_from_string() -> None:
    assert dataset_root("data") == Path("data")


def test_dataset_root_from_path() -> None:
    root = Path("sandbox")
    assert dataset_root(root) == root


def test_load_dataset_manifest_returns_validated_examples(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.jsonl"
    record = {
        "image_path": "images/shot-001.png",
        "instruction": "Open settings",
        "action_label": "click_settings",
        "metadata": {"source": "manual"},
    }
    manifest.write_text(json.dumps(record) + "\n", encoding="utf-8")

    examples = load_dataset_manifest(manifest)

    assert len(examples) == 1
    assert examples[0].image_path == tmp_path / "images/shot-001.png"
    assert examples[0].instruction == "Open settings"


def test_load_dataset_manifest_rejects_empty_manifest(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.jsonl"
    manifest.write_text("\n", encoding="utf-8")

    try:
        load_dataset_manifest(manifest)
    except ValueError as exc:
        assert "contains no examples" in str(exc)
    else:
        raise AssertionError("Expected ValueError for empty dataset manifest")


def test_load_dataset_manifest_rejects_invalid_json_line(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.jsonl"
    manifest.write_text('{"image_path": "x.png"\n', encoding="utf-8")

    try:
        load_dataset_manifest(manifest)
    except ValueError as exc:
        assert "Invalid JSON" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid JSON line")


def test_load_dataset_manifest_rejects_invalid_example_fields(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.jsonl"
    bad_record = {
        "image_path": "images/shot-001.png",
        "instruction": "   ",
        "action_label": "click_settings",
    }
    manifest.write_text(json.dumps(bad_record) + "\n", encoding="utf-8")

    try:
        load_dataset_manifest(manifest)
    except ValueError as exc:
        assert "Invalid example" in str(exc)
        assert "instruction" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid example fields")
