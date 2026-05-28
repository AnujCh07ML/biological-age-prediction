# =====================================
# Demographic Features
# =====================================

DEMOGRAPHIC_FEATURES = [
    "sex",
    "age_years",
]


# =====================================
# Metabolic Features
# =====================================

METABOLIC_FEATURES = [
    "albumin",
    "blood_urea_nitrogen",
    "creatinine",
    "uric_acid",
    "hba1c_percent",
]


# =====================================
# Lipid Features
# =====================================

LIPID_FEATURES = [
    "total_cholesterol",
    "hdl_cholesterol",
    "triglycerides",
]


# =====================================
# CBC / Hematology Features
# =====================================

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


# =====================================
# Electrolyte Features
# =====================================

ELECTROLYTE_FEATURES = [
    "calcium",
    "sodium_si",
    "potassium_si",
    "phosphorus",
]


# =====================================
# Liver Features
# =====================================

LIVER_FEATURES = [
    "total_bilirubin",
    "total_protein",
    "globulin",
    "ggt_si",
]


# =====================================
# Final Feature List
# =====================================

KEEP_COLUMNS = (
    DEMOGRAPHIC_FEATURES
    + METABOLIC_FEATURES
    + LIPID_FEATURES
    + CBC_FEATURES
    + ELECTROLYTE_FEATURES
    + LIVER_FEATURES
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
