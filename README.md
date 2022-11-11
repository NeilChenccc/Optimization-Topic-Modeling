# Optimization-Topic-Modeling

## Introduction 
Topic modeling, a machine learning technique that automatically detects topics for a set of documents, are crucial in the data analysis process of social media posts, emails, chats, open-ended survey responses, etc. By using topic analysis models, businesses are able to offload simple tasks onto machines instead of overloading employees with too much data (Pascual, 2019).

Latent Dirichlet Allocation (LDA) is a generative probabilistic model for collections of discrete data such as text corpora, which is one of the most popular methods in topic modeling. LDA is a three-level hierarchical Bayesian model, in which each item of a collection is modeled as a finite mixture over an underlying set of topics. Each topic is, in turn, modeled as an infinite mixture over an underlying set of topic probabilities. In the context of text modeling, topic probabilities provide an explicit representation of a document. Therefore, the words with a higher frequency will be placed on more emphasis.

However, when it comes to the definition of the subtopics for documents under the same main topic, more common words will appear in each document, indicating a higher weight in the model. Therefore, modifications need to be made for the classic LDA model to eliminate the effects of common high-frequency words. 

In this project, the LDA model will be implemented through two main improvements. First, the new model will introduce bigram, which are two words coming together in the corpus language model. By aggregating data at the n-gram level, we can pull out themes that would otherwise be impossible to identify when analyzing search terms in their entirety (Gridley & Konowal, 2020). Second, a semi-supervised topic model designed with large domain-specific data sets in mind based on the combination of Noiseless Latent Dirichlet Allocation (NLDA) and Guided Topic-Noise Model (GTM) will be applied to reduce noise words.

## Data

## Methodology

## Result

## Discussion


## Referrence
Topic modeling: An introduction. MonkeyLearn Blog. 2019 Sep 26 [accessed 2022 Nov 10]. https://monkeylearn.com/blog/introduction-to-topic-modeling. 

An introduction to topic-noise models | by Rob Churchill | Oct, 2022 ... [accessed 2022 Nov 11]. https://towardsdatascience.com/an-introduction-to-topic-noise-models-c48fe77e32a6.


https://www.seerinteractive.com/blog/what-are-ngrams-and-uses-case/
