#!/usr/bin/env python

import Exercise1
import unittest

class Exercise1Test(unittest.TestCase):

  def testBaseCases(self):
    self.assertEquals(True, Exercise1.is_permutation("", ""))
    self.assertEquals(False, Exercise1.is_permutation(None, None))

  def testKnownCases(self):
    self.assertEquals(True, Exercise1.is_permutation("Triangle", "Integral"))
    self.assertEquals(True, Exercise1.is_permutation("Silent", "Listen"))
    self.assertEquals(False, Exercise1.is_permutation("Apple", "Pabble"))

if __name__ == '__main__':
  unittest.main()