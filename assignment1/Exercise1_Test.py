#!/usr/bin/env python

import Exercise1
import unittest

class Exercise1Test(unittest.TestCase):

    def testBaseCases(self):
        self.assertTrue(Exercise1.is_permutation("", ""))
        self.assertFalse(Exercise1.is_permutation(None, None))
        self.assertFalse(Exercise1.is_permutation(None, "Silent"))
        self.assertFalse(Exercise1.is_permutation("Silent", None))
        self.assertTrue(Exercise1.is_permutation("a" * 10, "a" * 10))    
    
    def testKnownCases(self):
        self.assertTrue(Exercise1.is_permutation("Triangle", "Integral"))
        self.assertTrue(Exercise1.is_permutation("Silent", "Listen"))
        self.assertFalse(Exercise1.is_permutation("Apple", "Pabble"))
        self.assertTrue(Exercise1.is_permutation("1Hj)w", "W)Jh1"))  
    
    def testBaseCases_English(self):
        self.assertTrue(Exercise1.is_permutation_english("", ""))
        self.assertFalse(Exercise1.is_permutation_english(None, None))
        self.assertFalse(Exercise1.is_permutation_english(None, "Silent"))
        self.assertFalse(Exercise1.is_permutation_english("Silent", None))
        self.assertTrue(Exercise1.is_permutation("a" * 10, "a" * 10))      
    
    def testKnownCases_English(self):
        self.assertTrue(Exercise1.is_permutation_english("Triangle", "Integral"))
        self.assertTrue(Exercise1.is_permutation_english("Silent", "Listen"))
        self.assertFalse(Exercise1.is_permutation_english("Apple", "Pabble"))

    def testErrorCases(self):
        self.assertFalse(Exercise1.is_permutation_english("12345678", "87654321"))
    
if __name__ == '__main__':
    unittest.main()
