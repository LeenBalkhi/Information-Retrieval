from IR.parser import Parser
import os


class corpus(Parser):
    def __init__(self):
        Parser.__init__(self)

    def readfile(self, f):

        with open(os.path.join(self.file_path, f), 'r') as file:
            return file.read()
    # -------------------------------------------------------------

    def readStupWordfile(self):
        with open(os.path.join(os.path.dirname(os.path.abspath("top_level_file.txt")), 'stop words.txt'), 'r') as file:
            lines = (line.rstrip() for line in file)
            # Non-blank lines in a list
            lines = list(line for line in lines if line)
        return lines

    def readCorpus(self):
        L = dict()
        files = os.listdir(self.file_path)
        for f in files:
            L[f] = (self.readfile(f))
        return L
    # -------------------------------------------------------------

    def offline(self):
        self.Stup = self.readStupWordfile()
        self.files = os.listdir(self.file_path)
        for f in self.files:
            value = self.readfile(f)
            value = self.searchEnginStep(value)
            self.tokenfile[f] = value
        print(self.tokenfile)
