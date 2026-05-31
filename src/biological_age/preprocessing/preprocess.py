from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# =====================================
# Target Variable
# =====================================

TARGET_COLUMN = "age_years"


# =====================================
# Numeric Features
# =====================================

NUMERIC_FEATURES = [
    "albumin",
    "blood_urea_nitrogen",
    "creatinine",
    "uric_acid",
    "hba1c_percent",
    "total_cholesterol",
    "hdl_cholesterol",
    "triglycerides",
    "white_blood_cell_count",
    "lymphocyte_percent",
    "monocyte_percent",
    "neutrophil_percent",
    "red_blood_cell_count",
    "hemoglobin",
    "hematocrit",
    "mean_corpuscular_volume",
    "red_cell_distribution_width",
    "platelet_count",
    "calcium",
    "sodium_si",
    "potassium_si",
    "phosphorus",
    "total_bilirubin",
    "total_protein",
    "globulin",
    "ggt_si",
]


# =====================================
# Categorical Features
# =====================================

CATEGORICAL_FEATURES = [
    "sex",
]


# =====================================
# All Modeling Features
# =====================================

FEATURE_COLUMNS = (
    NUMERIC_FEATURES
    + CATEGORICAL_FEATURES
)


# =====================================
# Numeric Preprocessing Pipeline
# =====================================

numeric_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median"),
    ),
    (
        "scaler",
        StandardScaler(),
    ),
])


# =====================================
# Categorical Preprocessing Pipeline
# =====================================

categorical_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(
            strategy="most_frequent",
        ),
    ),
])


# =====================================
# Full Preprocessor
# =====================================

def build_preprocessor():
    """
    Build preprocessing pipeline for
    biological age modeling.
    """

    preprocessor = ColumnTransformer([
        (
            "numeric",
            numeric_pipeline,
            NUMERIC_FEATURES,
        ),
        (
            "categorical",
            categorical_pipeline,
            CATEGORICAL_FEATURES,
        ),
    ])

    return preprocessor


# =====================================
# Feature / Target Split
# =====================================

def split_features_target(df):
    """
    Split dataframe into features (X)
    and target (y).
    """

    X = df[FEATURE_COLUMNS]

    y = df[TARGET_COLUMN]

    return X, y
