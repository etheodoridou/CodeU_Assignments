import unittest
from count_islands import count_islands_rec

class CountingIslandsTest(unittest.TestCase):

    def setUp(self):
        self.array = [[False, True, False, True], [True, True, False, False], [False, False, True, False], [False, False, True, False]]
        self.big_array = [[False]*100, [True] * 100, [False] * 100, [True] * 100] * 25
    def testKnownCases_rec(self):
        self.assertEqual(3, count_islands_rec(4, 4, self.array))
        #self.assertEqual(50, count_islands_rec(100, 100, self.big_array))
if __name__ == '__main__':
    unittest.main()