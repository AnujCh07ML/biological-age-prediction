COLUMN_MAPPING = {

    # =========================
    # IDENTIFIERS / SURVEY
    # =========================

    "SEQN": "participant_id",
    "SDDSRVYR": "survey_cycle",
    "RIDSTATR": "interview_exam_status",
    "year": "survey_year",

    # =========================
    # DEMOGRAPHICS
    # =========================

    "RIAGENDR": "sex",
    "RIDAGEYR": "age_years",
    "RIDAGEMN": "age_months",
    "RIDRETH1": "race_ethnicity_old",
    "RIDRETH3": "race_ethnicity",
    "RIDEXMON": "exam_season",
    "RIDEXAGY": "age_at_exam_years",
    "RIDEXAGM": "age_at_exam_months",
    "RIDEXPRG": "pregnancy_status",

    # =========================
    # SOCIOECONOMIC
    # =========================

    "DMDEDUC2": "education_level",
    "DMDEDUC3": "education_level_youth",
    "INDHHIN2": "household_income",
    "INDFMIN2": "family_income",
    "INDFMPIR": "poverty_income_ratio",

    # =========================
    # HOUSEHOLD
    # =========================

    "DMDHHSIZ": "household_size",
    "DMDFMSIZ": "family_size",
    "DMDHHSZA": "num_children_0_5",
    "DMDHHSZB": "num_children_6_17",
    "DMDHHSZE": "num_elderly_60_plus",

    "DMDHRGND": "household_reference_gender",
    "DMDHRAGE": "household_reference_age",
    "DMDHRBR4": "household_reference_birth_country",
    "DMDHREDU": "household_reference_education",
    "DMDHRMAR": "household_reference_marital_status",
    "DMDHSEDU": "spouse_education_level",

    # =========================
    # CITIZENSHIP / LOCATION
    # =========================

    "DMDBORN4": "country_of_birth",
    "DMDCITZN": "citizenship_status",
    "DMDYRSUS": "years_in_us",
    "DMDYRUSZ": "years_in_us_grouped",

    # =========================
    # MARITAL STATUS
    # =========================

    "DMDMARTL": "marital_status",
    "DMDMARTZ": "marital_status_grouped",

    # =========================
    # MILITARY
    # =========================

    "DMQMILIZ": "military_status",
    "DMQADFC": "active_duty_status",

    # =========================
    # LANGUAGE / INTERVIEW
    # =========================

    "SIALANG": "interview_language",
    "SIAPROXY": "interview_proxy_used",
    "SIAINTRP": "interview_interpreter_used",

    "FIALANG": "family_interview_language",
    "FIAPROXY": "family_proxy_used",
    "FIAINTRP": "family_interpreter_used",

    "MIALANG": "mec_interview_language",
    "MIAPROXY": "mec_proxy_used",
    "MIAINTRP": "mec_interpreter_used",

    "AIALANGA": "audio_language",

    # =========================
    # SURVEY WEIGHTS
    # =========================

    "WTINT2YR": "interview_weight_2yr",
    "WTMEC2YR": "mec_exam_weight_2yr",
    "WTSAF2YR": "fasting_subsample_weight",

    "WTINTPRP": "interview_weight_prepandemic",
    "WTMECPRP": "mec_weight_prepandemic",
    "WTSAFPRP": "fasting_subsample_weight_prepandemic",

    "SDMVPSU": "masked_psu",
    "SDMVSTRA": "masked_strata",

    # =========================
    # FASTING
    # =========================

    "PHAFSTHR": "fasting_hours",
    "PHAFSTMN": "fasting_minutes",

    # =========================
    # LIVER / PROTEIN
    # =========================

    "LBXSAL": "albumin",
    "LBDSALSI": "albumin_si",

    "LBXSATSI": "alt_si",
    "LBXSASSI": "ast_si",
    "LBXSAPSI": "alkaline_phosphatase_si",

    "LBXSTB": "total_bilirubin",
    "LBDSTBSI": "total_bilirubin_si",

    "LBXSTP": "total_protein",
    "LBDSTPSI": "total_protein_si",

    "LBXSGB": "globulin",
    "LBDSGBSI": "globulin_si",

    "LBXSGTSI": "ggt_si",

    # =========================
    # KIDNEY / METABOLIC
    # =========================

    "LBXSBU": "blood_urea_nitrogen",
    "LBDSBUSI": "blood_urea_nitrogen_si",

    "LBXSCR": "creatinine",
    "LBDSCRSI": "creatinine_si",

    "LBXSUA": "uric_acid",
    "LBDSUASI": "uric_acid_si",

    # =========================
    # ELECTROLYTES / MINERALS
    # =========================

    "LBXSCA": "calcium",
    "LBDSCASI": "calcium_si",

    "LBXSNASI": "sodium_si",
    "LBXSKSI": "potassium_si",
    "LBXSCLSI": "chloride_si",

    "LBXSOSSI": "osmolality_si",

    "LBXSPH": "phosphorus",
    "LBDSPHSI": "phosphorus_si",

    # =========================
    # LIPIDS
    # =========================

    "LBXSCH": "total_cholesterol",
    "LBDSCHSI": "total_cholesterol_si",

    "LBDHDD": "hdl_cholesterol",
    "LBDHDDSI": "hdl_cholesterol_si",

    "LBXSLDSI": "ldl_cholesterol_si",

    "LBXSGL": "triglycerides",
    "LBDSGLSI": "triglycerides_si",

    "LBXSTR": "triglycerides_alt",
    "LBDSTRSI": "triglycerides_alt_si",

    # =========================
    # DIABETES / GLUCOSE
    # =========================

    "LBXGLU": "fasting_glucose",
    "LBDGLUSI": "fasting_glucose_si",

    "LBXGH": "hba1c_percent",

    "LBXIN": "fasting_insulin",
    "LBDINSI": "fasting_insulin_si",

    # =========================
    # IRON
    # =========================

    "LBXSIR": "serum_iron",
    "LBDSIRSI": "serum_iron_si",

    # =========================
    # MUSCLE DAMAGE
    # =========================

    "LBXSCK": "creatine_kinase",

    # =========================
    # CBC / IMMUNE
    # =========================

    "LBXWBCSI": "white_blood_cell_count",

    "LBXLYPCT": "lymphocyte_percent",
    "LBXMOPCT": "monocyte_percent",
    "LBXNEPCT": "neutrophil_percent",
    "LBXEOPCT": "eosinophil_percent",
    "LBXBAPCT": "basophil_percent",

    "LBDLYMNO": "lymphocyte_count",
    "LBDMONO": "monocyte_count",
    "LBDNENO": "neutrophil_count",
    "LBDEONO": "eosinophil_count",
    "LBDBANO": "basophil_count",

    "LBXRBCSI": "red_blood_cell_count",
    "LBXHGB": "hemoglobin",
    "LBXHCT": "hematocrit",

    "LBXMCVSI": "mean_corpuscular_volume",
    "LBXMCHSI": "mean_corpuscular_hemoglobin",
    "LBXMC": "mean_corpuscular_hgb_concentration",

    "LBXRDW": "red_cell_distribution_width",

    "LBXPLTSI": "platelet_count",
    "LBXMPSI": "mean_platelet_volume",

    "LBXNRBC": "nucleated_red_blood_cells",

    # =========================
    # HEPATITIS
    # =========================

    "LBXHE1": "hepatitis_b_antibody_1",
    "LBXHE2": "hepatitis_b_antibody_2",

    # =========================
    # DETECTION FLAGS
    # =========================

    "LBDHRPLC": "hdl_below_detection_limit",
    "LBDSATLC": "alt_below_detection_limit",
    "LBDSGTLC": "ggt_below_detection_limit",
    "LBDSTBLC": "bilirubin_below_detection_limit",
}

# rename function


def rename_columns(df):
    """
    Rename raw NHANES columns into human-readable names.
    """
    return df.rename(columns=COLUMN_MAPPING)


# validation function
def validate_columns(df):
    """
    Ensure all expected raw columns exist.
    """
    missing_columns = [
        col for col in COLUMN_MAPPING
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )
