"""Baseline model stub for offline training experiments."""

from dataclasses import dataclass


@dataclass(slots=True)
class BaselineModelConfig:
    """Configuration placeholder for a future baseline model."""

    name: str = "baseline-placeholder"
    device: str = "cpu"


class BaselineModel:
    """Minimal interface placeholder for training and prediction."""

    def __init__(self, config: BaselineModelConfig | None = None) -> None:
        self.config = config or BaselineModelConfig()

    def train(self) -> None:
        """Train on offline data only.

        TODO: Accept validated dataset objects and write checkpoints to
        `artifacts/checkpoints/`.
        """

        raise NotImplementedError("Offline training is not implemented yet.")

    def predict(self, *_args, **_kwargs) -> str:
        """Return a placeholder prediction for future offline inference."""

        raise NotImplementedError("Offline inference is not implemented yet.")
