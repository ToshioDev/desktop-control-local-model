from eval.metrics import accuracy, summarize_report


def test_accuracy_not_implemented() -> None:
    try:
        accuracy([], [])
    except NotImplementedError as exc:
        assert "not implemented yet" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from accuracy")


def test_summarize_report_not_implemented() -> None:
    try:
        summarize_report()
    except NotImplementedError as exc:
        assert "not implemented yet" in str(exc)
    else:
        raise AssertionError("Expected NotImplementedError from summarize_report")
