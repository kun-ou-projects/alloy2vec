# Unveiling 35 years of progress in metallic materials for extreme environments with word-embedding

## Overview

This project involves training and utilizing a series of word embeddings models, specifically designed for analyzing abstracts related to metallic materials for extreme environments. Building upon the model by Pei et al. (2023), all abstracts and titles were used for transfer learning to obtain benchmark word embeddings. Then the years from 1989 to 2023 were divided into six time periods, and new time-series embeddings were trained using word2vec. Following this, orthogonal Procrustes analysis was conducted to align these embeddings with the benchmark word embeddings, thereby enabling comparisons across different time periods.

## Getting Started

### Environment Setup ###
Ensure run this program under Python 3.8 environment. 

Run: 
```python
pip install --ignore-installed -r requirements.txt.
```
to download related packages. If failed, please download them seperately by using `conda install` or `pip install`.

Run the following command :
```python
python setup.py install
```
This will download the required benchmark word embeddings and time-series embeddings and move them to the directories `training/models/` and `training/models/aligned_time_series_embeddings/`. If the download of models fails, manually download the models and place them in the respective folders. If the download of packages fails, use `pip install` or `conda install`.

### Data Files ###
Download necessary data files for ChemDataExtractor:
```python
cde data download
```

### Important Note ###
To update or create new models, please execute commands in the main directory `tracking_progress_metallic_materials` to avoid errors which is "no xxx files or directory".

## Data Processing ##

Titles and DOIs of the literature are stored in `processing/data/titles_and_dois.txt`. We downloaded titles and abstracts from the Web of Science, removed unnecessary punctuation, and connected key phrases with underscores as specified in `keywords/substitute.py`. No additional processing is needed at this stage as model updates or builds involve further corpus processing.

## Model Training ##
To update an existing model using a test corpus, run:
```python
python training/updated_phrase2vec_parallel.py -hs -sg --epochs=30 --corpus "training/test.txt" --model_name test_update
```

To build a new model using a test corpus, run:
```python
python training/phrase2vec.py -hs -sg --epochs=30 --corpus "training/test.txt" --model_name test_new
```

The content in `training/all_ents.p` includes the phrases that we need to retain when training the model. If you wish to perform the same operation, add the `-include_extra_phrases` at the end.

## Orthogonal Procrustes Analysis ##
This file `training/gaussian_procrustes.py` primarily focuses on processing time-series word embeddings to enable comparison of the vector of the same word across different time periods.
Below is an example:
```python
python "training/gaussian_procrustes.py" "training/models/updated_1model_all" "training/raw_models/" --output "training/aligned_timeslice_models/"
```