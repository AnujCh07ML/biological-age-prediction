import pandas as pd


def calculate_missingness(df):
    """
    Calculate feature missingness ratios.
    """

    missingness = (
        df.isna()
        .mean()
        .sort_values(ascending=False)
    )

    return missingness
