from pathlib import Path

import pandas as pd


CRP_COLUMNS = [
    "HSCRP",
    "LBXHSCRP",
    "CRP",
    "HSV"
]


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Run basic validation checks on dataset integrity.
    """

    print("\n[INFO] Running dataset validation...")

    # Dataset shape
    print(f"[INFO] Dataset shape: {df.shape}")

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()
    print(f"[INFO] Duplicate rows: {duplicate_rows}")

    # Duplicate participant IDs
    if "SEQN" in df.columns:
        duplicate_seqn = df["SEQN"].duplicated().sum()
        print(f"[INFO] Duplicate SEQN values: {duplicate_seqn}")

    # Missing value summary
    missing_ratio = (
        df.isna()
        .mean()
        .sort_values(ascending=False)
    )

    print("\n[INFO] Top 10 columns by missing ratio:")
    print(missing_ratio.head(10))

    # Data type summary
    print("\n[INFO] Data type summary:")
    print(df.dtypes.value_counts())


def remove_crp_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove CRP-related columns permanently.
    """

    existing_crp_cols = [
        col for col in CRP_COLUMNS
        if col in df.columns
    ]

    if existing_crp_cols:
        df = df.drop(
            columns=existing_crp_cols,
            errors="ignore",
        )

        print(
            f"\n[INFO] Dropped CRP columns: "
            f"{existing_crp_cols}"
        )

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows and duplicate participants.
    """

    # Remove exact duplicate rows
    before_rows = len(df)

    df = df.drop_duplicates()

    after_rows = len(df)

    print(
        f"\n[INFO] Removed "
        f"{before_rows - after_rows} duplicate rows"
    )

    # Remove duplicate participant IDs
    if "SEQN" in df.columns:

        before_seqn = len(df)

        df = df.drop_duplicates(
            subset="SEQN",
        )

        after_seqn = len(df)

        print(
            f"[INFO] Removed "
            f"{before_seqn - after_seqn} "
            f"duplicate SEQN entries"
        )

    return df


def create_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main dataset creation pipeline.
    """

    print("\n[INFO] Creating processed dataset...")
    print(f"[INFO] Original shape: {df.shape}")

    # -----------------------------------
    # Remove rows with missing target
    # -----------------------------------

    missing_target = (
        df["age_years"]
        .isna()
        .sum()
    )

    if missing_target > 0:
        print(
            f"\n[INFO] Removing "
            f"{missing_target} rows with "
            f"missing age_years"
        )

        df = df.dropna(
            subset=["age_years"]
        )

    # -----------------------------------
    # Remove CRP-related columns
    # -----------------------------------

    df = remove_crp_columns(df)

    # -----------------------------------
    # Remove duplicate rows
    # -----------------------------------

    df = remove_duplicates(df)

    # -----------------------------------
    # Reset index
    # -----------------------------------

    df = df.reset_index(
        drop=True
    )

    print(
        f"\n[INFO] Final shape: {df.shape}"
    )

    # -----------------------------------
    # Validate dataset
    # -----------------------------------

    validate_dataset(df)

    return df


def save_dataset(df: pd.DataFrame, save_path: Path) -> None:
    """
    Save processed dataset as parquet.
    """

    save_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(save_path, index=False)

    print(f"\n[INFO] Dataset saved to:\n{save_path}")
