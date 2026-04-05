# Architecture Notes

This scaffold splits the MVP into four conservative areas:

- `src/capture/`: manual, reviewable data collection interfaces.
- `src/data/`: schemas, validation, and offline dataset helpers.
- `src/model/`: baseline training and inference surfaces for offline experiments.
- `src/eval/`: repeatable evaluation over saved artifacts and fixtures.

## Design Intent

- Prefer offline-first workflows.
- Keep desktop interaction separate from model training and evaluation.
- Treat any future capture mechanism as a narrow, explicit boundary.
- Make it easy to replace stubs with real implementations without changing layout.

## MVP Flow

1. User explicitly starts a manual capture session.
2. Approved samples are written to local files under `sandbox/` or curated into `data/`.
3. Data validation normalizes examples into a stable training format.
4. Baseline training runs on stored examples only.
5. Evaluation reports metrics on fixed datasets.
