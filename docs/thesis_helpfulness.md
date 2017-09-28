# Investigating the Impact of Discourse Relations on Review Helpfulness

[TOC]

## Introduction


## Previous Studies

* Almagrabi
* Kim
* Mudambi and Schuff (2010)
	* definition
	* search vs. experience goods
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

* Number of relations per type between electronics and book reviews
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


