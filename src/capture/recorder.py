"""Manual capture stub.

Future implementations should collect approved offline training data only.
They should never perform autonomous desktop actions.
"""

from pathlib import Path

from capture.policy import DEFAULT_CAPTURE_POLICY


def prepare_capture_session(output_dir: str | Path) -> Path:
    """Create a local directory for a future manual capture session.

    This function is intentionally narrow: it only prepares the filesystem
    location for a human-triggered session. Actual capture logic is deferred.
    """

    if not DEFAULT_CAPTURE_POLICY.manual_only:
        raise RuntimeError("Capture must remain manual-only in this scaffold.")

    session_dir = Path(output_dir)
    session_dir.mkdir(parents=True, exist_ok=True)
    return session_dir


def record_example(*_args, **_kwargs) -> None:
    """Placeholder for a future manual example-recording interface."""

    raise NotImplementedError(
        "TODO: implement an explicit, user-approved capture flow that writes only "
        "offline artifacts and does not automate the live desktop."
    )
