class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        result = []

        beg_col = 0
        beg_row = 0
        end_col = len(matrix[0]) - 1
        end_row = len(matrix) - 1

        while beg_col <= end_col and beg_row <= end_row:
            for num in range(beg_col, end_col + 1):
                result.append(matrix[beg_row][num])
            beg_row += 1
            for num in range(beg_row, end_row + 1):
                result.append(matrix[num][end_col])
            end_col -= 1

            if beg_row <= end_row:
                for num in reversed(range(beg_col, end_col + 1)):
                    result.append(matrix[end_row][num])
            end_row -= 1

            if beg_col <= end_col:
                for num in reversed(range(beg_row, end_row + 1)):
                    result.append(matrix[num][beg_col])
            beg_col += 1

        return result


"""
    Keep track of 4 pointers - beginning of row & col, end of col & row
    right, down, left, up
    create res var
    
    go through the matrix using 4 pointers - while begcol <= endcol and begrow <= endrow:
        go right first
            for loop, beginning at begcol and ending at endrow:
                append matrix[begrow][num]
            increment begrow + 1 to ensure we don't go up to 0 next time
        go down:
            for loop, beginning at begrow and ending at endrow
                append matrix[num][endcol]
            decrement endrow to ensure we don't go up to 0 next time
            
        go left
            for loop reversed on endcol begcol:
                append[endrow][num]
            decrement endrow
        go up
            for loop reversed endrow begrow:
                append[num][begcol]
            increment begcol 
        
"""
