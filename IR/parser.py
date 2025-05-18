# import these modules
from io import FileIO
from nltk.tokenize import RegexpTokenizer
import re
from datetime import datetime
from nltk.corpus import wordnet as wn
from types import new_class
from typing import List
import nltk
import os
import datefinder
from nltk.corpus.reader.wordnet import NOUN
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker
lemmatizer = WordNetLemmatizer()


class Parser:
    file_path: str
    Stup: FileIO
    files: FileIO = []
    tokenfile = {}

    # __init__ is known as the constructor

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(
            os.path.abspath("top_level_file.txt")), "corpus")

    def lemetization2(self, text):
        tagged = nltk.pos_tag(text)
        for idx in range(len(text)):
            if(tagged):
                if(tagged[idx][1][0].lower() == 'v' or tagged[idx][1][0].lower() == 'n'):
                    word = wn._morphy(text[idx], tagged[idx][1][0].lower())
                    if len(word) == 2:
                        text[idx] = word[1]
                    else:
                        if(len(word) == 1):
                            text[idx] = word[0]

        return text

    def ReFormatTime(self, string_with_dates):
        for string in string_with_dates:
            matches = datefinder.find_dates(string)
            try:
                for match in matches:
                    index = string_with_dates.index(string)
                    string_with_dates[index] = match.strftime(
                        "%m-%d-%Y")
            except:
                return string_with_dates
        return string_with_dates
    # -----------------------------------------------------------------

    def stemming(self, words):
        List = []
        ps = nltk.PorterStemmer()
        for w in words:
            List.append(ps.stem(w))
        return List

    def tokenization(self, text: str):
        tokenizer = RegexpTokenizer(
            "\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}|\w's+|\$[\d\.]+|\S+")
        return tokenizer.tokenize(text)

    def searchEnginStep(self, value):
        value = self.tokenization(value)
        value = self.removeStupWorld(self.Stup, value)
        value = self.ReFormatTime(value)
        value = self.remove_punctuation(value)
        value = self.stemming(value)
        value = self.lemetization2(value)
        value = self.remove_single_character(value)

        return value

    def lemetization(self, text):
        tagged = nltk.pos_tag(text)
        for idx in range(len(text)):
            if(tagged):
                text[idx] = lemmatizer.lemmatize(
                    text[idx], pos=tagged[idx][1][0].lower())
        return text

    def removeStupWorld(self, Stup, file):

        for text in Stup:
            for word in file:
                if word == text:
                    file.remove(word)
        return file

    def remove_punctuation(self, list2: List):
        for i, test_str in enumerate(list2):
            list2[i] = re.sub(r'[^a-zA-Z0-9_\s-]', '', list2[i])
        list2 = list(filter(None, list2))
        return list2

    def remove_single_character(self, list2):
        for word in list2:
                if(self.cheackIfNonUsefullToken(word)):
                    list2.remove(word)
                else:
                    if len(word) == 1:
                        list2.remove(word)
        return list2

    def cheackIfNonUsefullToken(self, token):
        unUsful = ['-', '--', '-19o', '-30o', '-a-month', '-soviet',
                   '00', '000', '000-a-week', '000000']
        if(token in unUsful):
            return True
        else:
            return False
