# WordVectors
Repo for exploring Word2Vec and Doc2Vec

### Setup

#### 1. Install Anaconda

We will be using python 3.5 with Anaconda. Download the installer from

https://www.continuum.io/downloads

and follow installation instructions

#### 2. Create conda virtual environment

    conda create -n word2vec_env pip

#### 3. Clone this git repo

    git clone https://github.com/abtpst/WordVectors.git

#### 4. Install all packages
Navigate to the cloned location and activate the environment created above

    activate word2vec_env
    
Now install the packages as 

    pip install -r requirements.txt
    
If you experience trouble installing `scipy` or `numpy`, follow these steps. Note that the environment must be activated and you should run these commands from the cloned location.

1. `conda install scipy`
2. `pip install -r requirements.txt`

#### 5. Bug fix for gensim 

In the versions of gensim, post 0.10.1, you need to make the following change

Modify the file `site-packages/gensim/models/word2vec.py` by changing line `1013` to 

    self.syn0[i] = self.seeded_vector(str(self.index2word[i]) + str(self.seed))
This fix is important as otherwise the word2vec training would fail.

#### 6. Tie this virtual environment to the project
The python interpreter for this project should point to the conda virtual environment we created above. Note that we can use this environment for `doc2vec` as well.

#### 7. Now you are ready to run the scripts

The `src` folder contains the packages for exploring `Word2Vec` and `Doc2Vec`. The respective Readme files with instructions are also provided.