import logging
import json
from gensim.models import word2vec

bagOfsentences = json.load(open("../../data/bagOfsentences.json","r"))

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
        level=logging.INFO)
    
# Set values for the parameters in Word2Vec

num_features = 500  # word vector dimensionality
# minimum word count: any word that does not occur at least this many times
# across all documents is ignored
min_word_count = 40
num_workers = 4  # Number of threads to run in parallel
context = 10  # Context window size
downsampling = 1e-3  # Downsample setting for frequent words

'''
Needed for python 3.x, before gensim 0.13.1

def myhash(obj):
    return hash(obj) % (2 ** 32)    
    
prior to gensim 0.13, the model declaration would be

model = word2vec.Word2Vec(bagOfsentences, workers=num_workers,
                          size=num_features, min_count=min_word_count,
                          window=context, sample=downsampling,hashfxn=myhash)

python 2.x declaration would be 

model = word2vec.Word2Vec(bagOfsentences, workers=num_workers,
                          size=num_features, min_count=min_word_count,
                          window=context, sample=downsampling
                          )
'''

print("Training model...")

model = word2vec.Word2Vec(bagOfsentences, workers=num_workers,
                          size=num_features, min_count=min_word_count,
                          window=context, sample=downsampling)
						  

"""
If you don't plan to train the model any further, calling
init_sims will make the model much more memory-efficient
If `replace` is set, forget the original vectors and only keep the normalized
ones = saves lots of memory!
"""
model.init_sims(replace=False)
    
# save the model for later use
# for loading, call Word2Vec.load()

model.save("../../classifier/Word2VectforNLPTraining")