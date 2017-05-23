#!/usr/bin/env python

"""
Method determines if two strings are permutations of each other

string1, string2: two string variables which will be compared for the purposes of this function

return true if the two strings are permutations of each other, otherwise false
"""
def is_permutation(string1, string2) :
	if string1 is None or string2 is None:
		return False
	
	string1_dict = string_to_dict(string1)
	string2_dict = string_to_dict(string2)
	
	return dicts_are_equal(string1_dict, string2_dict)

def is_permutation_english(string1, string2) : 
    if string1 is None or string2 is None:
        return False
    
    string1_dict = string_to_dict_english(string1)
    string2_dict = string_to_dict_english(string2)
    
    return dicts_are_equal(string1_dict, string2_dict)
	
def string_to_dict(input_string) :
	lower_case_string = input_string.lower()
	
	# create a dictionary where you map each character with a counter of
	# how many instances of a character exist
	dict = {}
	
	for character in lower_case_string:
		if character in dict:
			dict[character] = dict.get(character) + 1
		else:
			dict[character] = 1

	return dict

def string_to_dict_english(input_string):
    lower_case_string = input_string.lower()	
	
	dict = {}
	
	for alphabet in range('a','z'):
		dict[character] = 0
	
	for character in lower_case_string:
		if character in dict:		
			dict[character] = dict.get(character) + 1
    	else:			
            return None
    
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
	string1 = raw_input('Please insert the first string: ')
	print
	string2 = raw_input('What would you like to compare the first string with: ')
	print
	
	print is_permutation(string1, string2)  
