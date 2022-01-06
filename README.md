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

## Data description

### Davidson's Automated Hate Speech Detection and the Problem of Offensive Language dataset

~~~
@inproceedings{hateoffensive,
  title = {Automated Hate Speech Detection and the Problem of Offensive Language},
  author = {Davidson, Thomas and Warmsley, Dana and Macy, Michael and Weber, Ingmar}, 
  booktitle = {Proceedings of the 11th International AAAI Conference on Web and Social Media},
  series = {ICWSM '17},
  year = {2017},
  location = {Montreal, Canada},
  pages = {512-515}
  }
~~~

```csv
,count,hate_speech,offensive_language,neither,class,tweet
0,3,0,0,3,2,!!! RT @mayasolovely: As a woman you shouldn't complain about cleaning up your house. &amp; as a man you should always take the trash out...
1,3,0,3,0,1,!!!!! RT @mleew17: boy dats cold...tyga dwn bad for cuffin dat hoe in the 1st place!!
2,3,0,3,0,1,!!!!!!! RT @UrKindOfBrand Dawg!!!! RT @80sbaby4life: You ever fuck a bitch and she start to cry? You be confused as shit
3,3,0,2,1,1,!!!!!!!!! RT @C_G_Anderson: @viva_based she look like a tranny
4,6,0,6,0,1,!!!!!!!!!!!!! RT @ShenikaRoberts: The shit you hear about me might be true or it might be faker than the bitch who told it to ya &#57361;
5,3,1,2,0,1,"!!!!!!!!!!!!!!!!!!""@T_Madison_x: The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes! &#128514;&#128514;&#128514;"""
6,3,0,3,0,1,"!!!!!!""@__BrighterDays: I can not just sit up and HATE on another bitch .. I got too much shit going on!"""
```

The data are stored as a CSV containing 5 columns [—see more](https://github.com/t-davidson/hate-speech-and-offensive-language):

- `count` = number of CrowdFlower users who coded each tweet (min is 3, sometimes more users coded a tweet when judgments were determined to be unreliable by CF).
- `hate_speech` = number of CF users who judged the tweet to be hate speech.
- `offensive_language` = number of CF users who judged the tweet to be offensive.
- `neither` = number of CF users who judged the tweet to be neither offensive nor non-offensive.
- `class` = class label for majority of CF users.
    0 - hate speech
    1 - offensive  language
    2 - neither
