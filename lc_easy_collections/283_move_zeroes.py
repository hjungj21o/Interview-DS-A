class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zp], nums[i] = nums[i], nums[zp]
                zp += 1


"""
two pointers
one will move no matter what, one will move after a swap

declare a var, that will move only when it's hit a zero
create a loop that iterates through all eles in input list
    if the pointer that moves no matter what hits an int other than zero, swap, move the zp over

return input
"""
