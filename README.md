# GSE---TEAM-A

## Getting started

1. Get [Python](https://www.python.org/) (This project has been developed with version 3.9.4)

1. Get [Anaconda](https://www.anaconda.com/products/individual) to use this project's Jupyter notebooks

1. Install Python packages to your local environment and Anaconda (refer to [requirements.txt](requirements.txt))

1. Get required datasets by following [Usage of Data](#usage-of-data)

## Usage of Data

Data that is used for the functionality in this repository (e.g. *.csv files) should be placed within the directory ./resources that is ignored by git.

The used datasets have been collected from multiple sources and have to be downloaded __manually__ and placed within the __resources__ directory (Currently, you have to create this directory manually). 

You can get the sources from the following locations (For additional details please refer to the papers referenced from the respective authors):
- [auto_labeled_data.csv](https://github.com/t-davidson/hate-speech-and-offensive-language/blob/507feccf0f3cf609409f765a08e0bbdac0a33d68/data/labeled_data.csv) (currently has to be renamed)
- [Ethos_Dataset_Binary.csv](https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset/blob/master/ethos/ethos_data/Ethos_Dataset_Binary.csv)
- [fox_news.csv](https://github.com/sjtuprog/fox-news-comments/blob/914b6bcdff380b16b6a11818e4760529fe23f2f3/annotated-threads/all-comments.txt)
    - rename the file
    - remove existing semicolons
    - replace the separating colons ':' with semicolons ';'
    - add this header: 'class;tweet'
- ["IMDB Dataset.scv"](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- [OLIDv1.0](https://github.com/idontflow/OLID) (folder currently has to be renamed)

The resources directory then should look like this:

![Default resources directory](docs/imgs/resources_default.JPG)
