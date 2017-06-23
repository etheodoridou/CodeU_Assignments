'''
Created on 9 June 2017

@author: Eva
'''
from queue import Queue

class WordSearch:
    
    def __init__(self):
        return
        
    def words_found_in_grid(self, rowNo, columnNo, grid, dictionary):
        """Uses bfs to find valid words from a grid according to a given dictionary 
        
            Args:
                rowNo: number of rows in the grid
                columnNo: number of columns in the grid
                grid: two-dimensional array of characters
                dictionary: a dictionary object that holds the valid words and prefices
            
            Returns:
                A list of words that were found on the grid
        """
        self.__pathsTaken = []
        self.__foundWords = []
        self.__words_to_search = Queue()
        row = 0
        column = 0
        
        self.__words_to_search.put([grid[column][row], column, row, []])
        
        while not self.__words_to_search.empty():
            currentArray = self.__words_to_search.get()
            currentWord = currentArray[0]
            column = currentArray[1]
            row = currentArray[2]
            positions = currentArray[3]
            
            if dictionary.isPrefix(currentWord):
                tempPositions = positions.copy()
                tempPositions.append([column, row])
                if tempPositions in self.__pathsTaken: continue
                
                if dictionary.isWord(currentWord) and currentWord not in self.__foundWords:
                    self.__foundWords.append(currentWord)
                    newPositions = positions.copy()
                    newPositions.append([column, row])
                    self.__pathsTaken.append(newPositions)
            
                if row+1 < rowNo and [column, row+1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column, row+1, positions, grid, dictionary)
                    
                if row-1 > -1 and [column, row-1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column, row-1, positions, grid, dictionary)
                    
                if column+1 < columnNo and [column+1, row] not in positions:
                    self.addWordToSearch(currentWord, column, row, column+1, row, positions, grid, dictionary)
                
                if column-1 > -1 and [column-1, row] not in positions:
                    self.addWordToSearch(currentWord, column, row, column-1, row, positions, grid, dictionary)
                
                if column-1 > -1 and row-1 > -1 and [column-1, row-1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column-1, row-1, positions, grid, dictionary)
                
                if column+1 < columnNo and row+1 < rowNo and [column+1, row+1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column+1, row+1, positions, grid, dictionary)
                
                if column-1 > -1 and row+1 < rowNo and [column-1, row+1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column-1, row+1, positions, grid, dictionary)
            
                if column+1 < columnNo and row-1 > -1 and [column+1, row-1] not in positions:
                    self.addWordToSearch(currentWord, column, row, column+1, row-1, positions, grid, dictionary)
            
            else:
                previousPathTaken = positions.copy()
                previousPathTaken.append([column, row])
                self.__pathsTaken.append(previousPathTaken)
                
                if not self.__words_to_search.empty(): continue
                
                rowAddCopy = previousPathTaken.copy()
                rowAddCopy.append([column, row+1])
                columnAddCopy = previousPathTaken.copy()
                columnAddCopy.append([column+1, 0])
                
                if row+1 < rowNo and rowAddCopy not in self.__pathsTaken:
                    self.__words_to_search.put([grid[column][row+1], column, row+1, []])
                elif column+1 < columnNo and columnAddCopy not in self.__pathsTaken:
                    self.__words_to_search.put([grid[column+1][0], column+1, 0, []])
                else: break
                    
        return self.__foundWords
                
    def addWordToSearch(self, currentWord, initColumn, initRow, nextColumn, nextRow, positions, grid, dictionary):
        newWord = currentWord + grid[nextColumn][nextRow]
        if newWord in self.__foundWords: return
        if dictionary.isPrefix(newWord):
            newPositions = positions.copy()
            newPositions.append([initColumn, initRow])
            self.__words_to_search.put([newWord, nextColumn, nextRow, newPositions])

