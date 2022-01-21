'''
Created on 22 May 2017

@author: Eva
'''

from binary_tree import BinaryTree, TreeNode
import binary_tree_service
import unittest
import sys

class Question1Test(unittest.TestCase):

    def setUp(self):
        root_node = TreeNode(16)
        node9 = TreeNode(9)
        node18 = TreeNode(18)
        node3 = TreeNode(3)
        node14 = TreeNode(14)
        node19 = TreeNode(19)
        node1 = TreeNode(1)
        node5 = TreeNode(5)
        self.binary_tree = BinaryTree(root_node)
        self.binary_tree.insert(node9, root_node, True)
        self.binary_tree.insert(node18, root_node, False)
        self.binary_tree.insert(node3, node9, True)
        self.binary_tree.insert(node14, node9, False)
        self.binary_tree.insert(node1, node3, True)
        self.binary_tree.insert(node5, node3, False)
        self.binary_tree.insert(node19, node18, False)
    
    def testKnownCases(self):
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 16))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 9))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 18))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 3))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 14))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 19))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 1))
        self.assertTrue(binary_tree_service.print_ancestors(self.binary_tree, 5))
        self.assertFalse(binary_tree_service.print_ancestors(self.binary_tree, 2))
        self.assertFalse(binary_tree_service.print_ancestors(self.binary_tree, 20))
        self.assertFalse(binary_tree_service.print_ancestors(self.binary_tree, -1))

    def testErrorCases(self):
        self.assertFalse(binary_tree_service.print_ancestors(None, 16))  
        
if __name__ == '__main__':
    unittest.main()
