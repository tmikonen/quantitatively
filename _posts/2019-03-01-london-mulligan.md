---
layout: post
title: The London Mulligan
subtitle: How would the proposed London mulligan rule affect Old School?
post_description: The Wizards of the Coast are testing a new mulligan rule in the upcoming London Mythic Championships. Here's my limited but quantitative look on some of the potential effects of the new mulligan rule, if it was adopted in Old School 93/94.
bigimg: /img/london_mulligan/snap_keep.jpg
tags: [93/94, Power Monolith, Mulligan, London]
---

## The London Mulligan

On February 21st, the Wizards of the Coast [announced](https://magic.wizards.com/en/articles/archive/competitive-gaming/mythic-championship-ii-format-and-london-test-2019-02-21) that at the upcoming Mythic Championships at London, they would test out a new [mulligan](https://mtg.gamepedia.com/Mulligan) rule. The potential change understandably sparked a lot of discussion over the various forums.

The mulligan rule has already changed a number of times during the history of the game. Initially, the players had no possibility to exchange the cards in their starting hand, but already in 1994 the first mulligan rule was instated. This was the "all land" and "no land" mulligan rule, which allowed the player to redraw their starting hand if it consisted of only land cards or none at all. This helped somewhat in avoiding non-games, situations where the player would get stuck with an unplayable combination of cards for long enough to effectively lose the game. A few years later, the Paris mulligan rule was adopted, allowing the player to freely decide whether they would keep the starting hand or not. If they decided against keeping, they would shuffle the cards back into the deck and draw one less for their next hand. They could do this until they decided to keep the hand, each time going down one card. A few years ago, in 2015, the mulligan rule was again changed to the Vancouver mulligan rule. There, the player could, after deciding to keep their hand, look at the top card of their deck and then either put it back on top or move it to the bottom of their deck ("Scry 1").

The newly proposed London mulligan would again change the convention. Under the proposed rule, the player would always draw the same number of cards (seven) in their new hand. However, when they choose to keep the hand, they will need to put back into their deck a number of cards equal to the times they re-drew their hand. Effectively, the size of the starting hand is the same as in the Paris or Vancouver mulligan rule, but the amount of cards that the player sees increases. Again, the purpose is to reduce the game variance and the number of non-games in contemporary formats.

However, it is quite interesting that since the player can decide how to apply their mulligan strategy, they can actually take advantage of the natural variance of the game by purposefully filtering through the cards. Essentially, they can use the mulligan mechanic to pick out statistical outliers, the [black swans](https://en.wikipedia.org/wiki/Black_swan_theory), if you will. This kind of strategy lends itself especially to combo decks, which rely on assembling a statistically rare combination of cards that provide enormous, typically game-winning, synergies. An example from the Old School Magic is the combination of [Basalt Monolith](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=2) and [Power Artifact](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=1043), which together provide an engine to produce an infinite amount of colorless mana.

## Probabilities of certain combinations

The MinMax blog [already wrote about the London mulligan](https://www.minmaxblog.com/magic/2019/2/22/the-london-mulligan-an-eternal-perspective). They showed a nice numerical analyses for certain combos that are played in the Legacy format. For example, they calculate that the probability of casting a [Chalice of the Void](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=48326) on turn one, assuming 4 Chalices and 10 mana sources that allow it to be cast for 2 mana. With the mulligan rule change, the probability of getting that goes from 53 % to 62.5 %, assuming that the mulligan strategy is completely based on doing this one thing and hands of 5 cards are always kept. Similarly they find that assembling a two-card combo, of which there are 8 copies of both halves of the combo in the deck, gets more frequent by 9 [percentage points](https://en.wikipedia.org/wiki/Percentage_point), from about 70 % to 79 %.

In Old School, the most affected strategies would probably be combo decks such as the Power Monolith. Typically the sideboarded cards in Old School are relatively benign, with perhaps the exception of certain cards such as [City in a Bottle](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=904) and [Blood Moon](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=1784). An interesting character of old school is that many decks are playing copies of [Wheel of Fortune](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=231), [Timetwister](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=132) and [Ancestral Recall](http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=95). These three cards allow one to mulligan aggressively and then recover the lost card disadvantage by replenishing the hand with new cards from the deck, if the risk did not pay off otherwise.

To expand upon the results presented earlier in the MinMax blog, I calculated the probabilities if finding certain combinations of cards by Monte Carlo simulation. I took the same approach as MinMax, but expanded on it by also looking at the probabilities when starting on the draw (which is where the card Scry 1 rule of the Vancouver mulligan kicks in). I also added other combinations that I think are relevant for 93/94 Old School. The results are in the two tables below.

*Table 1. The probability of succesfully mulliganing into a certain set of cards with a 60 card deck, when willing to go down to 5 cards in hand. Statistical error is significantly less than 1 %.*

| Target card combination | Application | Chance to succeed, Vancouver, on the play | Chance to succeed, London, on the play |
| -- | -- | -- |
| 1 of 4 & <br> 1 of 10 | Legacy Chalice | 53 % | 63 % |
| 1 of 8 & <br> 1 of 8  | Legacy Sneak & Show | 70 % | 79 % |
| 1 of 4  | Sideboard card | 73 % | 78 % |
| 1 of 2  | Sideboard card | 47 % | 53 % |
| 1 of 3 & <br> 1 of 7  | Draw spell + 1 fast mana| 35 % | 44 % |
| 1 of 3 & <br> 2 of 7  | Draw spell + 2 fast mana| 9 % | 13 % |
| 1 of 4 & <br> 1 of 4 <br> 2 of 26  | Power Monolith combo w/ 2 mana sources| 21 % | 31 % |
| 2 of 16 & <br> 2 of 25 | Creature-based aggro | 75 % | 88 % |
| 3 of 16 & <br> 2 of 25 | Creature-based aggro | 30 % | 48 % |

*Table 2. Same as Table 1, except assuming being on the draw.*

| Target card combination | Application | Chance to succeed, Vancouver, on the draw | Chance to succeed, London, on the draw |
| -- | -- | -- |
| 1 of 4 & <br> 1 of 10 | Legacy Chalice | 59 % | 66 % |
| 1 of 8 & <br> 1 of 8  | Legacy Sneak & Show | 76 % | 82 % |
| 1 of 4  | Sideboard card | 77 % | 80 % |
| 1 of 2  | Sideboard card | 51 % | 55 % |
| 1 of 3 & <br> 1 of 7  | Draw spell + 1 fast mana| 41 % | 47 % |
| 1 of 3 & <br> 2 of 7  | Draw spell + 2 fast mana| 11 % | 15 % |
| 1 of 4 & <br> 1 of 4 <br> 2 of 26  | Power Monolith combo w/ 2 mana sources| 26 % | 34 % |
| 2 of 16 & <br> 2 of 25 | Creature-based aggro | 83 % | 91 % |
| 3 of 16 & <br> 2 of 25 | Creature-based aggro | 39 % | 55 % |

The first three entries (rows) in Table 1 merely repeat the results already discussed above and in the MinMax blog. Out of those, the relevant information for Old School is, perhaps, that the probability of finding certain sideboard cards is increased by roughly 3 to 5 percentage points. Not an alarming increase. Table 2 then shows the corresponding numbers for being on the draw.

Mulliganing into a draw spell (Wheel of Fortune, Timetwister, Ancestral Recall) and one or more fast mana cards (typically the Black Lotus, Sol Ring and the 5 Moxen) increases by about 9 percentage points (or 26 percent) on the play. This is probably a noticeable increase even with a small sample size, for instance games played over a tournament or two. On the draw the increase is smaller.

Considering the combo decks, I calculated the probability of finding at least 1 of two combo pieces (think Basalt Monolith and Power Artifact) and at least 2 mana sources out of the assumed 26. This is of course a gross simplification in many ways; I am attempting a more detailed analysis that I will hopefully discuss in the future. In any case, the probability of finding that particular combination increases from 21 % to 31 % (10 percentage points, or 48 percent!). That is quite a substantial boost for the combo. However, how that translates to actual game wins is unknown, and certainly beyond the scope of the present analysis.

Finally, I also calculated some probabilities for an assumed creature-based aggro deck, such as the Arabian Aggro. I'm assuming 25 mana sources and 16 threats that should be deployed in the first turns of the game (small creatures, Black Vises, etc.). Here the probability to have a decent hand start of at least 2 threats and 2 mana sources goes from 75 % to 88 %. So from fairly consistent to very consistent. The more aggressive start with at least 3 threats goes from
30 % to 48 % (18 percentage points, or 60 %). This is also a very significant increase! Again, how this is converted to game wins, is a very interesting question that unfortunately cannot be fully answered by just looking at the starting hands. Typically, aggro decks tend to face the problem of running out of playable cards, so very aggressive mulliganing may not be a good strategy.


## Conclusions

The London mulligan proposal would be a very interesting rules change. Only time will tell if it is adopted by Wizards of the Coast and if the Old School communities embrace it as well. Certain decks would receive a significant boost to their performance, but anything disastrous happening seems quite unlikely.

The relevance of the London mulligan rule to Old School was also discussed in the [Flippin' Orbs](http://www.wak-wak.se/9394/flippinorbs) and [All Tings Considered](http://alltingsconsidered.com/) podcasts. The general feeling seems to be that the change is probably not huge (definitely not format breaking) but that certain decks could benefit from the change. My analysis seems to agree with that sentiment for the most part.

Overall, I feel cautiously optimistic toward the London mulligan rule. If it ends up being part of the modern formats, it might be a refreshing change for the 93/94 also. Many of the largest playgroups currently play by the convention "old cards with new rules". Unless that symmetry is  broken, it would encourage absorbing the new mulligan rule as part of the 93/94 format as well. But certainly, actual playtesting reports would be in high demand before confirming such a rules change.

As the final caveat, I did not consider the effect of the rules change on the players' behavior. It is probable that the London mulligan would entice players to change into a more aggressive mulligan strategy. Purely from a mathematical point of view, the optimal strategy under different mulligan rules would also be different. Finding the optimal strategy would a very interesting challenge, but currently I clearly lack both the tools and also the game experience and insight to tackle such a problem with any seriousness.
