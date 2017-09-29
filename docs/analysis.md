# Relation-Results Analysis

## Typical Instances of `Expansion.Conjunction`

* The kit lenses are a great starter.  **And** they're worlds better than anything you'll get with a point-and-shoot.
* Plenty of reviews here on how great the camera is, **and** I agree with them.
* You're not just buying an e500 here, you're **also** buying into Olympus's lens system.
* The image quality is on par with similar offerings from Nikon and Canon, **and** it has the same, or very similar features.
* Spend a little more now, **and** it'll literally save you about $200 later.
* The 14-54 is built like a tank **and** the image quality will blow you away.

* Overall, the sets are very similar, my personal choice being the Haier, as I think the picture is sharper, the price is better and the battery lasts longer for my needs in bad weather. Haier **also** has way more picture settings and adjustments in the tv's menu

Typical reviews without the use of conjunction relations:

> It works fine.  It was easy to install.  I think that may have something to do with my experience with other routers though.  I am new to this.

> While the sound quality is okay (not excellent & NOT stereo), there are serious downers in my view:1) The included rechargeable batteries can ONLY be charged by attaching a headset to the transmitter.  There is no way the contact points on the batteries can work with any other battery charger.  The batteries are fitted with square thingys on each end, resulting in contact points being recessed within the squares.2)While transmitter is charging, it is NOT transmitting, rendering additional headsets useless.3) The headset that holds the batteries is built to accomodate ONLY rechargeable batteries from Sony.  Those square thingys stuck on each end!4) After 8 or 9 hours use, the batteries require about 20 hours charging.5) While the user can use AAA alkaline batteries, they must be acquired from Sony. the battery seating precludes the use of any other battery.  The square ends!  This has to be intentional on the part of Sony. forcing you to use only their product. Don't waste your money if you plan to use these headphones for any length of time.  The only thing good about this set is the foam earpads are cooler than the leather earpads offered by other manufacturers. I'll be returning mine and going back to Amphony. a much better choice.

## Accounts

### Multi-Confirmation

Readers seek for confirmation in their purchase-decision process. Once they're reading the reviews, they're already interested enough in the product that they actually *want* to buy it. The more confirming statements a review contains, the more helpful it will be perceived by these users. Often, multiple affirming statements are joined by a conjunction relation.

* The kit lenses are a great starter.  **And** they're worlds better than anything you'll get with a point-and-shoot.
* Spend a little more now, **and** it'll literally save you about $200 later.
* The 14-54 is built like a tank **and** the image quality will blow you away.

### Writing Quality

When taking a look at samples of reviews without any instances of `Expansion.Conjunction` relations, they often exhibit properties that indicate reduced writing quality.

* short sentences
* barely any use of cohesive devices
* short overall length

> It works fine.  It was easy to install.  I think that may have something to do with my experience with other routers though.  I am new to this.

| Electronics | Reviews including `Expansion.Conjunction` | Reviews without `Expansion.Conjunction` |
|--------|--------|--------|
| Avg. number of tokens       |      364.33  |      101.84  |
| Avg. sentence length       |       17.64 |       14.95 |
| Avg. number of discourse relations p.h.t.       |      3.83  |      2.34  |
| Avg. helpfulness score       |      0.83  |      0.71  |

| Books | Reviews including `Expansion.Conjunction` | Reviews without `Expansion.Conjunction` |
|--------|--------|--------|
| Avg. number of tokens       |      321.61  |      108.77  |
| Avg. sentence length       |       19.9 |       16.53 |
| Avg. number of discourse relations p.h.t.       |      3.15  |      1.93  |
| Avg. helpfulness score       |      0.77  |      0.65  |

### Persuasiveness

* Only explicitly signalled relations
* Causal relations: implicit
* even more persuasive

## Low Ranking of `Contingency.Cause`

### Usage

* Used not only to justify claims, but...
	* to motivate decisions
> i got this lens **because** i wanted a compact wide angle lens that i could easily throw in my bag to cover events.
	* to explain observations
> If the front and rear speakers are in phase (both pushing out at the same time) a ton of power is required **because** a vacuum is created inside the cabinet.

### Parsing Mistakes

* Many `Contingency.Cause` relations have been wrongly annotated with another relation type.
* see [examples.md](examples.md)