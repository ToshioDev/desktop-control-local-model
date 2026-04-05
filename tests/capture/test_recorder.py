"""Tests for capture session preparation safeguards."""

from pathlib import Path

import pytest

from capture import recorder
from capture.policy import CapturePolicy


def test_prepare_capture_session_creates_directory(tmp_path: Path) -> None:
    session_dir = tmp_path / "session"

    result = recorder.prepare_capture_session(session_dir)

    assert result == session_dir
    assert session_dir.exists()
    assert session_dir.is_dir()


def test_prepare_capture_session_rejects_non_manual_policy(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(recorder, "DEFAULT_CAPTURE_POLICY", CapturePolicy(manual_only=False))

    with pytest.raises(RuntimeError, match="manual-only"):
        recorder.prepare_capture_session(tmp_path / "session")
