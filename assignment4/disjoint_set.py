'''
Created on 23 June 2017

@author: Eva
'''

class DisjointSet:
    
    def __init__(self):
        self.parent = []
        self.rank = []
    
    def create_set(self, size):
        self.parent = [None] * size
        for i in range(size):
            self.parent[i] = i
        self.rank = [0] * size
    
    def merge(self, elem1, elem2):
        """Merges two elements of the disjoint set and the sets they are
        contained within.
            
            Args:
                elem1: an integer, the first element to be merged
                elem2: an integer, the second element to be merged
            
            Returns:
                void
        """
        root_elem1 = self.find(elem1)
        root_elem2 = self.find(elem2)
        if root_elem1 == root_elem2: return
        
        # union by rank heuristic
        if self.rank[root_elem1] > self.rank[root_elem2]:
            self.parent[elem2] = root_elem1
        elif self.rank[root_elem2] > self.rank[root_elem1]:
            self.parent[elem1] = root_elem2
        else:
            self.parent[elem1] = root_elem2
            self.rank[root_elem2] += 1
            
    def find(self, elem):
        # path compression heuristic (iterative)
        i = elem
        while i != self.parent[i]: # find root
            i = self.parent[i]
        
        if i != elem: # compress path
            temp = self.parent[elem]
            while i != temp:
                self.parent[elem] = i
                elem = temp
                temp = self.parent[temp]
        return i