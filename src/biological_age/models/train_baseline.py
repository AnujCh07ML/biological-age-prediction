from sklearn.ensemble import RandomForestRegressor


def train_model(
    estimator,
    preprocessor,
    X_train,
    X_test,
    y_train,
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

    print("\n=== RAW FEATURES ===")
    print(f"Number of raw features: {len(X_train.columns)}")

    for col in X_train.columns:
        print(col)

    X_train_processed = (
        preprocessor.fit_transform(X_train)
    )

    print("\n=== PROCESSED SHAPE ===")
    print(X_train_processed.shape)

    X_test_processed = (
        preprocessor.transform(X_test)
    )

    feature_names = (
        preprocessor.get_feature_names_out()
    )

    print("\n=== FIRST 20 FEATURES ===")

    for name in feature_names[:20]:
        print(name)

    print(
        f"\nTotal processed features: "
        f"{len(feature_names)}"
    )

    # -----------------------------
    # Train Model
    # -----------------------------

    estimator.fit(
        X_train_processed,
        y_train,
    )

    # -----------------------------
    # Predict on test set
    # -----------------------------

    y_pred = estimator.predict(
        X_test_processed
    )

    return (
        estimator,
        preprocessor,
        y_pred,
    )
