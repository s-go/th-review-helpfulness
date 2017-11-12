# Investigating the Impact of Discourse Relations on Review Helpfulness

[TOC]

## Abstract

* Investigate what influence individual discourse-relation types have on predicting the helpfulness of product reviews, and whether these effects vary across product categories.
* Two probabilistic models are trained on electronics and book reviews, using the distribution of discourse-relation types as their only features.
* Based on feature-weight analyses and comparisons across product categories, two key results are drawn:
	1. Other than expected, conjunction relations contribute most to predicting review helpfulness.
	2. When comparing the results between both product categories, around half of the relation types exhibit similar impact on review helpfulness, while the other half shows differing effects.

## Introduction

* The task of automatically evaluating the helpfulness of product reviews has rev

* Golly (2017) provides some evidence for the general claim that discourse structure influences the helpfulness of product reviews.
* Goal: investigate how certain discourse-relation types affect review helpfulness.
* Does this influence vary across product categories?

## Related Work

* PDTB
	* incl. pragmatic types
	* incl. Debopam's feedback
* Almagrabi
* Kim
* Mertz
	* they argue that the main influence on review helpfulness is the text of the review itself (rather than its product rating or other features derived from meta data.)
	* aim: propose and evaluate two novel text-based features for predicting review helpfulness
		* bigrams according to grammatical dependencies (dependency bigrams)
		* discourse connectives
			* "A potential indicator of review helpfulness could be the amount of internal discourse in a review text." (→ coherence)
			* regular expression matching instead of discourse parsing
* Mudambi and Schuff (2010)
	* definition
	* product type, specifically whether the product is a search or experience good, is important in understanding what makes a review helpful to consumers
	* moderate reviews are more helpful than extreme reviews (whether they are strongly positive or negative) for experience goods, but not for search goods
	* lengthier reviews generally increase the helpfulness of the review, but this effect is greater for search goods than experience goods
	* "Reviews of search goods are more likely to address specific, tangible aspects of the product, and how the product performed in different situations. Consumers are in search of specific information regarding the functional attributes of the product. Since objective claims about tangible attributes are more easily substantiated, extreme claims for search goods can be perceived as credible, as shown in the advertising literature (Ford et al. 1990)." (189)
	* "On consumer ratings sites, experience goods often have many extreme ratings and few moderate ratings, which can be explained by the subjective nature of the dominant attributes of experience goods. Taste plays a large role in many experience goods"

* Lin
* He & McAuley
* Golly (2017)
	* takes up the idea of Mertz that discourse structure is likely to have an effect on the perceived helpfulness of product reviews, while trying to overcome the shortcomings in their study.
	* a baseline regression model using the best-performing feature combination by Kim is enriched by features capturing the presence and occurrence frequencies of different discourse-relation types
	* To this end, it uses the discourse parser by \citet{Lin2014} to extract explicit discourse connectives and aggregate them into PDTB senses
	* supports the hypothesis that the distribution of discourse relations in a product review is an indicator of its helpfulness to other users – at least if the term “distribution” is defined as the \textit{presence} of certain relation types, rather than their occurrence frequencies.

## Goal of this Study

* **Q1:** What is the effect of individual discourse-relation types on predicting review helpfulness?
	* Claims supported by one or more premises
	* **H1:** Causal relations (\lstinline|Contingency.Cause| and \lstinline|Contingency.Pragmatic Cause|, in terms of PDTB sense tags) have a particularly high impact on review helpfulness.

* **Q2:** Does the impact of discourse-relation types on review helpfulness vary across product categories?
	* Mudambi/Schuff: rating and review length
	* **H2:** The effect of individual discourse-relation types on predicting review helpfulness differs among different product categories.

## Method

For investigating the research questions presented in the previous section, two probabilistic models have been trained on reviews from different product categories. This section descibes the data sets used in the experiments, the learning task and features of the probabilistic model, as well as the overall experimental setup.

### Data

### Learning Task

### Features

* Automatically extracted explicit PDTB sense tags
* Spot tests showed that the discourse parser was unable to correctly distinguish pragmatic PDTB types (`Contingency.Pragmatic cause`, `Contingency.Pragmatic condition`, `Comparison.Pragmatic contrast`, and `Comparison.Pragmatic concession`) from their non-pragmatic counterparts. As this distinction is not crucial to the intended analyses, I decided to merge the pragmatic types with their non-pragmatic variants. That is, the `Contingency.Cause` feature also includes all instances of `Contingency.Pragmatic cause`, covering both purely causal and justifying relations.

* See [examples.md](examples.md).

### Experimental Setup

Similar to Golly (2017):

* SVM regression model

