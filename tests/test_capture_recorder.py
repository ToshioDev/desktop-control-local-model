from capture.policy import CapturePolicy
from capture import recorder


def test_prepare_capture_session_creates_directory(tmp_path) -> None:
    target = tmp_path / "session"

    result = recorder.prepare_capture_session(target)

    assert result == target
    assert target.exists()
    assert target.is_dir()


def test_prepare_capture_session_blocks_when_policy_not_manual(monkeypatch) -> None:
    monkeypatch.setattr(recorder, "DEFAULT_CAPTURE_POLICY", CapturePolicy(manual_only=False))

    try:
        recorder.prepare_capture_session("sandbox/session")
    except RuntimeError as exc:
        assert "manual-only" in str(exc)
    else:
        raise AssertionError("Expected RuntimeError when manual_only is False")


def test_record_example_is_explicitly_not_implemented() -> None:
    try:
        recorder.record_example()
    except NotImplementedError as exc:
        assert "user-approved capture flow" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from record_example")
