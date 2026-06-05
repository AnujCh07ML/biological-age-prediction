# 🧬 Biological Age Prediction Using NHANES Biomarkers

A research-oriented machine learning project for estimating chronological age from clinical and laboratory biomarkers using multi-cycle NHANES (National Health and Nutrition Examination Survey) data.

The project emphasizes reproducible machine learning pipelines, biological validity, model comparison, and explainability.

---

# 🚀 Project Overview

Aging is associated with measurable physiological changes across multiple biological systems.

This project investigates whether routinely collected blood biomarkers can be used to estimate age and serve as a foundation for future biological age modeling.

The system:

- Integrates multiple NHANES cycles (2011–2020)
- Cleans and harmonizes heterogeneous biomedical datasets
- Builds a reproducible machine learning pipeline
- Benchmarks multiple tree-based models
- Supports future explainability using SHAP

---

# 🎯 Objectives

- Build a production-style ML pipeline
- Create a unified NHANES biomarker dataset
- Compare multiple machine learning algorithms
- Identify biomarkers most associated with aging
- Develop a foundation for biological age estimation research

---

# 📊 Dataset

### Source

National Health and Nutrition Examination Survey (NHANES)

### Study Period

2011–2020

### Final Dataset

| Metric       | Value       |
| ------------ | ----------- |
| Participants | 36,992      |
| Features     | 27          |
| Target       | Age (years) |

### Current Biomarkers

- Albumin
- Blood Urea Nitrogen
- Creatinine
- Uric Acid
- HbA1c
- Total Cholesterol
- HDL Cholesterol
- Triglycerides
- White Blood Cell Count
- Lymphocyte Percentage
- Monocyte Percentage
- Neutrophil Percentage
- Red Blood Cell Count
- Hemoglobin
- Hematocrit
- Mean Corpuscular Volume
- Red Cell Distribution Width
- Platelet Count
- Calcium
- Sodium
- Potassium
- Phosphorus
- Total Bilirubin
- Total Protein
- Globulin
- GGT
- Sex

---

# 🏗️ Project Architecture

```text
load_data
    ↓
merge_data
    ↓
combine_years
    ↓
create_dataset
    ↓
train_test_split
    ↓
preprocessing
    ↓
model_training
    ↓
evaluation
    ↓
artifact_persistence
    ↓
interpretability
```

---

# 📁 Project Structure

```text
biological-age-prediction/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│
├── outputs/
│   ├── metrics/
│   ├── plots/
│   └── reports/
│
├── notebooks/
│
├── src/
│   └── biological_age/
│       ├── data/
│       ├── preprocessing/
│       ├── features/
│       ├── models/
│       ├── evaluation/
│       ├── interpret/
│       ├── split/
│       └── utils/
│
├── tests/
├── main.py
├── config.yaml
└── README.md
```

---

# ⚙️ Machine Learning Pipeline

### Preprocessing

Numeric features:

- Median imputation
- Standard scaling

Categorical features:

- Most frequent imputation

### Train/Test Split

- Random state: 42
- Reproducible splits

### Models Evaluated

- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

---

# 🏆 Current Benchmark Results

| Model         | MAE  | RMSE  | R²    |
| ------------- | ---- | ----- | ----- |
| Random Forest | 8.05 | 11.30 | 0.777 |
| XGBoost       | 7.71 | 10.75 | 0.798 |
| LightGBM      | 7.71 | 10.73 | 0.799 |

### Current Best Model

LightGBM currently provides the strongest overall benchmark performance.

```text
MAE  : 7.71 years
RMSE : 10.73
R²   : 0.799
```

---

# 💾 Saved Artifacts

### Models

```text
models/
├── rf_model.pkl
├── xgb_model.pkl
└── lgbm_model.pkl
```

### Metrics

```text
outputs/metrics/
├── rf_metrics.json
├── xgb_metrics.json
├── lgbm_metrics.json
└── model_comparison.json
```

---

# 📈 Current Findings

- Tree-based gradient boosting methods outperform Random Forest.
- XGBoost and LightGBM perform similarly.
- Biomarker-based age prediction is feasible using standard laboratory measurements.
- Current performance suggests meaningful age-related biological signal exists within the selected feature set.

---

# 📌 Current Status

## Data Engineering

- [x] NHANES ingestion pipeline
- [x] Multi-year merging
- [x] Dataset validation
- [x] Processed dataset generation

## Machine Learning

- [x] Feature preprocessing pipeline
- [x] Random Forest benchmark
- [x] XGBoost benchmark
- [x] LightGBM benchmark
- [x] Model comparison framework
- [x] Model artifact persistence

## In Progress

- [ ] Hyperparameter optimization
- [ ] Feature importance analysis
- [ ] SHAP explainability
- [ ] Final model selection

## Planned

- [ ] Extended biomarker experiments
- [ ] Biological age proxy validation
- [ ] API deployment

---

# 🧰 Tech Stack

### Data

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- XGBoost
- LightGBM

### Explainability

- SHAP (planned)

### Engineering

- Pytest
- Docker
- Git

---

# 🔁 Reproducibility

```bash
git clone https://github.com/AnujCh07ML/biological-age-prediction.git

cd biological-age-prediction

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pip install -e .
```

Run pipeline:

```bash
python main.py
```

---

# 🔭 Future Work

- Hyperparameter tuning
- Feature importance analysis
- SHAP interpretation
- Additional biomarker experiments
- Biological age validation
- FastAPI deployment
- Dockerized inference service

---

# 🧠 Author Note

This project is intentionally structured as a maintainable machine learning system rather than a collection of notebooks.

The focus is on:

- Reproducibility
- Biological validity
- Modular architecture
- Explainable machine learning
- Research-oriented experimentation

---

# 📄 License

MIT License
