# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = r = 0
        seen = {}
        my_max = 1

        while r < len(s):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            my_max = max(my_max, r - l + 1)
            seen[s[r]] = r
            r += 1

        return my_max


"""
    create two pointers, l & r, pointing to 0
    create a dict to keep track of where chars were last seen
    create max counter, starting at 1 (b/c max will be at least 1 at all times)
    
    iterate through the string (while r < length of s):
        recalculate max by comparing current max and the diff between r and l + 1(2 - 0 + 1 = 3)
        add the char to seen, value at r (index)
        increment r
        
        if it has been seen, then move left pointer to last seen's index + 1 OR current left, whichever is greater
    
"""
