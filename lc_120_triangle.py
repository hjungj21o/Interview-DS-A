class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]


"""
    bottom-up approach - modify the original triangle
    
    start iterating through the triangle from the 2nd bottom(reversed(range(len(triangle) - 1))) row
        iterate through the elements in that "row", up to i
            the element at that given position should be added with the min of the numbers below
    
    return triangle[0][0] because it will have gotten the most min element

"""
