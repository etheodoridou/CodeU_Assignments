#!/usr/bin/env python

class Link(object) :
    
        def __init__(self, value, next_link=None):
            self.__value = value
            self.__next_link = next_link

        def get_value(self):
            return self.__value

        def get_next(self):
            return self.__next_link

        def set_next(self, next_link):
            self.__next_link = next_link


class LinkedList(object) :
    
    def __init__(self, head=None):
        self.head = head
        
    def get_head(self):
        return self.head
        
    # insert elements at the front of the list
    def add_first(self, data):
        new_link = Link(data)
        new_link.set_next(self.head)
        self.head = new_link
    
    def size(self):
        currentLink = self.head
        counter = 0
        while currentLink:
            counter += 1
            currentLink = currentLink.get_next()
        return counter    

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.get_value() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if not found:
            raise ValueError("Data not in list")

        previous.set_next(current.get_next())
    
    
def kth_to_last_element(head, k):
    """Finds the kth to last element in a simply linked list
    
    Args:
        head: a Link instance, the head of the linked list 
        k: an integer, the kth to last position of the Link we are looking for
        
    Returns:
        If the kth to last element given exists, return the value of the Link found. Otherwise, 
        raise a ValueError
    """
    if k < 0: raise ValueError("The index " + str(k) + " does not exist in this linked list.")
    
    ptr_to_last = ptr_temp = head
    
    for i in range(0,k+1):
        if ptr_temp is None: raise ValueError("The index " + str(i) + "does not exist in this linked list.")
        ptr_temp = ptr_temp.get_next()
        
    while ptr_temp is not None:
        ptr_temp = ptr_temp.get_next()
        ptr_to_last = ptr_to_last.get_next()
        
    return ptr_to_last.get_value()



