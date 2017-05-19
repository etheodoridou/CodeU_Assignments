#!/usr/bin/env python

from SimplyLinkedList import SimplyLinkedList

def main():
	linked_list = SimplyLinkedList()
	
	linked_list.add_first(0)
	linked_list.add_first(1)
	linked_list.add_first(2)
	linked_list.add_first(3)
	linked_list.add_first(4)
	linked_list.add_first(5)
	linked_list.add_first(6)
	linked_list.add_first(7)
	linked_list.add_first(8)
	
	list_head = linked_list.get_head()
	
	linked_list.kth_to_last_element(list_head, 3)
	
if __name__ == "__main__":
	main()