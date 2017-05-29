'''
Created on 22 May 2017

@author: Eva
'''

from binary_tree import BinaryTree, TreeNode
import binary_tree_service
import unittest

class Question2Test(unittest.TestCase):

    def setUp(self):
        self.root_node = TreeNode(16)
        self.node9 = TreeNode(9)
        node18 = TreeNode(18)
        node3 = TreeNode(3)
        node14 = TreeNode(14)
        node19 = TreeNode(19)
        node1 = TreeNode(1)
        node5 = TreeNode(5)
        self.binary_tree = BinaryTree(self.root_node)
        self.binary_tree.insert(self.node9, self.root_node, True)
        self.binary_tree.insert(node18, self.root_node, False)
        self.binary_tree.insert(node3, self.node9, True)
        self.binary_tree.insert(node14, self.node9, False)
        self.binary_tree.insert(node1, node3, True)
        self.binary_tree.insert(node5, node3, False)
        self.binary_tree.insert(node19, node18, False)
    
    def testKnownCases(self):
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(self.root_node, 5, 14), self.node9)
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(self.root_node, 5, 16), self.root_node)

    def testErrorCases(self):
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(None, 16, 16), None)
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(self.root_node, 16, 16), self.root_node)  
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(self.root_node, 7, 16), self.root_node)
        self.assertEqual(binary_tree_service.find_lowest_common_ancestor(self.root_node, 7, 10), None)
        
if __name__ == '__main__':
    unittest.main()