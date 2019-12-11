---
layout: post
title: Magic Card Detector
subtitle: How to detect and recognize MTG cards with Python
post_description: Last summer I put most of my other projects related to this blog on hold. I used that time to build a Magic card detector with Python. Here's how it turned out.
bigimg: /img/magic_card_detector/banner2.jpg
tags: [Python, OpenCV, Computer Vision, Segmentation, Recognition, Alpha]
usemathjax: true
---


# How to detect and recognize MTG cards with Python?

\\[C_\\textrm{all} = {60 \\choose 7} = 386206920, \\]




![](../img/magic_card_detector/hypno_original.jpg)

*Original image.*


![](../img/magic_card_detector/hypno_adjusted.jpg)

*Histogram adjusted image.*


![](../img/magic_card_detector/hypno_cnt.jpg)

*Contoured image.*


![](../img/magic_card_detector/hypno_bounding.jpg)

*Bounding quadrilateral inserted.*


![](../img/magic_card_detector/hypno_transformed.jpg)

*Segmented card candidate.*


![](../img/magic_card_detector/hypno_phash_diff.jpg)

*Perceptive hash differences to all Alpha cards.*



![](../img/magic_card_detector/hypno_recognized.jpg)

*Finally, the recognized Hypnotic Spectres.*








## Other examples

![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_dragon_whelp.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_counterspell_bgs.jpg)

![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_alpha_deck.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_black.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_geyser_twister_fireball.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_instill energy.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_lands_and_fatties.jpg)


![](https://github.com/tmikonen/magic_card_detector/raw/master/results/MTG_card_recognition_results_ruby.jpg)
