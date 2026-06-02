from sklearn.model_selection import train_test_split


def create_train_test_split(
    X,
    y,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Create reproducible train/test split.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix.

    y : pd.Series
        Target variable.

    test_size : float, default=0.2
        Proportion of data allocated to the test set.

    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    tuple
        X_train, X_test, y_train, y_test
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
    )
