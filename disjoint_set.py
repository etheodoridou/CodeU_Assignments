'''
Created on 23 June 2017

@author: Eva
'''

class DisjointSet:
    
    def __init__(self, size):
        self.parent = [None] * size
        self.rank = [0] * size
        self.create_set(size)
    
    def create_set(self, size):
        for i in range(0, size):
            self.parent[i] = i
    
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
            self.parent[root_elem2] = root_elem1
        elif self.rank[root_elem2] > self.rank[root_elem1]:
            self.parent[root_elem1] = root_elem2
        else:
            self.parent[root_elem1] = root_elem2
            self.rank[root_elem2] += 1
            
    def find(self, elem):
        if self.parent[elem] != elem:
            # path compression heuristic
            self.parent[elem] = self.find(self.parent[elem])
            
        return self.parent[elem]