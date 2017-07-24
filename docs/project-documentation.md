# Predicting the Helpfulness of Product Reviews Using Discourse Relations

**Research Question:** Can the performance of a probabiblistic model predicting the helpfulness of product reviews be improved by adding features capturing the distribution of discourse relations?

## Hypotheses

Previous work on predicting the helpfulness of product reviews has been using different kinds of features (cf. Kim et al. 2006: 2f.; Almagrabi et al. 2015):

* structural (such as the number of tokens in the review)
* lexical (such as unigram statistics)
* syntactic (such as part-of-speech analyses)
* semantic (such as sentiment analyses)
* meta-data (such as the overall rating)

Discourse structure has hardly been taken into account. It seems plausible that the way statements in a review are presented (e.g. justified, elaborated, contrasted) has an impact on its helpfulness to other users, as it affects as how comprehensible and credible it is perceived.

The discourse structure of a review is reflected in the distribution of discourse relations that are used in it.

> **Hypothesis 1:** The distribution of discourse relations in a product review is an indicator of its helpfulness to other users.

In previous work, there have been contrary findings on whether a balanced review (that uses both positive and negative statements about a product) will be more helpful than an unbalanced one (see Mudambi & Schuff (2010); Connors et al. (2011); Schlosser (2011)).

Schlosser (2011) concludes that "reviews including two-sided arguments are not necessarily more helpful, credible and persuasive than one-sided reviews" (p. 236), especially for reviews with an extreme product rating (1 or 5 stars). Reviews with a moderate product rating, however, "were deemed helpful by more voters" if they were two-sided (Schlosser 2011: 230).

In these cases with a moderate rating, presenting both pros and cons of a product increases the helpfulness of the review. This balanced presentation ==should reflect (justify?)== in the usage of comparison relations in the PDTB 2.0 hierarchy of sense tags (`COMPARISON.Contrast`, `COMPARISON.Pragmatic_Contrast`, `COMPARISON.Concession`, `COMPARISON.Pragmatic_Concession`; cf. Prasad et al. 2008: 5).

> **Hypothesis 2:** The usage of comparison relations within a product review is an indicator of its helpfulness, at least for reviews with a moderate product rating.

## Method

### Datasets

* 5-core corpus of Amazon.com reviews on products from the category "Electronics" (He & McAuley 2016)
* http://jmcauley.ucsd.edu/data/amazon/
* 1,689,188 reviews

#### Preprocessing

1. Assign a unique ID to every review
2. Filter out uninformative reviews
    * Remove reviews with less than 10 helpfulness votes
    * Remove reviews with less than 20 characters
    * 107,035 reviews remaining
3. Sample 20,000 reviews (randomly)
4. Export to CSV file
5. Withhold 10% of reviews as a development corpus and randomly sort the remaining 90% into ten sets for 10-fold cross validation.
	* development section: 2,000 reviews
	* training/test section: 18,000 reviews

### Probabilistic Model

* Following approach by Kim et al. (2006)

#### Task Definition

* Review helpfulness function h:
$$
h(r \in R) = \frac{rating_+(r)}{rating_+(r) + rating_-(r)}
$$
	* → helpfulness score

#### Features

* **Baseline model** with best-performing features (according to Kim et al. 2006: 6)
    * Length (LEN): The total number of tokens in a syntactic analysis of the review.
    * Unigram (UGR): The *tf-idf* statistic of each word occurring in a review.
	  http://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
    * Stars (STR): Most websites require reviewers to include an overall rating for the products that they review (e.g., star ratings in Amazon.com). This feature set includes the rating score (STR1) as well as the absolute value of the difference between the rating score and the average rating score given by all reviewers (STR2).
* **Discourse-relations model** with baseline features incremented by the use of explicit discourse relations
	* REL-CNT: counts of explicit discourse-relations types
	* REL-PRS: presence of explicit discourse-relations types

##### Feature Extraction

* Discourse relations
	* Parse sample reviews using the PDTB-styled end-to-end discourse parser (Lin et al. 2014)
```
java -Xmx12g -jar parser.jar data/reviews_sample
```
	* Use level 2 type of relations (as in Lin et al. 2014)
	* Only use `*.exp.res` files (containing explicit relations)
	* Don't use `*.nonexp.res` files (containing implicit relations) because of the unsatisfactory performance of the non-explicit classifier (cf. Lin et al. 2014: 175)
* List of annotated relations/senses:
```
Comparison.Concession
Comparison.Contrast
Comparison.Pragmatic concession
Comparison.Pragmatic contrast
Contingency.Cause
Contingency.Condition
Contingency.Pragmatic condition
Expansion.Alternative
Expansion.Conjunction
Expansion.Exception
Expansion.Instantiation
Expansion.List
Expansion.Restatement
Temporal.Asynchronous
Temporal.Synchrony
```

#### Learning the Probabilistic Model

