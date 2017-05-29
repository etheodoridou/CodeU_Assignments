'''
Created on 22 May 2017

@author: Eva
'''

class BinaryTree:
    
    def __init__(self, root=None):
        self.root = root
    
    def get_root(self):
        return self.root
    
    def insert(self, new_node, parent, to_left):
        
        if self.root is None:
            self.root = new_node
            
        elif to_left:
            if parent.get_left_node() is None: 
                parent.set_left_node(new_node)
            else:
                new_node.set_left_node(parent.get_left_node())
                parent.set_left_node(new_node)
                
        else:
            if parent.get_right_node() is None: 
                parent.set_right_node(new_node)
            else:
                new_node.set_right_node(parent.get_right_node())
                parent.set_right_node(new_node)
        
    
class TreeNode:
    
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        
    def get_value(self):
        return self.value
    
    def get_left_node(self):
        return self.left_node
    
    def set_left_node(self, left_child):
        self.left_node = left_child
    
    def get_right_node(self):
        return self.right_node
    
    def set_right_node(self, right_child):
        self.right_node = right_child
    