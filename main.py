from pathlib import Path

import pandas as pd
import yaml

import json
import joblib

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.pipeline import Pipeline

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

from biological_age.preprocessing.preprocess import (
    build_preprocessor,
    split_features_target,
)

from biological_age.split.train_test_split import (
    create_train_test_split,
)

from biological_age.models.train_baseline import (
    train_model,
)

from biological_age.evaluation.evaluate import (
    evaluate_model,
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
    # Step 5: Feature selection
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
    # Step 6: Missingness analysis
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

    missingness_df = (
        missingness
        .reset_index()
    )

    missingness_df.columns = [
        "feature",
        "missing_ratio",
    ]

    missingness_df.to_csv(
        report_path,
        index=False,
    )

    print(
        f"[INFO] Missingness report saved:\n"
        f"{report_path}"
    )

    # -----------------------------------
    # Step 7: Create processed dataset
    # -----------------------------------

    print(
        "\n[INFO] Creating processed dataset..."
    )

    processed_df = create_dataset(df)

    # -----------------------------------
    # Step 8: Save processed dataset
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
    # Step 9: Split features and target
    # -----------------------------------

    print(
        "\n[INFO] Splitting features and target..."
    )

    X, y = split_features_target(
        processed_df
    )

    print(
        f"[INFO] Features shape: {X.shape}"
    )

    print(
        f"[INFO] Target shape: {y.shape}"
    )

    # -----------------------------------
    # Step 10: Train/Test Split
    # -----------------------------------

    print(
        "\n[INFO] Creating train/test split..."
    )

    (
        X_train,
        X_test,
        y_train,
        y_test,
    ) = create_train_test_split(
        X,
        y,
    )

    print(
        f"[INFO] X_train shape: {X_train.shape}"
    )

    print(
        f"[INFO] X_test shape: {X_test.shape}"
    )

    # -----------------------------------
    # Step 11: Build preprocessor
    # -----------------------------------

    print(
        "\n[INFO] Building preprocessing pipeline..."
    )

    preprocessor = (
        build_preprocessor()
    )

    # -----------------------------------
    # Step 12: Define models
    # -----------------------------------

    models = {
        "rf": RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1,
        ),
        "xgb": XGBRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=6,
            random_state=42,
            n_jobs=-1,
        ),
        "lgbm": LGBMRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=6,
            random_state=42,
            n_jobs=-1,
        ),
    }

    # -----------------------------------
    # Step 13: Train and evaluate models
    # -----------------------------------

    comparison_results = {}

    for model_name, estimator in models.items():

        print(
            f"\n[INFO] Training {model_name.upper()}..."
        )

        # fresh preprocessor
        preprocessor = build_preprocessor()

        (
            model,
            preprocessor,
            y_pred,
        ) = train_model(
            estimator=estimator,
            preprocessor=preprocessor,
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
        )

        # -----------------------------------
        # Save model
        # -----------------------------------

        model_path = Path(
            f"models/{model_name}_model.pkl"
        )

        model_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            model,
            model_path,
        )

        print(
            f"[INFO] Model saved: {model_path}"
        )

        # -----------------------------------
        # Evaluate model
        # -----------------------------------

        metrics = evaluate_model(
            y_test,
            y_pred,
        )

        comparison_results[
            model_name
        ] = metrics

        # -----------------------------------
        # Print metrics
        # -----------------------------------

        print(
            f"\n{model_name.upper()} Results"
        )

        print(
            f"MAE : {metrics['mae']:.2f}"
        )

        print(
            f"RMSE: {metrics['rmse']:.2f}"
        )

        print(
            f"R²  : {metrics['r2']:.4f}"
        )

    # -----------------------------------
    # Step 14: Save comparison metrics
    # -----------------------------------

    metrics_path = Path(
        "outputs/metrics/model_comparison.json"
    )

    metrics_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        metrics_path,
        "w",
    ) as file:
        json.dump(
            comparison_results,
            file,
            indent=4,
        )

    print(
        f"\n[INFO] Metrics saved:\n"
        f"{metrics_path}"
    )

    # -----------------------------------
    # Pipeline completed
    # -----------------------------------

    print(
        "\n[INFO] Full data pipeline completed."
    )


if __name__ == "__main__":
    main()
