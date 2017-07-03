'''
Created on 23 June 2017

@author: Eva
'''

import unittest
from count_islands import count_islands_rec, count_islands_iter

class CountingIslandsTest(unittest.TestCase):

    def setUp(self):
        self.array = [[False, True, False, True], [True, True, False, False], [False, False, True, False], [False, False, True, False]]
    
    def errorCases(self, fn):
        empty_array = []
        empty_array_element = [[]]
        
        with self.assertRaises(ValueError): 
            fn(None)
        with self.assertRaises(ValueError):
            fn(empty_array)
        with self.assertRaises(ValueError):
            fn(empty_array_element)
    
    def allTrueCase(self, fn):
        true_array = [[True] * 10] * 10
        
        self.assertEqual(1, fn(true_array))
    
    def allFalseCase(self, fn):
        false_array = [[False] * 10] * 10
        
        self.assertEqual(0, fn(false_array))
        
    def largeMapCase(self, fn):
        big_array = [[False]*100, [True] * 100, [False] * 100, [True] * 100] * 25
        
        self.assertEqual(50, fn(big_array))
        
    def testErrorCasesRec(self):
        self.errorCases(count_islands_rec)
    
    def testErrorCasesIter(self):
        self.errorCases(count_islands_iter)
    
    def testAllTrueCaseRec(self):
        self.allTrueCase(count_islands_rec)
    
    def testAllTrueCaseIter(self):
        self.allTrueCase(count_islands_iter)
    
    def testAllFalseCaseRec(self):
        self.allFalseCase(count_islands_rec)
    
    def testAllFalseCaseIter(self):
        self.allFalseCase(count_islands_iter)
        
    def testKnownCaseRec(self):
        self.assertEqual(3, count_islands_rec(self.array))
    
    def testKnownCaseIter(self):
        self.assertEqual(3, count_islands_iter(self.array))
    
    def testLargeMapCaseRec(self):
        self.largeMapCase(count_islands_rec)
    
    def testLargeMapCaseIter(self):
        self.largeMapCase(count_islands_iter)
        
if __name__ == '__main__':
    unittest.main()