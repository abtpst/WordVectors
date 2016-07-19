# WordVectors
Repo for exploring Word2Vec and Doc2Vec

### Setup

#### 1. Install Anaconda

We will be using python 3 with Anaconda. Download the windows installer from

http://repo.continuum.io/archive/Anaconda3-4.1.1-Windows-x86_64.exe

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