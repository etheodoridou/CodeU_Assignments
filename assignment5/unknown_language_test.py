'''
Created on 07 July 2017

@author: Eva
'''

import unittest
from unknown_language import get_alphabet_adj

class UnknownLanguageTest(unittest.TestCase):
    def setUp(self):
        self.array = ['ART', 'RAT', 'CAT', 'CAR']
        self.mixed_case_array = ['ART', 'art', 'RAT', 'rat', 'CAT', 'cat', 'CAR', 'car']
    
    def lowerCapitalCase(self):
        self.assertEqual(['A', 'a', 'T', 't', 'R', 'r', 'C', 'c'], get_alphabet_adj(self.mixed_case_array))
        
    def testKnownCase(self):
        self.assertEqual(['A', 'T', 'R', 'C'], get_alphabet_adj(self.array))
        
    def errorCases(self):
        empty_array = []
        
        with self.assertRaises(ValueError): 
            get_alphabet_adj(None)
        with self.assertRaises(ValueError):
            get_alphabet_adj(empty_array)
     
if __name__ == '__main__':
    unittest.main()