class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = n + m - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        if j >= 0:
            nums1[0:k+1] = nums2[0:j+1]


"""
    index to change = m + n - 1
    
    while loop until n == 0 or m == 0
        if nums2[n - 1] > nums1[m - 1]:
            replace nums1[m + n - 1] to nums2[n - 1], decrement m
        else:
            replace nums1[m + n - 1] to nums1[m -1], decrement n
            
        if there's n left over, replace nums1[0:m+n-1] with nums2[0:n+1]
    
"""
