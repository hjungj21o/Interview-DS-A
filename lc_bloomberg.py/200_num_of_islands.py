# Given an m x n 2d grid map of '1's(land) and '0's(water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


"""
    create a count var that we're going to increment + return at the end
    
    iterate through the grid and its subarray (nested loop)
        if grid[i][j] == "1" (string)
            increment the count
            call dfs on the grid - grid, i, j as args
    
    return count
            
    
    helper dfs:
        if i or j are out of bounds or grid[i][j] is 0, then return out
        
        flip grid[i][j] to 0
        call dfs on up, down, left, right of current i and j

"""

