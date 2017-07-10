# Code Sources

## Feature Extraction

* [ ] Use nltk to obtain number of sentences, tokens, and average sentence length
https://github.com/ankeshanand/review-helpfulness/blob/master/models/SVM/extract_features.py
* [ ] Use nltk to obtain structural features
https://github.com/ankeshanand/review-helpfulness/blob/master/src/features/structural_features.py
- [ ] Use SpaCy for structural features
https://github.com/synsypa/helpful_reviews/blob/master/parse_raw.py


## Learning the Model

- [ ] SVM with grid search for best performing kernel
https://github.com/synsypa/helpful_reviews/blob/master/svm_class.py
- [ ] https://github.com/ankeshanand/review-helpfulness/blob/master/models/SVM/acl2015.py#L210
```
StandardScaler().fit_transform(X)
model = SVR()
grid = GridSearchCV(model, params, cv=5, scoring='mean_squared_error', n_jobs=-1)
```
- [ ] Linear regression model
https://github.com/rishabhmisra/Helpfulness-Prediction/blob/master/helpfulness_prediction_final_model.py
- [ ] SVM classification
https://github.com/Azure-rong/Review-Helpfulness-Prediction/blob/master/main/Helpfulness%20prediction%20module/helpfulness%20prediction%20(classification).py
- [ ] Keras LSTM Network implementation
https://github.com/ankeshanand/review-helpfulness/blob/master/models/LSTM/regression_model_electronics.py
https://github.com/ankeshanand/review-helpfulness/blob/master/src/modified_lstm_model.py