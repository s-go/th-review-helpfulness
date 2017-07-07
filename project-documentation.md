# Predicting the helpfulness of product reviews based on discourse relations

## Project Documentation

1. Got 5-core corpus of Amazon.com Electronics reviews from http://jmcauley.ucsd.edu/data/amazon/ (He & McAuley 2016) (1,689,188 reviews)
2. Preprocess corpus
	1. Assign a unique ID to every review
	2. Remove reviews with less than 10 helpfulness votes or less than 20 characters (107,035 remaining)
	3. Export to CSV file
	4. Sample 20,000 reviews (randomly)
3. Parse sample reviews using the PDTB-Styled End-to-End Discourse Parser (Lin et al. 2014)
	* Only use `*.exp.res` files (containing explicit relations)
	* Don't use `*.nonexp.res` files (containing implicit relations) because of the unsatisfactory performance of the non-explicit classifier (cf. Lin et al. 2014: 175)

## Potential Issues

* Automatic discourse parsing
	* "The parser gives an overall system F 1 score of 46.80 percent for partial matching utilizing gold standard parses, and 38.18 percent with full automation." (Lin et al. 2014: 152)
	* "A large portion of the misses comes from the Non-Explicit relations, as these are more difficult to classify in comparison with the Explicit relations." (Lin et al. 2014: 177)

## References

* He, R., & McAuley, J. (2016). Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering. In Proceedings of the 25th International Conference on World Wide Web (pp. 507-517). International World Wide Web Conferences Steering Committee.
* Lin, Z., Ng, H. T., & Kan, M. Y. (2014). A PDTB-styled end-to-end discourse parser. Natural Language Engineering, 20(2), 151-184.