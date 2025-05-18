from numpy.linalg import norm
from numpy import NAN, dot
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# Importing math library
import math
import os.path
from os import path
import pickle
import ast
import numpy as np
from sklearn import metrics


class VectorModel:
    tfId = []
    term = set()
    fileVector = dict()
    # this function to compute cos similarity

    def cosSimilarity(self, v1, v2):
        x = dot(v1, v2) / (norm(v1) * norm(v2))
        return x

    def queryVector(self, stemmed_list_query, terms):
        query_vec = []
        for term in terms:
            query_vec.append(stemmed_list_query.count(term))
        return query_vec

    def filesVector(self, files, terms):

        vectors = dict()
        count = 0
        for key, value in files.items():
            vec = []
            count = len(value)
            for idx, term in enumerate(terms):
                Termcount = value.count(term)
                vec.append(Termcount/count)
                if(Termcount > 0):
                    self.tfId[idx] += 1

            vectors[key] = vec
        return vectors

    def termVector(self, files):
        if(path.exists("term.txt")):
            terms = self.read_fromFile("term.txt")
        else:
            terms = set()
            for key, value in files.items():
                for w in value:
                    terms.add(w)
            terms = sorted(terms)

            self.save_inFile("term.txt", terms)
        if(len(self.tfId) == 0):
            self.tfId = np.zeros(len(terms))

        return terms

    def most_similar(self, similarity_list, min_talks=1):

        most_similar = []
        while min_talks > 0:
            tmp_index = max(similarity_list, key=similarity_list.get)
            most_similar.append(tmp_index)
            similarity_list[tmp_index] = 0
            min_talks -= 1
        return most_similar

    def getResult(self, query, files):
        if(len(self.term) == 0):
            self.term = self.termVector(files)
            if(not path.exists("idf_fileVector.txt")):
                self.fileVector = self.filesVector(files, self.term)
            else:
                self.fileVector = dict()
            self.idf_term(len(files))
            self.fileVector = self.idf_fileVector(self.fileVector)
        queryVec = self.queryVector(query, self.term)
        queryVec = self.idf_Vector(queryVec)
        similarity_list = dict()
        for key, value in self.fileVector.items():
            similarity_list[key] = self.cosSimilarity(queryVec, value)
        index = self.most_similar(similarity_list, 10)
        print(index)

    def idf_term(self, docNumb):
        if(path.exists("idf_term.txt")):
            self.tfId = self.read_fromFile("idf_term.txt")
        else:
            for idx, term in enumerate(self.tfId):
                self.tfId[idx] = 1 + math.log(docNumb/self.tfId[idx])
            list2 = self.tfId
            self.saveList_inFile("idf_term.txt", list2)

    def idf_fileVector(self, fileVector):
        if(path.exists("idf_fileVector.txt")):
            fileVector = self.read_fromFile("idf_fileVector.txt")
        else:
            for key, value in fileVector.items():
                for idx, term in enumerate(value):
                    value[idx] = self.tfId[idx]*value[idx]
            self.save_inFile("idf_fileVector.txt", fileVector)
        return fileVector

    def idf_Vector(self, fileVector):
        for idx, term in enumerate(fileVector):
            fileVector[idx] = self.tfId[idx] * fileVector[idx]
        return fileVector

    def save_inFile(self, fileName, list2):
        with open(fileName, 'w') as f:
            f.write(str(list2))  # set of numbers & a tuple
        f.close()

    def read_fromFile(self, fileName):
        with open(fileName, 'r') as f:
            try:
                score = ast.literal_eval(f.read())
            except:
                with open(fileName, 'r') as f:
                    score = []
                    for line in f:
                        score.append(float(line.strip()))
        return score

    def saveList_inFile(self, fileName, list2):

        with open(fileName, 'w') as f:
            f.writelines(["%s\n" % item for item in list2])
        f.close()



