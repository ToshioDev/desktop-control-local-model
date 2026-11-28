"""Safety policy helpers for capture workflows."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CapturePolicy:
    """Defines the guardrails for any future capture implementation."""

    manual_only: bool = True
    allow_live_control: bool = False
    allow_credentials_handling: bool = False


DEFAULT_CAPTURE_POLICY = CapturePolicy()
