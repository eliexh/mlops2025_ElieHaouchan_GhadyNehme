## MLOps Project 2025: NYC Taxi Trip Duration Prediction

## Overview

This project implements a complete end-to-end machine learning pipeline to predict taxi trip duration in New York City. The objective is to simulate a professional MLOps workflow—from local containerized development to cloud-based orchestration on **AWS SageMaker**.

---

## 👥 Group Information

Course: MLOps Course - USJ
Instructor: Naji El Hachem
Team: Elie Haouchan & Ghady Nehme
Repository: mlops2025_ElieHaouchan_GhadyNehme

---

## 🚕 Dataset & Task

* **Dataset:** NYC Yellow Cab trip record data (New York City Taxi Trip Duration | Kaggle).
* **Task:** Regression to predict the `trip_duration` (in seconds) of each taxi ride.
* **Constraints:** The data contains missing values, categorical/time-based features, and significant outliers (e.g., trips lasting >24 hours or <10 seconds).

---

## 🛠 Tech Stack

* **Dependency Management:** `uv` for reproducible environments.
* **Packaging:** `src/` layout Python packaging.
* **Containerization:** `Docker` and `docker-compose` for local consistency.
* **Cloud Orchestration:** `AWS SageMaker Pipelines` for training and batch inference.

---

## 🏗 Project Structure

.
├── src/mlproject/        # Core package (preprocessing, features, training)
├── scripts/              # SageMaker & local entry scripts
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── batch_inference.py
├── data/                 # Raw/Processed data (Git ignored)
├── models/               # Model artifacts (Git ignored)
├── Dockerfile            # System & library configuration
├── docker-compose.yml    # Local service orchestration
└── pyproject.toml        # Package metadata and dependencies


## 🚀 Usage

### 1. Local Development (Docker)

Build and run the entire pipeline inside a container:

```bash
docker-compose build
docker-compose run app python scripts/train.py
docker-compose run app python scripts/batch_inference.py
```


### 2. AWS SageMaker Deployment

Run the orchestration scripts to trigger cloud pipelines:

```bash
python scripts/run_training_pipeline.py
python scripts/run_batch_inference_pipeline.py

```

---

## 📈 Methodology & Justification

### Preprocessing & Feature Engineering

* **Outlier Removal:** We filter trips with extreme durations (e.g., <1 min or >12 hours) to prevent model skew.
* **Temporal Features:** Extraction of `pickup_hour`, `day_of_week`, and `month` from timestamps.
* **Spatial Features:** Implementation of Haversine distance between pickup and dropoff coordinates.

### Modeling Approach

* **Choice:** Random Forest / Gradient Boosting (XGBoost).
* **Justification:** These ensemble methods effectively handle non-linear interactions between spatial and temporal features typical in urban traffic data.

### Evaluation Metrics

* **Primary Metric:** **RMSLE** (Root Mean Squared Logarithmic Error).
* **Justification:** RMSLE is preferred for regression tasks where the target variable spans several orders of magnitude, as it penalizes under-predictions and over-predictions equally in log-space.

---

## 🌳 Git Branching Model

The project follows a strict branching strategy:

* `master`: Production-ready code.
* `feat/preprocess`, `feat/features`, `feat/train`, `feat/inference`: Modular feature development.
* `ops/docker`: Containerization setup.
* `ops/sagemaker`: Cloud orchestration.