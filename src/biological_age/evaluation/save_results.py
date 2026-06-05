from pathlib import Path
import json
import joblib


def save_metrics(
    metrics: dict,
    output_path: Path,
) -> None:
    """
    Save metrics to JSON.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_path,
        "w",
    ) as f:
        json.dump(
            metrics,
            f,
            indent=4,
        )


def save_model(
    model,
    output_path: Path,
) -> None:
    """
    Save trained model artifact.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        model,
        output_path,
    )
