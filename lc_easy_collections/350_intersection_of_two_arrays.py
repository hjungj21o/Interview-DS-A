class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #         dic = {}

        #         for num in nums1:
        #             if num not in dic:
        #                 dic[num] = 1
        #             else:
        #                 dic[num] += 1
        #         result = []
        #         for num in nums2:
        #             if num in dic and dic[num] > 0:
        #                 result.append(num)
        #                 dic[num] -= 1

        #         return result

        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result


"""
    dictionary:
        create a dictionary, iterate through nums1 and count the number of elements in num 1
        iterate through nums2
            if element exists in dic and the count is not 0, append it to result list
        return result
    
    sorted:
        sort both lists
        create a loop to go through both lists
        if list1's val is lower, then move up to next element
        vice versa for list2
        if they are equal, append it to result array and increment both
"""
