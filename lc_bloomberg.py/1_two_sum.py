# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6
# Output: [0, 1]


"""
    naive: nested for loop, checking every combination of numbers to see if pair meets target
    O(n^2) time, may time out

    optimal: use dictionary
    create an empty dict

    enumerate through nums
        check condition if target - num is a key already. if it is:
            return dict[target - num] and current index
        always initialize dict[target] = i


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dict
        dict = {}

        #enumerate through nums
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
        