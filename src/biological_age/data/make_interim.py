from pathlib import Path
from typing import Dict, Any
import pandas as pd

from biological_age.data.load_data import load_all_data
from biological_age.data.merge_data import merge_all_years, combine_years


def build_interim_dataset(raw_dir: Path, threshold: float,) -> pd.DataFrame:
    """
    Build full NHANES dataset from raw data.

    Pipeline:
    RAW → load_all_data → merge_all_years → combine_years

    Parameters
    ----------
    raw_dir : Path
        Path to raw data directory

    Returns
    -------
    pd.DataFrame
        Fully merged dataset across all years
    """

    if not raw_dir.exists():
        raise FileNotFoundError(f"Raw directory not found: {raw_dir}")

    print("[INFO] Loading raw data...")
    data = load_all_data(raw_dir, threshold=threshold,)

    if not data:
        raise ValueError("No data loaded from raw directory.")

    print(f"[INFO] Loaded datasets: {len(data)} tables")

    print("[INFO] Merging features within each year...")
    merged_data = merge_all_years(data)

    print(f"[INFO] Years processed: {list(merged_data.keys())}")

    print("[INFO] Combining all years...")
    final_df = combine_years(merged_data)

    print(f"[INFO] Final dataset shape: {final_df.shape}")

    return final_df


def save_interim(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save dataset to parquet format.

    Parameters
    ----------
    df : pd.DataFrame
        Data to save
    output_path : Path
        Output file path
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(output_path, index=False)

    print(f"[INFO] Saved interim dataset to: {output_path}")


def run_make_interim(config: Dict[str, Any]) -> None:
    """
    Run full interim data pipeline.

    Parameters
    ----------
    config : dict
        Loaded config.yaml dictionary
    """

    try:
        raw_dir = Path(config["paths"]["raw"])
        output_path = Path(config["paths"]["interim"])
        threshold = float(config["data"]["invalid_numeric_threshold"])

    except KeyError as e:
        raise KeyError(f"Missing config key: {e}")

    print("[INFO] Starting interim pipeline...")

    df = build_interim_dataset(raw_dir, threshold=threshold,)

    save_interim(df, output_path)

    print("[INFO] Interim pipeline completed successfully.")
