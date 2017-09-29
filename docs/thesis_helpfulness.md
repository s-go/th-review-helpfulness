# Investigating the Impact of Discourse Relations on Review Helpfulness

[TOC]

## Introduction


## Previous Studies

* Almagrabi
* Kim
* Mudambi and Schuff (2010)
	* definition
	* product type, specifically whether the product is a search or experience good, is important in understanding what makes a review helpful to consumers
	* moderate reviews are more helpful than extreme reviews (whether they are strongly positive or negative) for experience goods, but not for search goods
	* lengthier reviews generally increase the helpfulness of the review, but this effect is greater for search goods than experience goods
* PDTB
	* incl. pragmatic types
* Lin
* He & McAuley
* Golly (2017)

## Goal of this Study

* See proposal.

## Method

### Data

### Learning Task

### Features

* Automatically extracted explicit PDTB sense tags
* Spot tests showed that the discourse parser was unable to correctly distinguish pragmatic PDTB types (`Contingency.Pragmatic cause`, `Contingency.Pragmatic condition`, `Comparison.Pragmatic contrast`, and `Comparison.Pragmatic concession`) from their non-pragmatic counterparts. As this distinction is not crucial to the intended analyses, I decided to merge the pragmatic types with their non-pragmatic variants. That is, `Contingency.Cause` also includes all instances of `Contingency.Pragmatic cause`, covering both purely causal and justifying relations.

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

Other than expected: mid-field to low ranking of `Contingency.Cause` relations

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
	* Three most predictive relation types: same
	* Significant differences:
		* Contingency.Condition, Contingency.Cause: electronics +, books -
		* Expansion.List: electronics (slightly) +, books -
		* Temporal.Asynchronous, Expansion.Instantiation: electronics 0, books +
	* Typical examples?

## Discussion

### H1

* Accounts/Explanations for predictiveness of `Expansion.Conjunction` relation
	* Multi-Confirmation
	* Writing Quality
	* Persuasiveness

### H2

### Implications

### Limitations

### Future Work


## Conclusion


## Literature

Kamalski, J., Lentz, L., Sanders, T., & Zwaan, R. A. (2008). The forewarning effect of coherence markers in persuasive discourse: Evidence from persuasion and processing. Discourse Processes, 45, 545–579.
