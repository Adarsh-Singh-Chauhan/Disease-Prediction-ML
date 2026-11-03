<!-- Animated heading -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=30&pause=900&color=16A085&center=true&vCenter=true&width=760&lines=HeartGuard+%7C+Heart+Disease+ML;Explore+data.+Compare+models.+Learn+from+metrics." alt="HeartGuard animated title" />

<p><strong>A machine-learning study for heart-disease risk classification using structured clinical attributes.</strong></p>

<p>
  <a href="https://github.com/Adarsh-Singh-Chauhan/Disease-Prediction-ML"><img src="https://img.shields.io/badge/Project-Machine%20Learning-0f766e?style=for-the-badge" alt="Machine Learning" /></a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/scikit--learn-modeling-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Status-Research%20%26%20Learning-64748b?style=for-the-badge" alt="Research and learning" />
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#workflow">Workflow</a> ·
  <a href="#models">Models</a> ·
  <a href="#results">Results</a> ·
  <a href="#run-locally">Run locally</a>
</p>

</div>

---

## Overview

**HeartGuard** is the presentation layer name for this repository's heart-disease prediction study. The project explores how supervised machine-learning classifiers can learn patterns from tabular clinical data and how their performance can be compared using a consistent train/test split.

The supplied dataset, `heart.csv`, contains **13 input columns** and a binary `target` column. The notebooks cover exploratory data analysis, data preparation, model training and evaluation.

> **Important:** This is an educational machine-learning project, not a medical device. Its output must not be used to diagnose, rule out, or treat heart disease. A qualified healthcare professional must assess clinical concerns.

## Project highlights

<table>
<tr>
<td width="50%">

### Data exploration
- Load and inspect the heart dataset
- Explore distributions and relationships
- Visualize patterns with Matplotlib and Seaborn

</td>
<td width="50%">

### Model evaluation
- Stratified train/test split
- Feature scaling where appropriate
- Compare classification metrics
- Review confusion-matrix output

</td>
</tr>
<tr>
<td>

### Reproducible experiments
- Notebook-based workflow
- Fixed random seed in the documented split
- Saved experiment artifacts in the repository

</td>
<td>

### Explainable reporting
- Accuracy
- Precision
- Recall
- Confusion matrix

</td>
</tr>
</table>

## Technology stack

<div align="center">

| Layer | Tools |
|---|---|
| Language | Python |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine learning | scikit-learn |
| Gradient boosting reference | XGBoost |
| Experiment environment | Jupyter Notebook / Google Colab |
| Dataset | CSV (`heart.csv`) |

</div>

## Workflow

<div align="center">

`HEART.CSV` → `EDA` → `TRAIN / TEST SPLIT` → `PREPROCESSING` → `MODEL TRAINING` → `EVALUATION`

</div>

1. **Load data** — read `heart.csv` into a Pandas DataFrame.
2. **Explore** — inspect columns, distributions and relationships.
3. **Prepare** — separate the 13 predictors from the `target` label.
4. **Split** — the evaluation notebook documents an 80/20 stratified split with `random_state=42`.
5. **Preprocess** — apply `StandardScaler` for scale-sensitive estimators.
6. **Train and compare** — fit classifiers and inspect their evaluation metrics.

## Dataset fields

The CSV uses these predictor names:

| Field | Description (high-level) |
|---|---|
| `age` | Age |
| `sex` | Encoded sex field |
| `cp` | Chest-pain category |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood-sugar flag |
| `restecg` | Resting ECG category |
| `thalach` | Maximum recorded heart rate |
| `exang` | Exercise-induced angina flag |
| `oldpeak` | ST depression field |
| `slope` | ST-segment slope category |
| `ca` | Number of major vessels (dataset encoding) |
| `thal` | Thalassemia-related dataset category |
| `target` | Binary target label used for classification |

The categorical/integer encodings are dataset codes; they should not be interpreted as free-text clinical values.

## Models

The repository's evaluation materials reference these classifiers:

- Logistic Regression
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- XGBoost
- Neural Network

The evaluation notebook contains executable examples and logged outputs for several of these models. The list above records the algorithms referenced by the project; it does not imply every model has been trained and benchmarked in the same run.

## Results

The evaluation notebook contains the following logged results for its documented train/test split. These are **not** a guarantee of performance on new patients or other datasets.

| Model | Accuracy | Precision | Recall |
|---|---:|---:|---:|
| Logistic Regression | 80.33% | 76.92% | 90.91% |
| Gaussian Naive Bayes | 81.97% | 78.95% | 90.91% |
| SVM (RBF) | 81.97% | 77.50% | 93.94% |
| KNN | 80.33% | 76.92% | 90.91% |
| Decision Tree | 78.69% | 75.00% | 90.91% |
| Random Forest | **83.61%** | 78.05% | **96.97%** |

In the recorded run, Random Forest has the highest accuracy among the models with visible logged metrics in the notebook. For a reliable model-selection decision, rerun the full pipeline and evaluate with cross-validation, ROC-AUC, calibration and an independent test set.

## Repository structure

```text
Disease-Prediction-ML/
├── heart.csv
├── heart_eda_train_split.ipynb
├── heart_modeling.ipynb
├── Model_Evoluation_py.ipynb
├── artifacts.zip
├── heartguard-health-main (2).zip
├── LICENSE
└── README.md
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/Adarsh-Singh-Chauhan/Disease-Prediction-ML.git
cd Disease-Prediction-ML
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the notebook dependencies

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

Install XGBoost only when running the cells that use it:

```bash
pip install xgboost
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Open the notebook you want to run. Keep `heart.csv` in the working directory, then execute the cells in order. In Google Colab, upload the notebook and dataset when prompted by its cells.

## Project notebooks

| Notebook | Purpose |
|---|---|
| [EDA and train/test split](heart_eda_train_split.ipynb) | Explore the dataset and prepare the split |
| [Modeling](heart_modeling.ipynb) | Train baseline pipelines and review evaluation outputs |
| [Model evaluation](Model_Evoluation_py.ipynb) | Compare additional classifiers and inspect metrics |

## Team

| Member | Contribution (as recorded in the original project README) |
|---|---|
| Ansh | ML Lead |
| Sanjeet | EDA Analysis |
| Anushka | Database and Connectivity |
| Prakash | Assistant |
| OM Tiwari | Backend |
| Adarsh | Model Evaluation |

## Responsible use

- Do not treat a model score or prediction as a diagnosis.
- Do not enter identifiable patient information into public demos.
- Dataset labels and encodings are not a substitute for clinical interpretation.
- Validate data quality, bias, calibration and generalization before any real-world research or deployment.
- Seek medical advice from a qualified clinician for symptoms or health concerns.

## License

See [LICENSE](LICENSE) for the repository's license terms.

---

<div align="center">

**Built as a collaborative machine-learning learning project.**

<a href="https://github.com/Adarsh-Singh-Chauhan">GitHub · Adarsh Singh Chauhan</a>

<sub>Explore responsibly. Validate rigorously. Never use this project as a medical diagnosis.</sub>

</div>
