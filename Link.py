#!/usr/bin/env python

class Link(object) :
	
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node
	
	# provide a method to get the value of the link
	def get_value(self):
		return self.value
	
	# provide a method to get the next link
	def get_next(self):
		return self.next_node
	
	# provide a method to set the next link
	def set_next(self, next_node):
		self.next_node = next_node