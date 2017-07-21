'''
Created on 07 July 2017

@author: Eva
'''

import unittest
from rearranging_cars import rearrange_cars, Move

class UnknownLanguageTest(unittest.TestCase):
    def setUp(self):
        self.initial_array = [1, 2, 0, 3]
        self.final_array = [3, 1, 2, 0]
        self.solution = [Move(0,2), Move(3,0), Move(1,3), Move(2,1), Move(3,2)]
        self.maxDiff = None

    def testKnownCase(self):
        self.assertTrue(self.check_list_contents(rearrange_cars(self.initial_array, self.final_array), self.solution))
        
    def check_list_contents(self, result, expected):
        for i in range(len(result)):
            if result[i].get_origin() != expected[i].get_origin() and result[i].get_destination() != expected[i].get_destination():
                return False
        return True  
if __name__ == '__main__':
    unittest.main()
