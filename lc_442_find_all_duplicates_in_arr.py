class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #create result arrlist
        result = []

        #iterate through input
        for i in nums:
            if nums[abs(i) - 1] < 0:
                result.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1

        return result


"""
    suboptimal: use a set to determine if there are duplicates
        O(n) space, O(n) time
    
    sorting and two pointer: O(1) space, O(n log(n)) time
    
    [-4,-3,-2,-7,8,2,-3,-1]
                         
    curr_num = 2
    position = 
    curr_idx = 2
    [2]
    
    if the number that we're indexing into is already a negative int, 
    then append the current element that we're curently at in array's iteration to the result array
    
    Pseudocode:
    create an arrlist that will house the output
        use the current element as the index to turn that number into a negative int (don't forget to - 1 to account for indexing)
    
    iterate through the input arrlist
        if the number that we're indexing into has already been turned into a negative, then we know there's a duplicate, so add it to the result arrlist
        
    return the resutl arrlist

"""