Adaptions:

* linear kernel instead of RBF kernel → allows for feature-weight analysis
	* With thorough tuning of hyperparameters: equal prediction performance can be reached
* Only discourse-relation features to eliminate confounding factors
	* Comparison of discourse-feature variants
	* → REL-PRS

## Results

### Q1: What is the effect of individual discourse-relation types on predicting review helpfulness?

* The discourse-relation type that turns out to be by far most predictive of review helpfulness in both product categories is `Expansion.Conjunction`, typically witnessed by connectives such as *and* or *also*.

* To better understand this unexpected result, I examined samples of this relation type. ... show some typical instances.
	* see [analysis.md](analysis.md)
* Writing Quality
* Parsing Mistakes

Other relations that turn out to be predictive: `Temporal.Synchrony` and `Comparison.Contrast` (ranks 2 and 3 in both product categories).

Other than expected: mid-field to low ranking of `Contingency.Cause` relations (rank 5 in electronics, rank 9 in books)

* Usage of `Contingency.Cause` relations
* Parsing Mistakes

### Q2: Does the impact of discourse-relation types on review helpfulness vary across product categories?

* Number of relations per type between electronics and book reviews (per thousand tokens)
| PDTB Sense Tag | Electronics | Books |
|--------|--------|--------|
| Expansion.Conjunction  |    10.18 | 8.91 |
| Comparison.Contrast  |       7.41 | 6.46 |
| Contingency.Cause  |         4.65 | 2.98 |
| Contingency.Condition  |     4.15 | 2.43 |
| Temporal.Synchrony  |        4.11 | 3.25 |
| Temporal.Asynchronous  |     3.44 | 2.50 |
| Expansion.Alternative  |     0.76 | 0.64 |
| Comparison.Concession  |     0.49 | 0.61 |
| Expansion.Restatement  |     0.30 | 0.26 |
| Expansion.Instantiation  |   0.13 | 0.23 |
| Expansion.List  |            0.03 | 0.02 |
| Expansion.Exception  |       0.03 | 0.03 |

* Comparison of ranks
	* Three relation types with strongest positive coefficients: same
	* Significant differences:
		* Contingency.Condition, Contingency.Cause: electronics +, books -
		* Expansion.List, Expansion.Exception, Expansion.Alternative:
          electronics: close to 0; books: strong negative correlation
		* Expansion.List: electronics (slightly) +, books -
		* Temporal.Asynchronous, Expansion.Instantiation: electronics 0, books +
	* Typical examples?

## Discussion

### H1

* Unexpected result: `Expansion.Conjunction`
* Accounts/Explanations for predictiveness of `Expansion.Conjunction` relation
	* Multi-Confirmation (→ typical examples)
	* Writing Quality (→ linguistic properties)
		* writing style has an influence on predictive power (Liu et al. 2008)
	* Eckle-Kohler et al. (2015: 2239): discourse marker *und* (and) as being indicative of premises
		* claim-premise model of argumentation: premise → support for claim
* Accounts for medium/low predictiveness of causal relations
	* "approaches relying on discourse markers are not applicable for identifying argumentative discourse structures in documents which do not follow a standardized form" (Stab and Gurevych 2014: 54)
		* → rather Argumentation mining than discourse analysis?
	* explicit relations → Persuasiveness
	* "the component-level argument feature provides less useful information in review helpfulness identification." (Liu et al. 2017)
	* parsing mistakes

### H2

* Half of discourse-relation types: similar effect; other half: differing impact
	* → suggests some mechanisms that might be common within the text type, others being sensitive to product categories
	* To test this claim: investigate further product categories

### Limitations

* No clear separation of search and experience goods
	* books: non-fiction vs. novels
	* electronics: laser printers vs. MP3 players
* automatic parsing
	* only explicit
	* partly incorrect annotations


## Conclusion

This study investigated the effect of individual discourse-relation types on predicting review helpfulness. Contrary to expectations, the highest predictive power could not be found in causal relations, but rather in conjunction relations. Whether this is because the latter are often used to signal additional confirming statements, because their existence in a review is correlated with its writing quality, or because they are indicative of premises supporting a claim will have to be examined by further studies.


## Literature

Kamalski, J., Lentz, L., Sanders, T., & Zwaan, R. A. (2008). The forewarning effect of coherence markers in persuasive discourse: Evidence from persuasion and processing. Discourse Processes, 45, 545–579.

Liu, Y., Huang, X., An, A., & Yu, X. (2008, December). Modeling and Predicting the Helpfulness of Online Reviews. In Data mining, 2008. ICDM'08. Eighth IEEE international conference on Data mining (pp. 443-452). IEEE.