# NER-Classifier-for-Company-Names
##### Goal

The goal is to find out companies and their symbols in a story text. Once you get the company information, you may want to map it to symbol 

For ex.

Apple Inc. -> AAPL

Google Inc. -> GOOG


Once you get this information, you need to count how many times one particular symbol appears in the story. Sort them by count and whichever appears the most should be listed as security and the list of all securities appearing would be as a list of securities.

##### Input: 

The story text found in the dataset, symbol pickle file

##### Output:

Simple valid json containing two attributes security and securities. 

## Solution
I have used Spacy Word Embedding to generate Entity for [uci-news-aggregator](https://archive.ics.uci.edu/ml/datasets/News+Aggregator) Dataset.
And the model is trained using Bidirectional LSTM Model

### Steps:

#### 1)Formatting the data to BIO tagging 

The Data is in form of text sentences.We need to convert them to words and add a tag to all words.

We also have a file name [symbols.pickle](symbols.pickle) which contains the name of companies with their security name.

So we read that file and whenever we find any name in main dataset of words we change the tag of that word.

So to do all this we must run the command:

    python convert_data.py

![symbols.pickle](img/sym.png)
![](img/tex1.png)
![](img/tex2.png)

#### 2)Getting Training and Testing Data


