#!/usr/bin/env python

from string import ascii_lowercase

def is_permutation(string1, string2) :
    """Determines if two strings are permutations of each other.
    
    Args:
        string1: the first string to compare
        string2: the second string to compare
        
    Returns:
        True if the two strings are permutations of each other, otherwise false
    """
    if string1 is None or string2 is None:
        return False
    
    string1_dict = string_to_dict(string1)
    string2_dict = string_to_dict(string2)
    
    return string1_dict == string2_dict

def is_permutation_english(string1, string2) : 
    if string1 is None or string2 is None:
        return False
    
    string1_dict = string_to_dict_english(string1)
    string2_dict = string_to_dict_english(string2)
    
    if string1_dict == {} or string2_dict == {} :
        return False
    
    return string1_dict == string2_dict
    
def string_to_dict(input_string) :
    lower_case_string = input_string.lower()
    
    # create a dictionary where you map each character with a counter of
    # how many instances of a character exist
    dictionary = {}
    
    for character in lower_case_string:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    return dictionary

def string_to_dict_english(input_string):
    lower_case_string = input_string.lower()    
    
    dictionary = {}
    
    for alphabet in ascii_lowercase:
        dictionary[alphabet] = 0
    
    for character in lower_case_string:
        if character in dictionary:        
            dictionary[character] = dictionary.get(character) + 1 
        else:       
            return {}
    
    return dictionary

def main() :
    string1 = input('Please insert the first string: ')
    string2 = input('What would you like to compare the first string with: ') 

    print(is_permutation(string1, string2))
    print(is_permutation_english(string1, string2))
    
if __name__ == "__main__":
    main()
