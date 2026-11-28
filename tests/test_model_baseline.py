from model.baseline import BaselineModel, BaselineModelConfig


def test_baseline_model_uses_default_config() -> None:
    model = BaselineModel()

    assert isinstance(model.config, BaselineModelConfig)
    assert model.config.name == "baseline-placeholder"
    assert model.config.device == "cpu"


def test_baseline_model_accepts_custom_config() -> None:
    config = BaselineModelConfig(name="tiny", device="cpu")

    model = BaselineModel(config)

    assert model.config == config


def test_baseline_train_not_implemented() -> None:
    model = BaselineModel()

    try:
        model.train()
    except NotImplementedError as exc:
        assert "Offline training" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from BaselineModel.train")


def test_baseline_predict_not_implemented() -> None:
    model = BaselineModel()

    try:
        model.predict("anything")
    except NotImplementedError as exc:
        assert "Offline inference" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from BaselineModel.predict")
