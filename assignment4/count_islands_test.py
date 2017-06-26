'''
Created on 23 June 2017

@author: Eva
'''

import unittest
from count_islands import count_islands_rec, count_islands_iter

class CountingIslandsTest(unittest.TestCase):

    def setUp(self):
        self.array = [[False, True, False, True], [True, True, False, False], [False, False, True, False], [False, False, True, False]]
        self.true_array = [[True] * 10] * 10
        self.false_array = [[False] * 10] * 10
        self.empty_array = []
        self.empty_array_element = [[]]
        self.big_array = [[False]*100, [True] * 100, [False] * 100, [True] * 100] * 25
    
    def testBaseCasesRec(self):
        self.assertEqual(0, count_islands_rec(10, 10, self.false_array))
        self.assertEqual(1, count_islands_rec(10, 10, self.true_array))
        with self.assertRaises(ValueError): 
            count_islands_rec(100, 100, None)
        with self.assertRaises(ValueError):
            count_islands_rec(100, 100, self.empty_array)
        with self.assertRaises(ValueError):
            count_islands_rec(100, 100, self.empty_array_element)
        
    def testKnownCasesRec(self):
        self.assertEqual(3, count_islands_rec(4, 4, self.array))
        self.assertEqual(50, count_islands_rec(100, 100, self.big_array))
        
    def testBaseCasesIter(self):
        self.assertEqual(0, count_islands_iter(10, 10, self.false_array))
        self.assertEqual(1, count_islands_iter(10, 10, self.true_array))
        with self.assertRaises(ValueError): 
            count_islands_iter(100, 100, None)
        with self.assertRaises(ValueError):
            count_islands_iter(100, 100, self.empty_array)
        with self.assertRaises(ValueError):
            count_islands_iter(100, 100, self.empty_array_element)
        
    def testKnownCasesIter(self):
        self.assertEqual(3, count_islands_iter(4, 4, self.array))
        self.assertEqual(50, count_islands_iter(100, 100, self.big_array))
        
if __name__ == '__main__':
    unittest.main()
