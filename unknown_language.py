'''
Created on 07 July 2017

@author: Eva
'''

def get_alphabet_adj(dictionary):
    alphabet = []
    
    for j in range(len(dictionary) - 1):
        word_cur = dictionary[j]
        word_next = dictionary[j+1]
        
        alphabet = __check_adjacent_words(word_cur, word_next, alphabet)
        print(alphabet)
    
    return alphabet

def __check_adjacent_words(word_cur, word_next, alphabet):
    for i in range(len(word_cur)):
        first_letter = word_cur[i]
        second_letter = word_next[i]
        if first_letter == second_letter:
            continue
        if first_letter in alphabet and second_letter in alphabet:
            if alphabet.index(first_letter) >= alphabet.index(second_letter):
                alphabet.remove(second_letter)
                alphabet.insert(alphabet.index(first_letter) + 1, second_letter)
        elif first_letter in alphabet and second_letter not in alphabet:
            alphabet.insert(alphabet.index(first_letter) + 1, second_letter)
        elif second_letter in alphabet and first_letter not in alphabet:
            alphabet.insert(alphabet.index(second_letter), first_letter)
        else:
            alphabet.append(first_letter)
            alphabet.append(second_letter)
        break
    return alphabet

def get_alphabet_top_sort(dictionary):
                    