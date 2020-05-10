# NER-Classifier-for-Company-Names
## Goal

The goal is to find out companies and their symbols in a story text. Once you get the company information, you may want to map it to symbol 

For ex.

Apple Inc. -> AAPL

Google Inc. -> GOOG


Once you get this information, you need to count how many times one particular symbol appears in the story. Sort them by count and whichever appears the most should be listed as security and the list of all securities appearing would be as a list of securities.

#### Input: 

The story text found in the dataset, symbol pickle file

#### Output:

Simple valid json containing two attributes security and securities. 

## Solution
I have used Spacy Word Embedding to generate Entity for [uci-news-aggregator](https://archive.ics.uci.edu/ml/datasets/News+Aggregator) Dataset.

1. Main problem in NER for Company names is that Company Names sometimes contains postfix like Ltd,Inc,etc.
![](img/fuz.png)

So we use a algorithm named **[Levenshtein Distance ](https://dzone.com/articles/the-levenshtein-algorithm-1)** ,WHich calculates similarity betyeen two strings.

    ('Microsoft','Microsoft') = 100 %
    ('Microsoft Corp','Microsoft') = 78 %
    ('Microsoft Ltd,'Microsoft') = 81 %
    
       
2. Find Entity in input Text:
We do this by using spacy's pretrained entitity classifier

3. Then we do simple comparison of entitity and company name in symbols.pickle file

### Instructions

1. Fork the repo
2. Clone the repo
3. Run the [run.sh](run.sh) file to install required libraries
4. Change the string named **sentence** in [get_input.py](get_input.py)


       sentence=" "  
    
to 

    #example
    sentence="Apple, Amazon and Microsoft are reporting earnings after market close on April 30th."

5. run the get_input.py file

6. Output will be:

       {"security": "AAPL", "securities": ["AAPL", "MSFT"]}
       
**Note:** As there is no **Amazon** in the output because it was not present in **the symbols.pickle**       






    




