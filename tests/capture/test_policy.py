"""Tests for capture safety policy defaults."""

from capture.policy import DEFAULT_CAPTURE_POLICY


def test_default_capture_policy_is_manual_only() -> None:
    assert DEFAULT_CAPTURE_POLICY.manual_only is True
    assert DEFAULT_CAPTURE_POLICY.allow_live_control is False
    assert DEFAULT_CAPTURE_POLICY.allow_credentials_handling is False
