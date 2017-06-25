'''
Created on 23 June 2017

@author: Eva
'''

def count_islands_iter(rowMax, colMax, tiles):
    row = col = 0
    while row < rowMax:
        if tiles[row][col] == False or tiles[row][col]:
            if col + 1 < colMax: 
                col += 1
            else:
                col = 0
                row += 1
            continue
        
        
def count_islands_rec(rowMax, colMax, tiles):
    counter = 0
    visited = [None] * rowMax
    for i in range(0, rowMax):
        visited[i] = [False] * colMax
    
    for i in range(0, rowMax):
        for j in range(0, colMax):
            if visited[i][j]:
                continue
            elif not tiles[i][j]:
                visited[i][j] = True
                continue
            counter += 1
            flood_fill(rowMax, colMax, i, j, tiles, visited)
    return counter
    
                
def flood_fill(rowMax, colMax, rowCur, colCur, tiles, visited):
    if not tiles[rowCur][colCur] or visited[rowCur][colCur]: return
    visited[rowCur][colCur] = True
    if colCur + 1 < colMax: flood_fill(rowMax, colMax, rowCur, colCur + 1, tiles, visited)
    if colCur - 1 > -1: flood_fill(rowMax, colMax, rowCur, colCur - 1, tiles, visited)
    if rowCur + 1 < rowMax: flood_fill(rowMax, colMax, rowCur + 1, colCur, tiles, visited)
    if rowCur - 1 > -1: flood_fill(rowMax, colMax, rowCur - 1, colCur, tiles, visited)