'''
Created on 9 June 2017

@author: Eva
'''

class Dictionary:
    
    def __init__(self, words, prefixes):
        self.__words = words
        self.__prefixes = prefixes
        
    def isWord(self, inputString):
        return inputString in self.__words
    
    def isPrefix(self, inputString):
        return inputString in self.__prefixes