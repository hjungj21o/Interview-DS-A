class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set()

        for num in nums:
            if num in sets:
                return True
            else:
                sets.add(num)

        return False

        # return len(set(nums)) != len(nums)


"""
    Using set to find duplicates
    create a set
    iterate through nums
        if not in set, add it
        if it is in sets (which means there's a duplicate), return true
    return false at the end
"""
