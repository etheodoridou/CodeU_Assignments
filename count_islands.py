'''
Created on 23 June 2017

@author: Eva
'''

from disjoint_set import DisjointSet

def count_islands_iter(rowMax, colMax, tiles):
    if tiles is None or len(tiles) == 0: raise ValueError("Please insert a non-empty array of tiles.")
    
    dis_set = DisjointSet(rowMax * colMax)
    
    for i in range(0, rowMax):
        for j in range(0, colMax):
            if tiles[i][j] == False: continue
            if in_bound(j+1, colMax) and tiles[i][j+1] == True:
                dis_set.merge(i*rowMax+j, i*rowMax+j+1)
            if in_bound(j-1, colMax) and tiles[i][j-1] == True:
                dis_set.merge(i*rowMax+j, i*rowMax+j-1)
            if in_bound(i+1, rowMax) and tiles[i+1][j]:
                dis_set.merge(i*rowMax+j, (i+1)*rowMax+j)
            if in_bound(i-1, rowMax) and tiles[i-1][j]:
                dis_set.merge(i*rowMax+j, (i-1)*rowMax+j)
    
    visited_roots = []
    island_counter = 0
    for i in range(0, rowMax):
        for j in range(0, colMax):
            if tiles[i][j] == True and dis_set.find(i*rowMax+j) not in visited_roots:
                    root = dis_set.find(i*rowMax+j)
                    island_counter = island_counter + 1
                    visited_roots.append(root)
    
    return island_counter            
    
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
    
    if in_bound(colCur + 1, colMax): flood_fill(rowMax, colMax, rowCur, colCur + 1, tiles, visited)
    if in_bound(colCur - 1, colMax): flood_fill(rowMax, colMax, rowCur, colCur - 1, tiles, visited)
    if in_bound(rowCur + 1, rowMax): flood_fill(rowMax, colMax, rowCur + 1, colCur, tiles, visited)
    if in_bound(rowCur - 1, rowMax): flood_fill(rowMax, colMax, rowCur - 1, colCur, tiles, visited)

def in_bound(x, x_bound):
    return x >= 0 and x < x_bound