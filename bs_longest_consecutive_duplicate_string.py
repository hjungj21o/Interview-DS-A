# Given a string s, return the length of the longest substring with same characters.

# For example, given abcccdda, return 3 since it's the length of ccc.

# Example 1
# Input

# s = "abbbba"
# Output

# 4

class Solution:
    def solve(self, s):
        # Write your code here
        count = 1
        maxnum = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                count = 1
            maxnum = max(maxnum, count)

        return maxnum
