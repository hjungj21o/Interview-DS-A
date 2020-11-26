class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4

                    if i > 0 and grid[i - 1][j]:
                        res -= 2
                    if j > 0 and grid[i][j - 1]:
                        res -= 2

                # res += count

        return res


"""
    determine what is land and what is water
    
    iterate through the matrix:
        if curr position is 1
            res += 4
            
            since we're traversing grid from left -> right, top -> bottom, we only need to check if left and up cells are land
            
            if i > 0 and grid[i - 1][j]:
                res -= 2
"""
