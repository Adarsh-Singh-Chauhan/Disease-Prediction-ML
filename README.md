<!-- Animated project title -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=32&pause=900&color=16A085&center=true&vCenter=true&width=820&lines=HeartGuard+%7C+Heart+Disease+ML;Explore+data.+Compare+models.+Understand+outputs." alt="HeartGuard animated title" />

<p><strong>An interactive machine-learning lab for exploring a heart-disease classification model.</strong></p>

<p>
  <a href="https://heartguard-health.vercel.app"><img src="https://img.shields.io/badge/Live%20Demo-Open%20HeartGuard-0f766e?style=for-the-badge&logo=vercel&logoColor=white" alt="Live demo" /></a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#live-application">Live application</a> ·
  <a href="#machine-learning-workflow">ML workflow</a> ·
  <a href="#evaluation-snapshot">Evaluation</a> ·
  <a href="#run-locally">Run locally</a>
</p>

</div>

---

## Overview

**HeartGuard** is an educational machine-learning project built around the heart-disease dataset in `heart.csv`. It combines the original notebook-based exploration and model evaluation work with a responsive web interface and a Python prediction API.

The application lets a visitor enter the 13 dataset attributes, submit them to the FastAPI endpoint, and inspect the Random Forest model's predicted dataset class and probability scores.

> **Medical safety:** HeartGuard is a learning and research demonstration only. It is not a medical device, diagnostic system, or substitute for a clinician. Its score is not a calibrated clinical risk estimate. Do not use it to make health decisions or delay medical care.

## Live application

<div align="center">

### [Open HeartGuard ↗](https://heartguard-health.vercel.app)

</div>

The current deployment includes:
- Responsive dark dashboard with animated visual elements.
- 13-field input form aligned with the source CSV columns.
- FastAPI endpoints for service health, model metadata and prediction.
- Random Forest classification trained from the repository dataset.
- Explicit model-output context and medical-use disclaimer.

## Technology stack

| Layer | Technology | Role |
|---|---|---|
| ML language | Python 3.12 | Model and API implementation |
| Data processing | Pandas, NumPy | Dataset loading and feature preparation |
| Machine learning | scikit-learn | Random Forest classifier |
| API | FastAPI, Pydantic | Request validation and prediction endpoints |
| Frontend | HTML5, CSS3, JavaScript | Responsive interactive application |
| Visualization / EDA | Matplotlib, Seaborn | Notebook analysis and plots |
| Experiment environment | Jupyter Notebook / Google Colab | EDA and model experiments |
| Hosting | Vercel | Production deployment |

## Live application architecture

```text
Browser
  │
  ├── HTML / CSS / JavaScript interface
  │
  └── POST /api/predict
          │
          ▼
       FastAPI
          │
          ├── Validate 13 input fields (Pydantic)
          ├── Load heart.csv
          ├── Fit cached Random Forest model
          └── Return predicted class + model scores
```

The model is initialized once per running serverless worker and cached for subsequent requests handled by that worker. The service trains from the committed CSV at runtime; it does not require a separate hosted database.

## Dataset

The checked-in `heart.csv` contains **303 rows**, **13 input features** and one binary `target` column.

| Feature | Dataset field |
|---|---|
| Age | `age` |
| Sex code | `sex` |
| Chest-pain category code | `cp` |
| Resting blood pressure | `trestbps` |
| Serum cholesterol | `chol` |
| Fasting blood-sugar code | `fbs` |
| Resting ECG category code | `restecg` |
| Maximum heart rate | `thalach` |
| Exercise-induced angina code | `exang` |
| ST depression field | `oldpeak` |
| ST slope category code | `slope` |
| Major-vessel count code | `ca` |
| Thal category code | `thal` |
| Binary label | `target` |

The categorical fields use the numeric encodings in the source data. The web form displays those codes instead of translating them into clinical interpretations.

## Machine-learning workflow

1. **Load** — read `heart.csv` into a Pandas DataFrame.
2. **Explore** — inspect the dataset and visualize distributions and relationships.
3. **Prepare** — separate the 13 input columns from the `target` label.
4. **Split** — the evaluation notebook documents an 80/20 stratified train/test split with `random_state=42`.
5. **Preprocess** — scale features for scale-sensitive estimators in the notebook experiments.
6. **Compare** — evaluate classifiers with accuracy, precision, recall and confusion-matrix output.
7. **Serve** — the web API fits the repository's Random Forest configuration against the checked-in dataset and serves predictions.

