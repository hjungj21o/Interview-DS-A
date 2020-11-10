class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


"""
    almost like binary search
    
    get l and r pointers (0 and len of nums - 1)
    
    while l <= r:
        get mid (l + r // 2)
        
        if nums[mid] == target, return mid
        elif the array is left rotated (smaller nums are at the right) - nums[mid] >= nums[l]
            if target is in between l and mid (it's in proper ascending order):
                move r to mid - 1
            else (target is sandwiched in rotated portion):
                move l to mid + 1
        else (the array is right rotated (larger nums at the left)):
            if target is between mid and r (it's in proper ascending order):
                l = mid + 1
            else (target is sandwiched in rotated):
                r = mid - 1
    if nothing is found, return -1

"""
