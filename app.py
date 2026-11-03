from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, ConfigDict, Field
from sklearn.ensemble import RandomForestClassifier

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "heart.csv"
PUBLIC_DIR = ROOT / "public"

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]

app = FastAPI(
    title="HeartGuard ML API",
    description="Educational heart-disease classification demo built from the repository dataset.",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)


class PredictionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    age: int = Field(ge=18, le=100)
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: int = Field(ge=70, le=250)
    chol: int = Field(ge=100, le=700)
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: int = Field(ge=50, le=250)
    exang: Literal[0, 1]
    oldpeak: float = Field(ge=0, le=10)
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3, 4]
    thal: Literal[0, 1, 2, 3]


@lru_cache(maxsize=1)
def get_model() -> tuple[RandomForestClassifier, int]:
    """Load the checked-in dataset and fit the repository's Random Forest setup once per worker."""
    if not DATA_PATH.exists():
        raise RuntimeError("heart.csv is missing from the deployment bundle.")

    frame = pd.read_csv(DATA_PATH)
    frame.columns = [str(column).strip() for column in frame.columns]
    missing = [column for column in FEATURES + ["target"] if column not in frame.columns]
    if missing:
        raise RuntimeError(f"Dataset is missing required columns: {', '.join(missing)}")

    clean = frame[FEATURES + ["target"]].dropna()
    if clean.empty or clean["target"].nunique() != 2:
        raise RuntimeError("Dataset must contain rows for both target classes.")

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42,
        n_jobs=1,
    )
    model.fit(clean[FEATURES], clean["target"].astype(int))
    return model, len(clean)


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(PUBLIC_DIR / "index.html")


@app.get("/styles.css", include_in_schema=False)
def styles() -> FileResponse:
    return FileResponse(PUBLIC_DIR / "styles.css", media_type="text/css")


@app.get("/app.js", include_in_schema=False)
def javascript() -> FileResponse:
    return FileResponse(PUBLIC_DIR / "app.js", media_type="application/javascript")


@app.get("/api/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "HeartGuard ML API",
        "dataset_available": DATA_PATH.exists(),
        "features": len(FEATURES),
        "model": "RandomForestClassifier",
    }


@app.get("/api/model")
def model_info() -> dict:
    try:
        _, sample_count = get_model()
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Model could not be initialized. Check the deployment dataset.") from exc

    return {
        "name": "Random Forest",
        "estimator": "RandomForestClassifier",
        "configuration": {"n_estimators": 200, "max_depth": 6, "random_state": 42},
        "training_rows": sample_count,
        "features": FEATURES,
        "target": "target (binary dataset label)",
    }


@app.post("/api/predict")
def predict(payload: PredictionInput) -> dict:
    try:
        model, sample_count = get_model()
        row = pd.DataFrame([payload.model_dump()], columns=FEATURES)
        probabilities = model.predict_proba(row)[0]
        class_index = int(probabilities.argmax())
        predicted_class = int(model.classes_[class_index])
        positive_index = list(model.classes_).index(1)
        positive_score = float(probabilities[positive_index])
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Prediction is temporarily unavailable. Please try again.") from exc

    return {
        "prediction": predicted_class,
        "label": "Positive class (target = 1)" if predicted_class == 1 else "Negative class (target = 0)",
        "model_score": round(float(probabilities[class_index]) * 100, 1),
        "positive_class_score": round(positive_score * 100, 1),
        "training_rows": sample_count,
        "model": "Random Forest · 200 estimators · max depth 6",
        "notice": "Experimental dataset classification only. Not a medical diagnosis or calibrated clinical risk estimate.",
    }
