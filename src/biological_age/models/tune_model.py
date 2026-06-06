from sklearn.model_selection import RandomizedSearchCV


def tune_model(
    estimator,
    param_grid,
    X_train,
    y_train,
):
    """
    Tune model using RandomizedSearchCV.
    """

    search = RandomizedSearchCV(
        estimator=estimator,
        param_distributions=param_grid,
        n_iter=25,
        cv=3,
        scoring="neg_mean_absolute_error",
        n_jobs=-1,
        random_state=42,
        verbose=2,
    )

    search.fit(
        X_train,
        y_train,
    )

    return search
