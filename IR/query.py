from IR.parser import Parser
from IR.vector import VectorModel
from spellchecker import SpellChecker

import os


class queryProcess(Parser):        
    vector = VectorModel()
    def __init__(self):
        Parser.__init__(self)
    def getQueryFromUser(self):
        val = input("Enter your value: ")
        val = self.searchEnginStep(val)
        # self.vector.AUC()
        self.vector.getResult(val, self.tokenfile)
        print(val)
    def spellingCorrection(self, list):
        spell = SpellChecker()
        misspelled = spell.unknown(list)
        for word in misspelled:
            # Get the one `most likely` answer
            print(spell.correction(word))
            index = list.index(word)
            list[index] = spell.correction(word)
            # Get a list of `likely` options
            print(spell.candidates(word))
        if(len(misspelled) > 1):
            print("did You Mean")
            print(" " .join(list))
