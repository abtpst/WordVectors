import pandas as pd
import json,os
import utilities.preProc as preProc 
import nltk.data
from gensim.models import word2vec

if __name__ == '__main__':
    
    # Read labelled training data
    train = pd.read_csv("././data/labeledTrainData.tsv",
                    header=0, delimiter="\t", quoting=3)
    
    # Read unlabelled training data
    
    unlabeled_train = pd.read_csv("././data/unlabeledTrainData.tsv",
                    header=0, delimiter="\t", quoting=3)
    
    # Load a tokenizer from nltk
    
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Initialize list for holding cleaned up sentences
    
    bagOfsentences = []
    
    # Parse labeled sentences and append to bagOfsentences
    
    print("Parsing sentences from labeled training set")
    for review in train["review"]:
        #review = review.decode("utf8","ignore")
        bagOfsentences.append(preProc.review_to_sentences(review, tokenizer, False, True, False))
    
    # Parse unlabeled sentences and append to bagOfsentences
    
    print("Parsing sentences from unlabeled set")
    for review in unlabeled_train["review"]:
        #review = review.decode("utf8","ignore")
        bagOfsentences.append(preProc.review_to_sentences(review, tokenizer, False, True, False))
    
    # Save bagOfsentences
    
    json.dump(bagOfsentences,open("././classifier/bagOfsentences.json", "w"))