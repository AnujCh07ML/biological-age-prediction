DEMOGRAPHIC_FEATURES = [
    "sex",
    "age_years",
    "race_ethnicity",
    "education_level",
    "poverty_income_ratio",
]


METABOLIC_FEATURES = [
    "albumin",
    "blood_urea_nitrogen",
    "creatinine",
    "uric_acid",
    "fasting_glucose",
    "hba1c_percent",
    "fasting_insulin",
]


LIPID_FEATURES = [
    "total_cholesterol",
    "hdl_cholesterol",
    "ldl_cholesterol_si",
    "triglycerides",
]


CBC_FEATURES = [
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
]


ELECTROLYTE_FEATURES = [
    "calcium",
    "sodium_si",
    "potassium_si",
    "phosphorus",
]


LIVER_FEATURES = [
    "total_bilirubin",
    "total_protein",
    "globulin",
    "ggt_si",
]


FASTING_FEATURES = [
    "fasting_hours",
]


KEEP_COLUMNS = (
    DEMOGRAPHIC_FEATURES
    + METABOLIC_FEATURES
    + LIPID_FEATURES
    + CBC_FEATURES
    + ELECTROLYTE_FEATURES
    + LIVER_FEATURES
    + FASTING_FEATURES
)


def select_features(df):
    """
    Select curated modeling features.
    """

    missing_features = [
        col for col in KEEP_COLUMNS
        if col not in df.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing features: {missing_features}"
        )

    return df[KEEP_COLUMNS]
