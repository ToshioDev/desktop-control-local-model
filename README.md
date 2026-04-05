# Desktop Control Local Model MVP Scaffold

This repository contains a conservative Python scaffold for a Windows-local desktop-control training prototype.

The current state is intentionally limited to safe, developer-friendly structure only. It does **not** implement autonomous live desktop control, credentials handling, browser/session automation, or any unattended action execution.

## Goals

- Provide a clean project layout for capture, data, model, and evaluation work.
- Make the next implementation steps obvious through small stubs and TODOs.
- Keep all future desktop interaction work opt-in, reviewable, and sandboxed.

## Non-Goals

- No background desktop agents.
- No remote control capabilities.
- No secret storage or credential flows.
- No live click/type automation against the real desktop.

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

## Project Layout

```text
.
|-- README.md
|-- pyproject.toml
|-- configs/
|-- docs/
|-- src/
|   |-- capture/
|   |-- data/
|   |-- eval/
|   `-- model/
|-- sandbox/
|-- data/
`-- artifacts/
```

## Recommended Next Steps

1. Implement a manual-only capture flow that records approved screenshots and human labels into `sandbox/` first.
2. Define dataset schemas and validation for examples before training code is added.
3. Add a tiny baseline model that operates on offline fixtures only.
4. Add evaluation scripts against fixed test samples, not a live desktop.

## Safety Notes

- Keep any future capture flow explicitly user-triggered and visibly bounded.
- Treat `sandbox/` as the only place for early experiments.
- Do not add credential collection or secret persistence to this repository.
- Review `docs/safety.md` before implementing anything that touches the desktop.
