---
title: Eliminating Machine Bias w/ Mary Ann Brennan & Getting from Machine Learning Outputs to Decisions…  timely things!
date: 2018-05-09 14:18:26 -0700
last_modified_at: 2018-05-16 14:12:13 -0700
permalink: /2018/05/09/eliminating-machine-bias-w-mary-ann-brennan-getting-from-machine-learning-outputs-to-decisions-timely-things/
slug: eliminating-machine-bias-w-mary-ann-brennan-getting-from-machine-learning-outputs-to-decisions-timely-things
wp_id: 14001
original_url: https://compositecode.blog/2018/05/09/eliminating-machine-bias-w-mary-ann-brennan-getting-from-machine-learning-outputs-to-decisions-timely-things/
categories:
- Conferences
- machine learning
- Ml4all
- Unknown Code Ramblings
tags:
- conferences
- developer conferences
- machine learning
- Ml4all
excerpt: Meet Mary Ann Brennan (@mabmierau) presenting… Eliminating Machine Bias Mary Ann is a jack-of-all-trades software engineer with background in iOS and full-stack web at a bunch of startups you’ve probably never heard of. She’s currently using her extended maternity leave to refresh her studies in Artificial Intelligence, the concentration for her master’s in Computer Science …
image: /wp-content/uploads/2018/04/ml4all-banner.png
---

Meet Mary Ann Brennan ([@mabmierau](https://twitter.com/mabmierau)) presenting…

## Eliminating Machine Bias

![mary-ann-brennan](/wp-content/uploads/2018/05/mary-ann-brennan.jpg)

Mary Ann is a jack-of-all-trades software engineer with background in iOS and full-stack web at a bunch of startups you’ve probably never heard of. She’s currently using her extended maternity leave to refresh her studies in Artificial Intelligence, the concentration for her master’s in Computer Science at Stanford. She recently completed Coursera’s Deep Learning specialization.

Mary Ann will give a quick overview of the machine bias problem. She’ll provide a definition (and contrast with statistical bias) and show examples like criminal justice system algorithms with racial bias and machine translation algorithms with gender bias.

Mary Ann will also pull an example from the Deeplearning.ai courses that shows how to remove gender bias from word representations. She’s been surprised how simple and manageable it was to do and hopes this will help inspire people to take the extra step to consider how they might eliminate bias in their work. Time permitting, she’ll also aim to round the talk out with other techniques and more info on what to look for in your own data.

In Brennan’s talk, there may even be a code up of web-based interactive before and after view of word representations that you can check out, maybe. Be sure to ask about it, as it might be in *under construction*!

*Meet Robert Dodier ([@robert-dodier](https://twitter.com/robert-dodier)) presenting…*

## Getting from Machine Learning Outputs to Decisions

![robert-dodier](/wp-content/uploads/2018/05/robert-dodier.jpg)

Robert is interested in Bayesian inference and decision analysis, among many other topic. He’s got a background in math, computer science, and engineering. He also wrote his PhD dissertation on Bayesian network models applied to engineering problems. Since then he’s worked on statistical analysis, including machine learning, in different domains and also worked for some years on a agent-based system for control of distributed energy resources.

You’ve set up a machine learning pipeline and it’s delivering predictions and estimates in real time just as you hoped it would! Now, what can you do with those numbers? Intuitively, we think that if we compute a prediction that an event A is more likely than another event B, we should probably take an A-related action instead of a B-related action. But not if the A-action is really expensive compared to the B-action; then we’d hesitate unless we’re very sure about A. We could set up some rules to post-process the predictions to figure out which action to take. That sounds kind of hackish.

But wait! The good news is that we can formalize the decision problem in terms of statements of beliefs (i.e., probabilities) and values or preferences (i.e., utilities). Typical machine learning algorithms can produce probabilities, which we’ll take as the inputs for the decision-making step. Given fairly broad assumptions, the right way to make a decision is to take the action which maximizes expected (i.e., weighted average) utility. This gives a straightforward recipe for deriving actions from beliefs and preferences. Typically the expected utility calculation is much simpler than the belief calculation, so we can easily a devise a decison-making back end for our machine learning pipeline.

In this talk, Robert will pose some real-world decision problems and then talk about the features they have in common. He’ll describe a framework for finding best actions for such problems in general, and show how the framework applies to the problems he posed at the beginning of the talk. He’ll emphasize the idea that a formal decision making analysis gives an obvious way to inject business logic into the pipeline in a clear and easily-modified way.

- Manuel -> [Barriers To Accelerating The Training Of Artificial Neural Networks – A Systemic Perspective](/2018/05/15/barriers-to-accelerating-the-training-of-artificial-neural-networks-a-systemic-perspective-meet-manual-muro/)
- Ashutosh -> [Conducting a Data Science Contest in Your Organization](/2018/05/10/conducting-a-data-science-contest-in-your-organization-w-ashutosh-sanzgiri/)
- Poul -> [From Zero to Machine Learning for Everyone](/2018/05/10/from-zero-to-machine-learning-for-everyone-w-poul-peterson/)
- Anna -> [Your First NLP Machine Learning Project: Perks and Pitfalls of Unstructured Data](/2018/05/10/your-first-nlp-machine-learning-project-perks-and-pitfalls-of-unstructured-data-w-anna-widiger/)
- Kaleo Ha’o -> [Jump or Not to Jump: Solving Flappy Bird with Deep Reinforcement Learning](/2018/05/10/jump-or-not-to-jump-solving-flappy-bird-with-deep-reinforcement-learning-w-kaleo-hao/)
- Mary & Robert -> [Eliminating Machine Bias & Getting from Machine Learning Outputs to Decisions… timely things!](/2018/05/09/eliminating-machine-bias-w-mary-ann-brennan-getting-from-machine-learning-outputs-to-decisions-timely-things/)
- Kirsten & Rich -> [Now, Kirsten Westeinde & Rich Jolly](/2018/05/04/now-kirsten-westeinde-rich-jolly/)
- Jon & Amy -> [Say Hello to Jon and Amy @ML4ALL!](/2018/05/03/say-hello-to-jon-and-amy-ml4all/)
- Igor & Carol -> [More @ML4ALL Intros: Meet Igor & Carol! Also, the bike ride map!](/2018/05/01/more-ml4all-intros-meet-igor-carol-also-the-bike-ride-map/)
- Clair & Ricky -> [@ML4ALL Meet Clair J. Sullivan & Ricky Hennessy](/2018/04/30/ml4all-meet-clair-j-sullivan-ricky-hennessy/)
- Paige & Suz -> [ML4ALL Speakers – Meet Paige & Suz](/2018/04/29/ml4all-speakers-meet-paige-suz/)
