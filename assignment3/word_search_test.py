import unittest
from word_search import WordSearch
from dictionary import Dictionary

class WordSearchTest(unittest.TestCase):

    def setUp(self):
        self.dictionary = Dictionary(['CAR', 'CARD', 'CART', 'CAT'], ['C', 'CA', 'CAR', 'CARD', 'CART', 'CAT'])
        self.grid = [['A', 'A', 'R'],['T', 'C', 'D']]
        self.word_search = WordSearch()
        
        self.fourbyfourgrid = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j','k','l'], ['m','n','o','p']]
        self.fourbyfourdict = Dictionary(['abfg','jfbcdhl','olgb'],['a','ab','abf','abfg','j', 'jf','jfb','jfbc','jfbcd','jfbcdh','jfbcdhl','o','ol','olg','olgc'])
    
    def testKnownCases(self):
        self.assertCountEqual(['CAR', 'CARD', 'CAT'], self.word_search.words_found_in_grid(3, 2, self.grid, self.dictionary))

if __name__ == '__main__':
    unittest.main()
