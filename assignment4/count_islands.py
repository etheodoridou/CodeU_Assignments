'''
Created on 23 June 2017

@author: Eva
'''

from disjoint_set import DisjointSet

def count_islands_iter(rowMax, colMax, tiles):
    """Counts the number of islands that exist in the given array.
    
    This approach uses a disjoint set to merge the land tiles that
    are adjacent either vertically or horizontally to a given land tile.
    It then counts the roots of trees that represent land tiles to 
    calculate the islands.
    
    NB. True -> Land tile
        False -> Water tile
    NB2. Assume rowMax and colMax are not out of bounds of the array
        
        Args:
            rowMax: an integer, the number of rows in the array
            colMax: an integer, the number of columns in the array
            tiles: a two-dimensional array of boolean values
        
        Returns:
            The number of islands found in the array.
    """
    if tiles is None or len(tiles) == 0 or len(tiles[0]) == 0: 
        raise ValueError("Please insert a non-empty array of tiles.")
    
    dis_set = DisjointSet(rowMax * colMax)
    
    for i in range(rowMax):
        for j in range(colMax):
            if tiles[i][j] == False: continue
            
            # right
            if in_bound(j+1, colMax) and tiles[i][j+1] == True:
                dis_set.merge(i*rowMax+j, i*rowMax+j+1)
            # left
            if in_bound(j-1, colMax) and tiles[i][j-1] == True:
                dis_set.merge(i*rowMax+j, i*rowMax+j-1)
            # top
            if in_bound(i+1, rowMax) and tiles[i+1][j]:
                dis_set.merge(i*rowMax+j, (i+1)*rowMax+j)
            # bottom
            if in_bound(i-1, rowMax) and tiles[i-1][j]:
                dis_set.merge(i*rowMax+j, (i-1)*rowMax+j)
    
    visited_roots = []
    island_counter = 0
    for i in range(rowMax):
        for j in range(colMax):
            if tiles[i][j] == True and dis_set.find(i*rowMax+j) not in visited_roots:
                    root = dis_set.find(i*rowMax+j)
                    island_counter = island_counter + 1
                    visited_roots.append(root)
    
    return island_counter            
    
def count_islands_rec(rowMax, colMax, tiles):
    """Counts the number of islands that exist in the given array.
    
    This approach uses DFS and Flood-Fill.
    
    NB. True -> Land tile
        False -> Water tile
    NB2. Assume rowMax and colMax are not out of bounds of the array
    
        Args:
            rowMax: an integer, the number of rows in the array
            colMax: an integer, the number of columns in the array
            tiles: a two-dimensional array of boolean values
        
        Returns:
            The number of islands found in the array.
    """
    if tiles is None or len(tiles) == 0 or len(tiles[0]) == 0: 
        raise ValueError("Please insert a non-empty array of tiles.")
    
    counter = 0
    visited = [None] * rowMax
    for i in range(rowMax):
        visited[i] = [False] * colMax
    
    for i in range(rowMax):
        for j in range(colMax):
            if visited[i][j]:
                continue
            elif not tiles[i][j]:
                visited[i][j] = True
                continue
            counter += 1
            flood_fill(rowMax, colMax, i, j, tiles, visited)
    return counter
    
                
def flood_fill(rowMax, colMax, rowCur, colCur, tiles, visited):
    """Helper function to count_islands_rec.
        
        Args:
            rowMax: an integer, the number of rows in the array
            colMax: an integer, the number of columns in the array
            rowCur: an integer, the current row investigated
            colCur: an integer, the current column investigated
            tiles: a two-dimensional array of boolean values
            visited: a two-dimensional array used to keep track
                     of which tiles have been visited
        
        Returns:
            void
    """
    if not tiles[rowCur][colCur] or visited[rowCur][colCur]: return
    
    visited[rowCur][colCur] = True
    
    # right
    if in_bound(colCur + 1, colMax): flood_fill(rowMax, colMax, rowCur, colCur + 1, tiles, visited)
    # left
    if in_bound(colCur - 1, colMax): flood_fill(rowMax, colMax, rowCur, colCur - 1, tiles, visited)
    # top
    if in_bound(rowCur + 1, rowMax): flood_fill(rowMax, colMax, rowCur + 1, colCur, tiles, visited)
    # bottom
    if in_bound(rowCur - 1, rowMax): flood_fill(rowMax, colMax, rowCur - 1, colCur, tiles, visited)

def in_bound(x, x_bound):
    return x >= 0 and x < x_bound