* Support Vector Machine (SVM) regression model
* SVM with radial basis function (RBF) kernel (performs best according to Kim et al. 2006: 5)
* Tune RBF kernel parameters C (the penalty parameter) and $$$\gamma$$$ (the kernel width hyperparameter) performing full grid search
* Scale each feature between [-1, 1]

### Experiments

#### Evaluation Metrics

* **Gold standard:** estimate the helpfulness function h "using user ratings extracted from Amazon.com, where $$$rating_+(r)$$$ is the number of unique users that rated the review r as helpful and $$$rating_-(r)$$$ is the number of unique users that rated r as unhelpful")
* **Adaption to Kim et al. (2006): no ranking**
    * Kim et al. (2006)'s model tries to predict the absolute helpfulness score in order to learn the ranks of each review on a product
    * Here: predict helpfulness score without ranking
* Evaluate model performance by a 10-fold cross-validation: Train SVM model using 9 folds, evaluate performance on remaining test fold
* Correlation of the predicted helpfulness score against the gold standard by computing the Pearson correlation coefficient
	* Kim et al. (2006): Pearson correlation coefficient for best-performing system (with 95% confidence bounds):
0.476 ± 0.038

## Results

| Feature Combinations   | Pearson r      | $$$p_{one-tailed} $$$ |
|------------------------|----------------|-----------------------|
| STR, LEN, UGR          | 0.560 (± 0.042)| –
| STR, LEN, UGR, REL-CNT | 0.560 (± 0.041)| 0.5
| STR, LEN, UGR, REL-PRS | **0.574 (± 0.040)**| **0.0197**
| STR, LEN, UGR, REL-CMP | 0.563 (± 0.042)| 0.33

* Significance test:
	* http://vassarstats.net/rdiff.html
	* https://stats.stackexchange.com/a/99747
	* Compare with significance level: $$$p < .05$$$?
* **Key result:** Adding the presence of discourse-relation types as features significantly improves the performance of our model in predicting review helpfulness.

## Discussion

### Implications

* Results show that the distribution of discourse relations in a product review is, in fact, an indicator of its helpfulness.
	* "Distribution": presence of relation types ("senses"), not counts
	* No effect of relation-type counts: probably more because of technical reasons (feature scaling) than deep theoretical ones
* This suggests that discourse structure influences the perceived value of a review to other users.
* What we don't know yet:
	* Do certain relation types have a bigger impact than others?
	* How exactly does the presence of discourse relations influence the perceived value? (Comprehensibility, credibility, ...?)
	* Does the impact of discourse relations on review helpfulness vary across product categories (e.g., books vs. electronics)?

### Limitations

* Automatic discourse parsing
	* "The parser gives an overall system $$$F_1$$$ score of 46.80 percent for partial matching utilizing gold standard parses, and 38.18 percent with full automation." (Lin et al. 2014: 152)
	* Ignored implicit relations because of the unsatisfactory performance of the non-explicit classifier (cf. Lin et al. 2014: 175)

## References

* Almagrabi, H., Malibari, A., & McNaught, J. (2015). A Survey of Quality Prediction of Product Reviews. In International Journal of Advanced Computer Science & Applications, 1(6), 49-58.
* Connors, L., Mudambi, S. M., & Schuff, D. (2011). Is It the Review or the Reviewer? a Multi-Method Approach to Determine the Antecedents of Online Review Helpfulness. In Proceedings of the 2011 44th Hawaii International Conference on System Sciences (pp. 1-10). IEEE Computer Society.
* He, R., & McAuley, J. (2016). Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering. In Proceedings of the 25th International Conference on World Wide Web (pp. 507-517). International World Wide Web Conferences Steering Committee.
* Kim, S. M., Pantel, P., Chklovski, T., & Pennacchiotti, M. (2006). Automatically assessing review helpfulness. In Proceedings of the 2006 Conference on empirical methods in natural language processing (pp. 423-430). Association for Computational Linguistics.
* Lin, Z., Ng, H. T., & Kan, M. Y. (2014). A PDTB-styled end-to-end discourse parser. Natural Language Engineering, 20(2), 151-184.
* Mertz, M., Korfiatis, N., & Zicari, R. V. (2014). Using Dependency Bigrams and Discourse Connectives for Predicting the Helpfulness of Online Reviews. In International Conference on Electronic Commerce and Web Technologies (pp. 146-152). Springer International Publishing.
* Mudambi, S. M., & Schuff, D. (2010). What Makes a Helpful Online Review? A Study of Customer Reviews on Amazon.com. MIS Quarterly 34(1), 185-200.
* Prasad, R., Dinesh, N., Lee, A., Miltsakaki, E., Robaldo, L., Joshi, A., & Webber, B. (2008). The Penn Discourse Treebank 2.0. Paper presented at the 6th International Conference on Language Resources and Evaluation (LREC 2008), Marrakesh, Morocco.
* Schlosser, A. E. (2011). Can including pros and cons increase the helpfulness and persuasiveness of online reviews? The interactive effects of ratings and arguments. Journal of Consumer Psychology, 21(3), 226-239.