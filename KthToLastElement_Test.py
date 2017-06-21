#!/usr/bin/env python

from linked_list import LinkedList, kth_to_last_element
import unittest

class KthToLastElement_Test(unittest.TestCase):

    def setUp(self):
        self.__linked_list = LinkedList()
        self.__linked_list.add_first(0)
        self.__linked_list.add_first(1)
        self.__linked_list.add_first(2)
        self.__linked_list.add_first(3)
        self.__linked_list.add_first(4)
        self.__linked_list.add_first(5)
        self.__linked_list.add_first(6)
        self.__linked_list.add_first(7)
        self.__linked_list.add_first(8)
        self.__list_head = self.__linked_list.get_head()
        
    def testBaseCases(self):
        self.__max_value = self.__linked_list.size()
        for i in range(0, self.__max_value):
            self.assertEqual(kth_to_last_element(self.__list_head, i), i)
        
    def testErrorCases(self):
        with self.assertRaises(ValueError): 
                kth_to_last_element(self.__list_head, -1)
                kth_to_last_element(self.__list_head, self.__max_value + 1)
        
    
if __name__ == '__main__':
    unittest.main()