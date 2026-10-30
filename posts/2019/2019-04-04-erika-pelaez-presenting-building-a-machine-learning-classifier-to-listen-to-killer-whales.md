---
title: Erika Pelaez Presenting “Building a Machine Learning Classifier to Listen to Killer Whales”
date: 2019-04-04 11:53:55 -0700
last_modified_at: 2019-05-05 11:58:13 -0700
permalink: /2019/04/04/erika-pelaez-presenting-building-a-machine-learning-classifier-to-listen-to-killer-whales/
slug: erika-pelaez-presenting-building-a-machine-learning-classifier-to-listen-to-killer-whales
wp_id: 15623
original_url: https://compositecode.blog/2019/04/04/erika-pelaez-presenting-building-a-machine-learning-classifier-to-listen-to-killer-whales/
categories:
- Ml4all
- Unknown Code Ramblings
tags:
- conferences
- Ml4all
excerpt: 'UPDATED: Video Added from the Conference! Introducing Erika Pelaez > @midoridancer < presenting “Building a Machine Learning Classifier to Listen to Killer Whales“. Data Scientist with experience and love for Machine Learning. I like making smart things and have worked with a diverse types of data from biological to transportation. Did you know that Machine …'
image: /wp-content/uploads/2019/04/ml4all-erika-pelaez.jpg
---

## UPDATED: Video Added from the Conference!

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/K0vmU_Jf3f4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

Introducing Erika Pelaez > [@midoridancer](https://twitter.com/midoridancer) < presenting “*Building a Machine Learning Classifier to Listen to Killer Whales*“.

![erika-pelaez](/wp-content/uploads/2019/04/erika-pelaez.jpg)Data Scientist with experience and love for Machine Learning. I like making smart things and have worked with a diverse types of data from biological to transportation.

Did you know that Machine Learning can help protect killer whales? Orcasound (<https://github.com/orcasound>) is a magnificent open source project for people to connect to their neighbor killer whales of the pacific northwest. They provide a platform that continuously broadcasts the underwater sounds from the Puget Sound area to anyone willing to listen. Come to my talk and I’ll show you how we’re applying Machine Learning with the Scikit-learn Python library against web scraped audio to build models that can be used for signal collection and classification.

Avid users spend time listening to mostly noise or ships but frankly the majority is there just to hear the orca sounds. The present talk will narrate the process we are following to automatically detect and classify orca vs non orca (false killer whale and humpback whale) sounds.

The first challenge faced with this project was getting labeled data as the raw transmissions are unlabeled so my first approach was to build a dataset from scratch by web scraping audio from the internet using Beautiful soup then I used a bash script for making sure all the files had a maximum duration of 5s as this is the duration of the files that orcasound saves. The feature extraction of the audio files was handled with the librosa library from Python. I finally built a Random Forest Classifier with the scikit-learn Python library that was able to reach an accuracy of 99 +/-2% with a 10 fold cross validation. The next steps will be to have the model accessible through an API and send the collected signals to it for classification, after a signal is detected a notification could be send to the users so they don’t have to listen to all the noise.

Come check out Erika Pelaez’s talk at [ML4ALL](http://ml4all.org) happening April 28th-30th in amazing Portland, Oregon! Get your tickets to attend [here](http://ml4all.org/attend.html). For the [schedule](http://ml4all.org/schedule.html), our [excellent sponsors](http://ml4all.org/sponsors.html) [docs for the conference](http://ml4all.org/docs.html), check out the [ML4ALL Conference Site](http://ml4all.org)!
