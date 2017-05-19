#!/usr/bin/env python

from Link import Link

class SimplyLinkedList(object) :
	
	def __init__(self, head=None):
		self.head = head
		
	# get the head link
	def get_head(self):
		return self.head
		
	# insert elements at the front of the list
	def add_first(self, data):
		new_node = Link(data)
		new_node.set_next(self.head)
		self.head = new_node
	
	# calculate the size of the linked list
	def size(self):
		currentLink = self.head
		counter = 0
		while currentLink:
			counter += 1
			currentLink = currentLink.get_next()
		return counter	

	# remove some data from the linked list
	def remove(self, data):
		# get the current link
		current = self.head
		# get the previous link
		previous = None
		# save whether the falue has been found
		found = False
		
		# while the link is not None and the value has not been found
		while current and found is False:
			# if data is found update boolean
			if current.get_value() == data:
				found = True
			# else move on to the next link
			else:
				previous = current
				current = current.get_next()
		
		# if the current link is None the data has not been found
		if current is None:
			raise ValueError("Data not in list")
		
		# replace the current item with the item after it
		# removing it hence from your list
		previous.set_next(current.get_next())
	
	def kth_to_last_element(self, head, k):
		# if the index provided is higher than the size of the array
		# alert the user
		if k > self.size : raise ValueError("Index not in list")
		
		# when you reach the end of the list return
		if head is None: return 0
		
		# update the index of the current link in the list
		index = self.kth_to_last_element(head.get_next(), k) + 1
		
		# if the index is the same as the one we are searching for
		# return the index and print the value
		if index == k :
			print head.value
		
		return index