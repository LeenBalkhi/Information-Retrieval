# import these modules
from nltk.tokenize import RegexpTokenizer
from IR.corpus import corpus
from IR.query import queryProcess

import re
from datetime import datetime
from nltk.corpus import wordnet as wn
from types import new_class
from typing import List
import nltk
import os
from os import path

from nltk.corpus.reader.wordnet import NOUN
from nltk.stem import WordNetLemmatizer

from spellchecker import SpellChecker
lemmatizer = WordNetLemmatizer()
file_path = os.path.join(os.path.dirname(__file__), "corpus")
Corpus = corpus()
query = queryProcess()


if(not path.exists("idf_fileVector.txt")):
    Corpus.offline()
    query.Stup=Corpus.Stup
else:
   query.Stup=Corpus.readStupWordfile()
# query.spellingCorrection(['stap','pley'])
while (True):
 query.getQueryFromUser() 
