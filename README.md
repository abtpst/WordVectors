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

#### 5. Tie this virtual environment to the project
The python interpreter for this project should point to the conda virtual environment we created above. Note that we can use this environment for `doc2vec` as well.

#### 6. Now you are ready to run the scripts