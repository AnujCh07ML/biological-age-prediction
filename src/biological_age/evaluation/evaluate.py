from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def evaluate_model(
    y_true,
    y_pred,
):
    """
    Evaluate regression model performance.
    """

    mae = mean_absolute_error(
        y_true,
        y_pred,
    )

    rmse = mean_squared_error(
        y_true,
        y_pred,
        squared=False,
    )

    r2 = r2_score(
        y_true,
        y_pred,
    )

    metrics = {
        "mae": mae,
        "rmse": rmse,
        "r2": r2,
    }

    return metrics
