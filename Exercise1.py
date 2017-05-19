#!/usr/bin/env python


def is_permutation(string1, string2) :
	# check if any of the strings is None
	if string1 is None or string2 is None:
		return False
	# change strings inputted to dictionaries
	string1_dict = string_to_dict(string1)
	string2_dict = string_to_dict(string2)
	
	# check if the two dictionaries are equal
	result = dicts_are_equal(string1_dict, string2_dict)
	
	return result
	
def string_to_dict(input_string) :
	# make sure all characters are lower case
	lower_case_string = input_string.lower()
	
	# create a dictionary where you map each character with a counter of
	# how many instances of a character exist
	# if the strings can only include characters from the English alphabet:
	# initialise the dictionary at this stage with all the letters of the alphabet
	# and a starting counter value of 0
	dict = {}
	
	# add the characters to the dictionary
	for character in lower_case_string:
		if character in dict:
			value = dict[character]
			dict[character] = value + 1
		else:
			dict[character] = 1
			
	# for the case where only the English alphabet is allowed
	# modify the for-loop
	# 		
	# for character in lower_case_string:
	# 	if character in dict:
	# 		value = dict[character]
	# 		dict[character] = value + 1
	# 	else:
	# 		return None
	
	return dict

def dicts_are_equal(dict1, dict2) :
	
	# check that for each key in one dictionary,
	# the same key exists in the other dictionary
	# and the counter values are equal
	for key in dict1:
		if key in dict2 and dict2[key] == dict1[key]:
			continue
		else:
			return False
	return True

def main() :
	string1 = raw_input('Please insert the first string.')
	print
	string2 = raw_input('What would you like to compare the first string with?')
	print
	
	print is_permutation(string1, string2)  
