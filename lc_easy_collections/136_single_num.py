class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return len(nums)

        # dic = collections.Counter(nums)
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        for k, v in dic.items():
            if v == 1:
                return k


"""
option 1: using a set?
option 2: sorting?
option 3: two pointers?

"""
