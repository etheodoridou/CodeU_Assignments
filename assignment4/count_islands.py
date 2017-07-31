'''
Created on 23 June 2017

@author: Eva
'''

from disjoint_set import DisjointSet

def count_islands_iter(tiles):
    """Counts the number of islands that exist in the given array.
    
    This approach uses a disjoint set to merge the land tiles that
    are adjacent either vertically or horizontally to a given land tile.
    It then counts the roots of trees that represent land tiles to 
    calculate the islands.
        
        Args:
            tiles: a two-dimensional array of boolean values where 
                True represents a location with land and False 
                represents a location with water.
        
        Returns:
            The number of islands found in the array.
    """
    if not is_valid(tiles): 
        raise ValueError("must be non-empty: tiles")
    
    row_max = len(tiles)
    # assume all columns have the same length
    col_max = len(tiles[0])
    
    dis_set = DisjointSet()
    dis_set.create_set(row_max * col_max)
    
    for i in range(row_max):
        for j in range(col_max):
            if not tiles[i][j]: # this is a water tile so it does not belong to an island
                continue
            
            i_range = [i, i, i-1, i+1]
            j_range = [j-1, j+1, j, j]
            for k,l in zip(i_range, j_range):
                if in_bounds(k, row_max) and in_bounds(l, col_max) and tiles[k][l]:
                    dis_set.merge(position(i,j,row_max), position(k, l, row_max))
                    
    visited_roots = set([])
    island_counter = 0
    for i in range(row_max):
        for j in range(col_max):
            root = dis_set.find(position(i,j,row_max))
            if tiles[i][j] == True and root not in visited_roots:
                    island_counter = island_counter + 1
                    visited_roots.add(root)
    
    return island_counter            
    
def count_islands_rec(tiles):
    """Counts the number of islands that exist in the given array.
    
    This approach uses DFS and Flood-Fill.
    
        Args:
            tiles: a two-dimensional array of boolean values where 
                True represents a location with land and False 
                represents a location with water.
        
        Returns:
            The number of islands found in the array.
    """
    if not is_valid(tiles): 
        raise ValueError("must be non-empty: tiles")
    
    row_max = len(tiles)
    # assume all columns have the same length
    col_max = len(tiles[0])
    
    island_counter = 0
    visited = [None] * row_max
    for i in range(row_max):
        visited[i] = [False] * col_max
    
    for i in range(row_max):
        for j in range(col_max):
            if visited[i][j]:
                continue
            if not tiles[i][j]: # this is a water tile so it does not belong to an island
                visited[i][j] = True
            else:
                island_counter += 1
                flood_fill(row_max, col_max, i, j, tiles, visited)
    return island_counter
    
                
def flood_fill(row_max, col_max, row_cur, col_cur, tiles, visited):
    """Helper function to count_islands_rec.
        
        Args:
            row_max: an integer, the number of rows in the array
            col_max: an integer, the number of columns in the array
            row_cur: an integer, the current row investigated
            col_cur: an integer, the current column investigated
            tiles: a two-dimensional array of boolean values
            visited: a two-dimensional array used to keep track
                     of which tiles have been visited
        
        Returns:
            void
    """
    if not tiles[row_cur][col_cur] or visited[row_cur][col_cur]: return
    
    visited[row_cur][col_cur] = True
    
    row_range = [row_cur, row_cur, row_cur-1, row_cur+1]
    col_range = [col_cur-1, col_cur+1, col_cur, col_cur]
    for i,j in zip(row_range, col_range):
        if in_bounds(i, row_max) and in_bounds(j, col_max): 
            flood_fill(row_max, col_max, i, j, tiles, visited)
            
def in_bounds(x, x_bound):
    return x >= 0 and x < x_bound

def is_valid(array):
    if array and array[0]:
        return True
    else:
        return False

def position(i, j, row_max):
    return i * row_max + j