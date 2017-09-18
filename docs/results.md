# Experimental Results

* **Features:**
	* STR: overall rating
	* LEN: review length in tokens
	* UGR: *tf-idf* statistic of each word occurring in a review
	* REL-CNT: counts of explicit discourse-relations types
	* REL-PRS: presence of explicit discourse-relations types

## Pre-Study

### STR, LEN, UGR, REL-CNT

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

### STR, LEN, UGR, REL-PRS

```
--- Starting experiment ---

Data path: "data/electronics/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.545 (± 0.099)

--- Took 9.12 seconds ---
```

### Linear Kernel (SVR)

```
--- Starting experiment ---

Data path: "data/electronics/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=0.01, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',
  kernel='linear', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.546 (± 0.104)

--- Took 16.05 seconds ---
```

### Linear Kernel (LinearSVR)

```
--- Starting experiment ---

Data path: "data/electronics/reviews_dev.csv" (2000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: LinearSVR(C=0.01, dual=True, epsilon=0.1, fit_intercept=True,
     intercept_scaling=1.0, loss='epsilon_insensitive', max_iter=1000,
     random_state=None, tol=0.0001, verbose=0)

CV Pearson r: 0.553 (± 0.099)

--- Took 1.60 seconds ---
```

## Experiment

### STR, LEN, UGR, REL-PRS

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

### STR, LEN, UGR, REL-PRS (with log transformation)

```
--- Starting experiment ---

Data path: "data/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.577 (± 0.042)

--- Took 444.56 seconds ---
```

### STR, LEN, UGR, REL-CNT (normalized frequencies)

```python
            rels_df = rels_df.div(
                self.reviews_dataframe['numTokens'], axis='rows') * 100
```

```
--- Starting experiment ---

Data path: "data/electronics/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: SVR(C=1, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.001,
  kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)

CV Pearson r: 0.560 (± 0.042)

--- Took 439.07 seconds ---
```

### Linear Kernel (LinearSVR)

```
--- Starting experiment ---

Data path: "data/electronics/reviews_traintest.csv" (18000 reviews)
Extracting features from raw data...

Starting 10-fold cross-validation...
Model: LinearSVR(C=0.01, dual=True, epsilon=0.1, fit_intercept=True,
     intercept_scaling=1.0, loss='epsilon_insensitive', max_iter=1000,
     random_state=None, tol=0.0001, verbose=0)

CV Pearson r: 0.575 (± 0.032)

--- Took 15.94 seconds ---
```