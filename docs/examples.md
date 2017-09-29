# Examples

## Discourse-Relation Types

Temporal.Asynchronous
> The internal cables could be a tiny bit longer, so measure carefully inside your case **before** you purchase

Temporal.Synchrony
> the DVD sounded like it was going through a meat grinder **when** it was playing

Contingency.Cause
> i got this lens **because** i wanted a compact wide angle lens that i could easily throw in my bag to cover events.

Contingency.Pragmatic cause
> The reason there is so little research done on these ecosystems is, in Flannery's words, "**Because** the work is just too depressing ".
* Tagged correctly? – No. Should be used for justifications – "no causal influence" (PDTP Annotation Manual: 29)
* Very only instance!

Contingency.Condition
> So **if** you want a great 70-200 zoom and crave attention and can carry the weight this lens is for you.

Contingency.Pragmatic condition
"these are cases of Explicit if tokens with Arg1 and Arg2 not being causally related. In all cases, Arg1 holds true independently of Arg2." (PDTP Annotation Manual: 31)
> The DC supply is nice **when** you need to work on your sensor, but it is not essential.
* Annotation: doubtful

Comparison.Contrast
> Yeah, you'll pay a little more, **but** the quality you'll get will be worth it.

Comparison.Pragmatic contrast
* No correctly tagged example

Comparison.Concession
> **Although** the camera cannot zoom very far it still is a very good camera.

Comparison.Pragmatic concession
> "it's not a world apart from other hyped low noise cameras" **BUT** it may be actually the Best(low light)point and shoot by a small margin.
* Annotated correctly?
* Only two instances!

Expansion.Conjunction
> The kit lenses are a great starter. **And** they're worlds better than anything you'll get with a point-and-shoot.

Expansion.Instantiation
> The only problem i have with the camera is that it has a hard time focusing on small texts. **For example** i want to copy a receipt and send it to the manufacturer it would come out blurry.

Expansion.Restatement
> **Overall**, I am happy with the build and performance of these chargers.

Expansion.Alternative
> you need to press it slow and firm, **or** it won't start.
* Annotated correctly?

Expansion.Exception
> wifi works well, **except** that streaming does not work all the time.

Expansion.List
> The keyboard is great, screen is good **and** overall quality is very good.
* Uses of "and" that mostly should be annotated as `Expansion.Conjunction`.

## Parsing Mistakes

> Don't know if the problem is router related or n-version related but **since** range and not speed is the issue for me, I do not find the unit to be an improvement over what I have already installed.
* tagged as Temporal.Asynchronous
* should be Contingency.Cause

> The picture is absolutely gorgeous, **as** it has the new atsc digital signal receiver built in!
* tagged as Temporal.Synchrony
* should be Contingency.Cause (often)

> I've had time to thoroughly test it **and** I've sort of begun to have second thoughts about these.
> * tagged as Contingency.Cause
* should be Expansion.Conjunction

Contingency.Pragmatic cause
* Only annotated in one case (wrongly)
* Parser doesn't detect justifying relations as `Contingency.Pragmatic cause`, but rather as `Contingency.Cause`.

Contingency.Pragmatic condition
* Only annotated for "when" in a non-temporal meaning

Comparison.Pragmatic contrast
* "The tag “Pragmatic Contrast” applies when the connective indicates a contrast between one of the
arguments and an *inference* that can be drawn from the other" (PDTP Annotation Manual: 33)
* Only a few instances annotated, all should be Comparison.Contrast

## Product-Type Related Differences

* Contingency.Condition, Contingency.Cause: electronics +, books -
* Expansion.List: electronics (slightly) +, books -
* Temporal.Asynchronous, Expansion.Instantiation: electronics 0, books +

### Contingency.Condition

#### Electronics
> So **if** you want a great 70-200 zoom and crave attention and can carry the weight this lens is for you.

#### Books

often either related to the content or advise to the reader

> I didn't like any one in this novel and really didn't care **if** they survived or not.
> Do not buy this book **if** you have the option of buying Wolff's book- and definentely do not waste your money buying both of them.

### Contingency.Cause

#### Electronics
> i got this lens **because** i wanted a compact wide angle lens that i could easily throw in my bag to cover events.

#### Books

Motivation
> The only reason I finished the bk is **because** so many of my readers friends loved it and I kept waiting for its redeeming qualities.

Justification
> My guess is that this is the author's first book, because it reads like the work of an amateur, complete with awkward transitions, weak characterizations, and one-dimensional characters.