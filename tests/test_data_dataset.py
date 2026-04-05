from pathlib import Path

from data.dataset import dataset_root, load_dataset_manifest


def test_dataset_root_from_string() -> None:
    assert dataset_root("data") == Path("data")


def test_dataset_root_from_path() -> None:
    root = Path("sandbox")
    assert dataset_root(root) == root


def test_load_dataset_manifest_not_implemented() -> None:
    try:
        load_dataset_manifest()
    except NotImplementedError as exc:
        assert "not implemented yet" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from load_dataset_manifest")
