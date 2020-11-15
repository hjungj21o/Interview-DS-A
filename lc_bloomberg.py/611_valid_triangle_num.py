# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2, 2, 3, 4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2, 3, 4 (using the first 2)
# 2, 3, 4 (using the second 2)
# 2, 2, 3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of[0, 1000].


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        counter = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1

            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    counter += r - l
                    r -= 1
                else:
                    l += 1

        return counter


"""
time: O(n^2) where N is size of list
space: O(logN) because sorting takes logN
Sliding window, 3-sum sort of problem

Sort first, because to make a valid triangle, the condition is a + b > c, where a <= b <= c

Pseudo:
    create a counter
    sort the list
    
    iterate backwards, up until the 2nd ele (because we're going to have 2 dynamic pointers pointers that come before i)
    
    l, r = 0, i - 1
    
    while l < r:
        if nums[i] < nums[l] + nums[r]:
            it's a vlid triangle.
            increment counter by r - l ==> all the numbers in between r and l are also valid triangles
            decrement r by 1
        else:
            it's not a valid triangle, so increment l by one
            
    return counter

"""
