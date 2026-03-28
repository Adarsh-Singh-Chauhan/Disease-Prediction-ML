# Heart Dataset EDA and Train-Test Split Report

- Input file: `heart.csv`
- Rows: **303**, Columns: **14**
- Target column: `target`
- Duplicate rows: **1**

## 1. Basic EDA

### Missing Values

          missing_count  missing_pct
age                   0          0.0
sex                   0          0.0
cp                    0          0.0
trestbps              0          0.0
chol                  0          0.0
fbs                   0          0.0
restecg               0          0.0
thalach               0          0.0
exang                 0          0.0
oldpeak               0          0.0
slope                 0          0.0
ca                    0          0.0
thal                  0          0.0
target                0          0.0

### Feature Types

- Numerical features (5): age, trestbps, chol, thalach, oldpeak
- Categorical features (8): sex, cp, fbs, restecg, exang, slope, ca, thal

### Target Balance (%)

          pct
target       
0       45.54
1       54.46

### Numeric Summary

          count      mean      std    min    25%    50%    75%    max   iqr
age       303.0   54.3663   9.0821   29.0   47.5   55.0   61.0   77.0  13.5
trestbps  303.0  131.6238  17.5381   94.0  120.0  130.0  140.0  200.0  20.0
chol      303.0  246.2640  51.8308  126.0  211.0  240.0  274.5  564.0  63.5
thalach   303.0  149.6469  22.9052   71.0  133.5  153.0  166.0  202.0  32.5
oldpeak   303.0    1.0396   1.1611    0.0    0.0    0.8    1.6    6.2   1.6
target    303.0    0.5446   0.4988    0.0    0.0    1.0    1.0    1.0   1.0

### Categorical Summary

 column  unique_values  top_value  top_count  top_pct
     ca              5          0        175    57.76
     cp              4          0        143    47.19
   thal              4          2        166    54.79
restecg              3          1        152    50.17
  slope              3          2        142    46.86
    sex              2          1        207    68.32
    fbs              2          0        258    85.15
  exang              2          0        204    67.33

## 2. Advanced EDA

### Outlier Summary (IQR Method)

 feature    q1    q3  iqr  lower_bound  upper_bound  outlier_count  outlier_pct
trestbps 120.0 140.0 20.0        90.00       170.00              9         2.97
 oldpeak   0.0   1.6  1.6        -2.40         4.00              5         1.65
    chol 211.0 274.5 63.5       115.75       369.75              5         1.65
 thalach 133.5 166.0 32.5        84.75       214.75              1         0.33
     age  47.5  61.0 13.5        27.25        81.25              0         0.00

### Feature-Target Associations

 feature                type  pearson_with_target  mutual_info
     age           numerical              -0.2254          NaN
trestbps           numerical              -0.1449          NaN
    chol           numerical              -0.0852          NaN
 thalach           numerical               0.4217          NaN
 oldpeak           numerical              -0.4307          NaN
    thal categorical_encoded                  NaN     0.141657
      ca categorical_encoded                  NaN     0.122503
      cp categorical_encoded                  NaN     0.121352
   exang categorical_encoded                  NaN     0.093674
   slope categorical_encoded                  NaN     0.083317
     sex categorical_encoded                  NaN     0.073447
 restecg categorical_encoded                  NaN     0.000000
     fbs categorical_encoded                  NaN     0.000000

## 3. Train-Test Split

- Test size: **0.2**
- Random state: **42**
- Train shape: **(242, 13)**
- Test shape: **(61, 13)**

### Target Distribution After Split

    train   test
0  0.4545  0.459
1  0.5455  0.541

## 4. Generated Artifacts

- `numeric_summary.csv`
- `categorical_summary.csv`
- `correlation_matrix.csv`
- `outlier_summary.csv`
- `feature_target_associations.csv`
- `categorical_mutual_info.csv` (if categorical features exist)
- `plots/` (all saved visualizations)
- `train_test_split/X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`
- `train_test_split/train.csv`, `test.csv`