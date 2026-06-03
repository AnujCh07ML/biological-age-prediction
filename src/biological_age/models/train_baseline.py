from sklearn.ensemble import RandomForestRegressor


def train_baseline_model(
    preprocessor,
    X_train,
    X_test,
    y_train,
    random_state: int = 42,
):
    """
    Train baseline Random Forest model.

    Parameters
    ----------
    preprocessor : ColumnTransformer
        Preprocessing pipeline.

    X_train : pd.DataFrame
        Training features.

    X_test : pd.DataFrame
        Test features.

    y_train : pd.Series
        Training target.

    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    tuple
        (
            model,
            fitted_preprocessor,
            X_train_processed,
            X_test_processed,
            y_pred,
        )
    """

    # -----------------------------
    # Fit preprocessor on train only
    # -----------------------------

    X_train_processed = (
        preprocessor.fit_transform(X_train)
    )

    X_test_processed = (
        preprocessor.transform(X_test)
    )

    # -----------------------------
    # Train Random Forest
    # -----------------------------

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=random_state,
        n_jobs=-1,
    )

    model.fit(
        X_train_processed,
        y_train,
    )

    # -----------------------------
    # Predict on test set
    # -----------------------------

    y_pred = model.predict(
        X_test_processed
    )

    return (
        model,
        preprocessor,
        y_pred,
    )
