'''
Created on 22 May 2017

@author: Eva
'''
from binary_tree import BinaryTree

def print_ancestors(tree, key):
    """Prints the ancestors of a given node.
    
    Args:
        tree: a BinaryTree object that holds all the nodes
        key: the value of the node
        
    Returns:
        True if the key exists in the binary tree, otherwise false
    """
    if tree is None:
        return False
    
    if tree.get_root().get_value() == key:
        return True
    
    if tree.get_root().get_left_node() is not None:
        left_tree = BinaryTree(tree.get_root().get_left_node())
        if print_ancestors(left_tree, key):
            print(tree.get_root().get_value())
            return True
            
    if tree.get_root().get_right_node() is not None:
        right_tree = BinaryTree(tree.get_root().get_right_node())
        if print_ancestors(right_tree, key):
            print(tree.get_root().get_value())
            return True
    
    return False

def find_lowest_common_ancestor(root_node, node1, node2):
    """Determines the lowest common ancestor of two nodes.
    
    Args:
        root_node: a TreeNode object that is the root of the tree
        node1: the value of the first node
        node2: the value of the second node
        
    Returns:
        The node representing the lowest common ancestor of the two nodes

    NB. Assume both nodes exist in the binary search tree
    """
    if root_node is None:
        return None
    
    if root_node.get_value() == node1 or root_node.get_value() == node2:
        return root_node
    
    left_node = find_lowest_common_ancestor(root_node.get_left_node(), node1, node2)
    right_node = find_lowest_common_ancestor(root_node.get_right_node(), node1, node2)
    
    if left_node and right_node:
        return root_node
    
    return left_node if left_node is not None else right_node
    
