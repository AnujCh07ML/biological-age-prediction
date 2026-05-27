from pathlib import Path

import pandas as pd
import yaml

from biological_age.data.make_interim import (
    run_make_interim,
)

from biological_age.data.create_datasets import (
    create_dataset,
    save_dataset,
)

from biological_age.features.column_mapping import (
    validate_columns,
    rename_columns,
)

from biological_age.features.feature_selection import (
    select_features,
)


from biological_age.preprocessing.missingness import (
    calculate_missingness,
)


def load_config(
    config_path: str = "config.yaml",
) -> dict:
    """
    Load project configuration file.
    """

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config


def main():
    """
    Main pipeline entrypoint.
    """

    # -----------------------------------
    # Step 0: Load configuration
    # -----------------------------------

    print("\n[INFO] Loading configuration...")

    config = load_config()

    # -----------------------------------
    # Step 1: Build interim dataset
    # -----------------------------------

    print("\n[INFO] Running interim pipeline...")

    run_make_interim(config)

    # -----------------------------------
    # Step 2: Load interim dataset
    # -----------------------------------

    interim_path = Path(
        config["paths"]["interim"]
    )

    print(
        f"\n[INFO] Loading interim dataset:\n"
        f"{interim_path}"
    )

    df = pd.read_parquet(interim_path)

    # -----------------------------------
    # Step 3: Validate raw columns
    # -----------------------------------

    print(
        "\n[INFO] Validating raw NHANES columns..."
    )

    validate_columns(df)

    print(
        "[INFO] Column validation passed."
    )

    # -----------------------------------
    # Step 4: Rename columns
    # -----------------------------------

    print(
        "\n[INFO] Renaming columns..."
    )

    df = rename_columns(df)

    print(
        "[INFO] Column renaming completed."
    )

    # -----------------------------------
    # Step 4.a: Create feature selection subset
    # -----------------------------------

    print(
        "\n[INFO] Selecting curated features..."
    )

    df = select_features(df)

    print(
        f"[INFO] Selected feature count: "
        f"{df.shape[1]}"
    )

    # -----------------------------------
    # Step 4.b: Missingness analysis
    # -----------------------------------

    print(
        "\n[INFO] Calculating missingness..."
    )

    missingness = calculate_missingness(df)

    report_path = Path(
        "outputs/reports/missingness_report.csv"
    )

    report_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    missingness.to_csv(report_path)

    print(
        f"[INFO] Missingness report saved:\n"
        f"{report_path}"
    )

    # -----------------------------------
    # Step 5: Create processed dataset
    # -----------------------------------

    print(
        "\n[INFO] Creating processed dataset..."
    )

    processed_df = create_dataset(df)

    # -----------------------------------
    # Step 6: Save processed dataset
    # -----------------------------------

    processed_path = Path(
        config["paths"]["processed"]
    )

    print(
        f"\n[INFO] Saving processed dataset:\n"
        f"{processed_path}"
    )

    save_dataset(
        processed_df,
        processed_path,
    )

    # -----------------------------------
    # Pipeline completed
    # -----------------------------------

    print(
        "\n[INFO] Full data pipeline completed."
    )


if __name__ == "__main__":
    main()
