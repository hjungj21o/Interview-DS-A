"""
    Valid Triangle Num

    Given an array of nonneg numbers
    return count num of triplets that can make a triangle

    valid triangle == a + b > c, a + c > b, b + c > a
    a + b > c where c > b > a
    [2, 2, 3, 4]
    l    r   i
    count = 3
    [2, 3, 4], [2, 3, 4], [2, 2, 3]

    [2, 5, 10]
    count = 0


    sort the argument

    l = 0
    r = i - 1
    i is dynamic (iteration)

    for i in range(len(input) - 1, 2, - 1):
        while l < r:
            if i < l + r:
                count += r - l
                r -= 1
            else:
                l += 1
    return count

    time: O(N log N) where N size input
    space: O(1) 

"""

def valid_triangle(nums):
    nums.sort()  # [2, 2, 3, 4]

    count = 0
    for i in range(len(nums) - 1, 1, -1): #3
        l, r = 0, i - 1 #0, 1

        while l < r:
            if nums[i] < nums[l] + nums[r]: #3 < 2 + 2
                count += r - l #3
                r -= 1 #0
            else:
                l += 1 #1
    
    return count # 3


print(valid_triangle([2, 2, 3, 4]))
