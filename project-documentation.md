# Predicting the Helpfulness of Product Reviews Based on Discourse Relations

## Project Documentation

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
* ==Dataset description after filtering== (similar to Table 2 in Kim et al. 2006: 5)
	* Total products
	* Total reviews
	* Average reviews/product
	* Min/max reviews/product

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
    * LEN=Length
    * UGR=Unigram
    * STR=Stars
* **Discourse-relations model** with baseline features incremented by the use of explicit discourse relations

##### Feature Extraction

* Discourse relations
	* Parse sample reviews using the PDTB-styled end-to-end discourse parser (Lin et al. 2014)
```
java -Xmx12g -jar parser.jar data/reviews_sample
```
	* Use level 2 type of relations (as in Lin et al. 2014)
	* Only use `*.exp.res` files (containing explicit relations)
	* Don't use `*.nonexp.res` files (containing implicit relations) because of the unsatisfactory performance of the non-explicit classifier (cf. Lin et al. 2014: 175)

#### Learning the Probabilistic Model

* Support Vector Machine (SVM) regression model
* SVM with radial basis function (RBF) kernel (performs best according to Kim et al. 2006: 5)
	* But: "we tested the ability of SVM regression to recover the target helpfulness score, given the score itself as the only feature. The Spearman correlation for this test was a perfect 1.0. Interestingly, the Pearson correlation was only 0.798, suggesting that the RBF kernel does learn the helpfulness ranking without learning the function exactly." (Kim et al. 2006: 6)
	* → ==Test other kernels!==
		* [ ] linear
		* [ ] polynomial (degrees 2, 3, and 4)
* Tune RBF kernel parameters C (the penalty parameter) and $$$\gamma$$$ (the kernel width hyperparameter) performing full grid search
* Apply standard transformation to each feature measurement *f*:
$$
\text{ln}(f+1)
$$
* Scale each feature between [0, 1]

### Experiments

#### Evaluation Metrics

* **Gold standard:** estimate the helpfulness function h "using user ratings extracted from Amazon.com, where $$$rating_+(r)$$$ is the number of unique users that rated the review r as helpful and $$$rating_-(r)$$$ is the number of unique users that rated r as unhelpful")
* **Adaption to Kim et al. (2006): no ranking**
    * Kim et al. (2006)'s model tries to predict the absolute helpfulness score in order to learn the ranks of each review on a product
    * Here: predict helpfulness score without ranking
* Evaluate model performance by a 10-fold cross-validation: Train SVM model using 9 folds, evaluate performance on remaining test fold
* Correlation of the predicted helpfulness score against the gold standard by computing the computed the standard Pearson correlation coefficient
	* Kim et al. (2006): Pearson correlation coefficient for best-performing system (with 95% confidence bounds):
0.476 ± 0.038

#### Regression Performance

## Limitations

* Automatic discourse parsing
	* "The parser gives an overall system F 1 score of 46.80 percent for partial matching utilizing gold standard parses, and 38.18 percent with full automation." (Lin et al. 2014: 152)
	* "A large portion of the misses comes from the Non-Explicit relations, as these are more difficult to classify in comparison with the Explicit relations." (Lin et al. 2014: 177)

## References

* He, R., & McAuley, J. (2016). Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering. In Proceedings of the 25th International Conference on World Wide Web (pp. 507-517). International World Wide Web Conferences Steering Committee.
* Kim, S. M., Pantel, P., Chklovski, T., & Pennacchiotti, M. (2006). Automatically assessing review helpfulness. In Proceedings of the 2006 Conference on empirical methods in natural language processing (pp. 423-430). Association for Computational Linguistics.
* Lin, Z., Ng, H. T., & Kan, M. Y. (2014). A PDTB-styled end-to-end discourse parser. Natural Language Engineering, 20(2), 151-184.