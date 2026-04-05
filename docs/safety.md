# Safety Guardrails

This repository is intentionally scaffold-only.

## Allowed Direction

- Manual dataset capture with explicit user approval.
- Offline preprocessing and model experimentation.
- Evaluation on saved fixtures and reports.

## Disallowed Direction For This MVP

- Autonomous control of the live desktop.
- Background monitoring or hidden capture.
- Credential entry, password storage, or token handling.
- Automated clicking, typing, or navigation against real user sessions.

## Implementation Guidance

- Keep future capture entry points interactive and obvious.
- Require local paths and explicit output directories.
- Default all experimental outputs to `sandbox/` or `artifacts/`.
- Add tests around data handling before adding any higher-risk capability.
