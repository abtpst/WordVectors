import pandas as pd
import nltk
import json
import logging
import utilities.preProc as preProc

if __name__ == '__main__':
    
    #Set up logging configurations
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
    
    #Read labeled and unlabeled training data
    train = pd.read_csv("../../data/labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

    unlabeled_train = pd.read_csv("../../data/unlabeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
    
    #Choose tokenizer from nltk
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    
    num_reviews = len(train["review"])
    
    labeled = []
    
    #Clean labeled reviews
    for i in range(0, num_reviews):
        
        if( (i+1)%1000 == 0 ):
            
            print ("Labeled Review %d of %d\n" % ( i+1, num_reviews ))
        
        #The function review_to_sentences has been defined below
        labeled.append(preProc.review_to_sentences(train.review[i], tokenizer,str(train.sentiment[i])))
    
    #Save cleaned up labeled reviews
    json.dump(labeled,open("../../data/labeledSentiFFF.json", "w"))
    
    unlabeled = []
    
    #Clean unlabeled reviews    
    for i in range(0, num_reviews):
        
        if( (i+1)%1000 == 0 ):
            
            print ("Unlabeled Review %d of %d\n" % ( i+1, num_reviews ))
        
        #The function review_to_sentences has been defined below
        unlabeled.append(preProc.review_to_sentences(unlabeled_train.review[i], tokenizer))    
    
    #Save cleaned up unlabeled reviews
    json.dump(unlabeled,open("../../data/unlabeledFFF.json", "w"))