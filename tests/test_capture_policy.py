from capture.policy import CapturePolicy, DEFAULT_CAPTURE_POLICY


def test_default_capture_policy_is_locked_down() -> None:
    assert DEFAULT_CAPTURE_POLICY.manual_only is True
    assert DEFAULT_CAPTURE_POLICY.allow_live_control is False
    assert DEFAULT_CAPTURE_POLICY.allow_credentials_handling is False


def test_capture_policy_can_be_explicitly_configured() -> None:
    policy = CapturePolicy(
        manual_only=True,
        allow_live_control=False,
        allow_credentials_handling=False,
    )

    assert policy == DEFAULT_CAPTURE_POLICY
