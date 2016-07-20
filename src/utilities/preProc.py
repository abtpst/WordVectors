'''
Created on Jul 15, 2016

@author: atomar
'''
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
# Here is the function review_to_sentences 

def review_to_sentences(review, tokenizer, sentiment="",removeStopwords=False, removeNumbers=False, removeSmileys=False):
    """
    This function splits a review into parsed sentences
    :param review:
    :param tokenizer:
    :param removeStopwords:
    :return: sentences, list of lists
    """
    # review.strip()remove the white spaces in the review
    # use tokenizer to separate review to sentences
    
    rawSentences = tokenizer.tokenize(review.strip())

    cleanedReview = []
    for sentence in rawSentences:
        if len(sentence) > 0:
            cleanedReview += review_to_words(sentence, removeStopwords, removeNumbers, removeSmileys)

    if(sentiment != ""):
        cleanedReview.append(sentiment)
              
    return cleanedReview

#The function review_to_words

def review_to_words(rawReview, removeStopwords=False, removeNumbers=False, removeSmileys=False):
    
    # use BeautifulSoup library to remove the HTML/XML tags (e.g., <br />)
    reviewText = BeautifulSoup(rawReview).get_text()

    # Emotional symbols may affect the meaning of the review
    smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^)
                :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D :( :/ :-( :'( :D :P""".split()
    smiley_pattern = "|".join(map(re.escape, smileys))

    # [^] matches a single character that is not contained within the brackets
    # re.sub() replaces the pattern by the desired character/string
    
    # Check to see how we need to perform cleanup
    if removeNumbers and removeSmileys:
        reviewText = re.sub("[^a-zA-Z]", " ", reviewText)
    elif removeSmileys:
        reviewText = re.sub("[^a-zA-Z0-9]", " ", reviewText)
    elif removeNumbers:
        reviewText = re.sub("[^a-zA-Z" + smiley_pattern + "]", " ", reviewText)
    else:
        reviewText = re.sub("[^a-zA-Z0-9" + smiley_pattern + "]", " ", reviewText)


    # split in to a list of words
    words = reviewText.lower().split()

    if removeStopwords:
        # create a set of all stop words
        stops = set(stopwords.words("english"))
        # remove stop words from the list
        words = [w for w in words if w not in stops]

    # for bag of words, return a string that is the concatenation of all the meaningful words
    # for word2Vector, return list of words
    # return " ".join(words)
               
    return words

def clean_data(data):
    """
    clean the training and test data and return a list of words
    :param data:
    :return:
    """
    # raise an error if there is no review column
    try:
        reviewsSet = data["review"]
    except ValueError:
        print('No "review" column!')
        raise

    cleaned_data = [review_to_words(review, True, True, False) for review in reviewsSet]
    
    return cleaned_data