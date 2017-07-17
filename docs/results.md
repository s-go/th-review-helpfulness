# Experimental Results

## Pre-Study

* **Corpus:** Development dataset (2,000 reviews)

### STR

```
Data path: "data/reviews_dev.csv"

# Starting 10-fold cross-validation...
Evaluating model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.48 (± 0.10)
```

### STR, LEN (no scaling, no standard transformation)

```
Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.50 (± 0.12)
```

### STR, LEN, UGR (no scaling, no standard transformation)

```
Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.50 (± 0.12)
```

### STR, LEN, UGR (with feature scaling, no standard transformation)

```
Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.54 (± 0.10)
```


### STR, LEN, UGR (with feature scaling, with standard transformation)

```
Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.54 (± 0.11)
```