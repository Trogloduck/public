### Table of contents
- [[#Intro]]
- [[#Data collection and analysis]]
- [[#AI models]]

___
### Intro
[[#Table of contents|Back to the top]]

- **Rule-based programming**: just if else statements
- **Machine learning**: machine creates its own rules based on data
- **Deep learning**: ability to process unstructured data
- **Generative AI**: ability to generate data

**AI vs Expert system**
Expert can sometimes reach 100% accuracy based on some explicit rules
For instance, BMI = weight/height²
If we feed AI with a lot of weight, height, BMI data, it will not reach 100% accuracy as without context it won't create the BMI = weight/height² formula
AI is better used when we don't know the rule

**Darktrace** company: uses AI machine learning to detect attacks

___
### Data collection and analysis
[[#Table of contents|Back to the top]]

[Datasets for AI training](https://www.kaggle.com)

1. Data
	1. Acquisition: collect -- web scraping, open data, ...
	2. Cleaning: most of the work
	3. Analysis: understand data
2. Model training: feeding model with data
3. Result evaluation: feedback to correct predictions

Kinds of data
- Structured: tabular data
- Unstructured
	- Text
	- Image
	- Sound
	- Video

___
### AI models
[[#Table of contents|Back to the top]]

#### Supervised learning

1. Labeled data
2. Training
3. Predicting label

Types
- Regression: predicting continuous variable
- Classification
	- Binary: boolean
	- Multi-class: item
	- Multi-label: collection of items

#### Unsupervised learning

1. Unlabeled data
2. Training
3. Clustering: create groups/communities
4. Predicting to what group item belongs

#### Generative models

1. Observations
2. Training
3. Generation

- LLM: Large Language Models -- text
- DIF: Diffusion models -- images

**RAG** -- Retrieval-Augmented Generation: modifies interactions with LLM, model responds to user queries with reference to specified set of documents

https://huggingface.co/: **finetuned** models for different tasks