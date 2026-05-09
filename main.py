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
    # Step 3: Create processed dataset
    # -----------------------------------
    processed_df = create_dataset(df)

    # -----------------------------------
    # Step 4: Save processed dataset
    # -----------------------------------
    processed_path = Path(config["paths"]["processed"])

    save_dataset(processed_df, processed_path,)

    print(
        "\n[INFO] Full data pipeline completed."
    )


if __name__ == "__main__":
    main()
