# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlaps, merge them into[1, 6].
# Example 2:

# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None

        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        for interval in intervals:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res


"""
    sort first - sort intervals by 0th index
    create res list
    put the first interval into res
    
    iterate through interval
        if res[-1][1] >= interval[0] (meaning there's overlap)
            replace res[-1][1] with max between interval[1] or res[-1][1]
        else
            append interval into res
    
    return res

"""
