class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(i, j, board, word):
                    return True

        return False

    def backtrack(self, i, j, grid, word):
        if len(word) == 0:
            return True

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != word[0]:
            return False

        grid[i][j] = "x"

        if self.backtrack(i + 1, j, grid, word[1:]):
            return True
        if self.backtrack(i - 1, j, grid, word[1:]):
            return True
        if self.backtrack(i, j + 1, grid, word[1:]):
            return True
        if self.backtrack(i, j - 1, grid, word[1:]):
            return True

        grid[i][j] = word[0]
        # return False


"""
    Backtracking problem (feels like DFS)
    
    helper function: takes in board, i, j, and word as args
        base case: if length of word == 0 (meaning we've found the word)
            return True
        base case 2: if i, j are out of bounds or board[i][j] != word[0]:
            return False
            
        mark current location with "x" so when we backtrack we don't go back to this position
        
        backtrack on up, down, left, right (i +/- 1, j +/- 1) and word[1:]:
        if they come back True, return True
        
        bring the current position back to word[0]
        
    main function:
        iterate through row and col (i , j) of board:
            if backtrack function returns True, then return True
            
        return False at the end
    
"""
