# Experimental Results

## Pre-Study

* **Corpus:** Development dataset (2,000 reviews)
* **Features:**
	* STR: overall rating
	* LEN: review length in tokens
	* UGR: *tf-idf* statistic of each word occurring in a review
	* REL1: counts of explicit discourse-relations types
	* REL2: existence of explicit discourse-relations types

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

### STR, LEN, UGR

```
--- Starting experiment ---

Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.540 (± 0.102)

--- Took 7.20 seconds ---
```

### STR, LEN, UGR, REL1

```
--- Starting experiment ---

Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.541 (± 0.101)

--- Took 8.29 seconds ---
```

### STR, LEN, UGR, REL2

```
--- Starting experiment ---

Data path: "data/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.547 (± 0.101)

--- Took 7.17 seconds ---
```

## Experiment

### STR, LEN, UGR

```
--- Starting experiment ---

Data path: "data/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.560 (± 0.042)

--- Took 418.74 seconds ---
```

### STR, LEN, UGR, REL1

```
--- Starting experiment ---

Data path: "data/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.560 (± 0.041)

--- Took 441.45 seconds ---
```

:-(

### STR, LEN, UGR, REL2

```
--- Starting experiment ---

Data path: "data/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.574 (± 0.040)

--- Took 436.78 seconds ---
```