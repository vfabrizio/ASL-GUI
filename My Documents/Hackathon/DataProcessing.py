import os
import string
from PIL import Image
import random

class DataProcessing:
    def __init__(self):
        # initialize the a dictionary associating integers 0-25 to letter a-z
        self.__numLtrDict = dict(zip(range(0, 26), string.ascii_uppercase))
        self.__key = 0
    
        # initialize the dictionary associating integers 0-25 to each image obj
        self.__signDict = {}
        self.__partialSignDict = {}
        self.__initSignDict()
        self.__partialSignDict = self.__signDict.copy()
    
    def __initSignDict(self):
        for index in range(0, 26):
            filePath = os.path.join("images", str(self.__numLtrDict[index]) + ".png")
            self.__signDict[index] = Image.open(filePath)
    
    def generateChoices(self):
        self.__returnList = []
        # pop out a random key in the dictionary as a correct answer, save it 
        # and then delete it
        self.__key = random.sample(self.__partialSignDict.keys(), 1)[0]
        self.__returnList.append(self.__key)
        del self.__partialSignDict[self.__key]
        
        # copy the signDict to a temp dict and then manipulate it
        self.__temp2 = self.getWholeSignDict().copy()
        del self.__temp2[self.__key]
        self.__tempDict = self.__temp2.copy()
        
        for index in range(3):
            self.__tempKey = random.sample(self.__tempDict.keys(), 1)[0]
            self.__returnList.append(self.__tempKey)
            del self.__tempDict[self.__tempKey]
        
        random.shuffle(self.__returnList)
        
        return self.__returnList

    def resetPartialSignDict(self):
        self.__partialSignDict = self.__signDict.copy()

    def getPartialSignDict(self):
        return self.__partialSignDict
        
    def getWholeSignDict(self):
        return self.__signDict
        
    def getAnswer(self):
        return self.__key
        
    def getNumLtrDict(self):
        return self.__numLtrDict
