class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


"""
    2 pointers, iterative
    
    create 2 pointers, l, r, starting at 0 and length of nums
    middle pointer will be dynamic
    
    create a loop, l < r:
        middle = l + r // 2
        
        check for 3 conditions:
            1. if nums[mid] == target: we can just return middle
            2. if nums[mid] < target, it means target is on the right side of nums then we move the l pointer to mid + 1
            3. if nums [mid] > target, it means target is on the left side of nums, so move r pointer to mid - 1
            
    return - 1 if it yields no results up in the loop

"""
