'''
Created on 23 June 2017

@author: Eva
'''

class DisjointSet:
    
    def __init__(self, size):
        self.__parent = [None] * size
        self.__size = [1] * size
        self.create_set(size)
        
    def get_parent_array(self):
        return self.__parent
    
    def create_set(self, size):
        for i in range(0, size):
            self.__parent[i] = i
    
    def merge(self, elem1, elem2):
        root_elem1 = self.find(elem1)
        root_elem2 = self.find(elem2)
        if root_elem1 == root_elem2: return
        
        # union by rank heuristic
        if self.__size[root_elem1] > self.__size[root_elem2]:
            self.__parent[root_elem2] = root_elem1
            self.__size[root_elem1] += self.__size[root_elem2]
        else:
            self.__parent[root_elem1] = root_elem2
            self.__size[root_elem2] += self.__size[root_elem1]
        
    def find(self, elem):
        if self.__parent[elem] != elem:
            self.find(self.__parent[elem])
            
        return self.__parent[elem]