### Model used by the live API

```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42,
    n_jobs=1,
)
```

The live API retrains this estimator from all usable rows in `heart.csv` on the first prediction handled by a worker. The model is cached in that worker after initialization.

## Models referenced in the notebooks

- Logistic Regression
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- XGBoost
- Neural Network

The list records the algorithms referenced by the original project materials. It does not imply every model has been benchmarked in the same run or is used by the live API.

## Evaluation snapshot

The original model-evaluation notebook contains the following logged metrics for its documented split:

| Model | Accuracy | Precision | Recall |
|---|---:|---:|---:|
| Logistic Regression | 80.33% | 76.92% | 90.91% |
| Gaussian Naive Bayes | 81.97% | 78.95% | 90.91% |
| SVM (RBF) | 81.97% | 77.50% | 93.94% |
| KNN | 80.33% | 76.92% | 90.91% |
| Decision Tree | 78.69% | 75.00% | 90.91% |
| Random Forest | **83.61%** | 78.05% | **96.97%** |

These values are historical notebook outputs, not a guarantee of live prediction quality or clinical performance. The production API is a separate fit on the full checked-in dataset; it does not calculate or claim that the notebook's test metrics for each individual response. For serious research, rerun the complete pipeline and assess independent validation data, cross-validation, calibration, subgroup performance and data leakage.

## API reference

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/health` | Service and dataset availability |
| `GET` | `/api/model` | Model configuration and feature list |
| `POST` | `/api/predict` | Validate an input profile and return a prediction |

Example prediction request:

```json
{
  "age": 52,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 204,
  "fbs": 0,
  "restecg": 1,
  "thalach": 160,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

The response contains the predicted binary class, the model score for that predicted class, the positive-class score, the number of training records and a notice explaining the model's limitations.

## Repository structure

```text
Disease-Prediction-ML/
├── app.py                         # FastAPI application + model inference
├── public/
│   ├── index.html                 # HeartGuard interface
│   ├── styles.css                 # Responsive design + animations
│   └── app.js                     # Form handling + API integration
├── heart.csv                      # 303-row source dataset
├── heart_eda_train_split.ipynb    # EDA and train/test split
├── heart_modeling.ipynb           # Model training and evaluation
├── Model_Evoluation_py.ipynb      # Model comparison notebook
├── requirements.txt               # Python dependencies
├── vercel.json                    # Vercel function configuration
├── .python-version                # Python runtime version
├── artifacts.zip                  # Existing experiment artifacts
├── LICENSE
└── README.md
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/Adarsh-Singh-Chauhan/Disease-Prediction-ML.git
cd Disease-Prediction-ML
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn app:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

API health check: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

## Run the notebooks

Install the analysis libraries if needed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter xgboost
jupyter notebook
```

Open a notebook and execute its cells in order. Keep `heart.csv` in the working directory, or upload it when a Colab cell requests a file.

## Deployment

The GitHub repository is connected to the Vercel project **heartguard-health**. Pushes to `main` are configured to trigger production deployments.

Vercel configuration and Python dependencies live in:
- `vercel.json`
- `requirements.txt`
- `.python-version`

## Team

| Member | Contribution (as recorded in the original README) |
|---|---|
| Ansh | ML Lead |
| Sanjeet | EDA Analysis |
| Anushka | Database and Connectivity |
| Prakash | Assistant |
| OM Tiwari | Backend |
| Adarsh | Model Evaluation |

## Responsible use

- Never interpret the prediction as a diagnosis or a clinical risk calculation.
- Do not enter identifiable patient information into a public demo.
- The dataset uses encoded fields; its labels should not be treated as medical guidance.
- Model probability outputs may be poorly calibrated and can be wrong.
- Seek advice from a qualified healthcare professional for symptoms or health concerns.

## License

See [LICENSE](LICENSE) for the repository's license terms.

---

<div align="center">

**Built as a collaborative machine-learning learning project.**

<a href="https://github.com/Adarsh-Singh-Chauhan">GitHub · Adarsh Singh Chauhan</a>

<sub>Explore responsibly. Validate rigorously. Never use this project as a medical diagnosis.</sub>

</div>
