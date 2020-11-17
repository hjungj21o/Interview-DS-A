# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = collections.defaultdict(list)

        for str in strs:
            my_sorted = tuple(sorted(str))
            dict[my_sorted].append(str)

        return dict.values()


"""
    time: O(N)
    space: O(N)
    
    Pattern: when the characters are all sorted, they should all have the same outcome
        ex: tea, eat = a e t
    Can have the sorted characters as key and store them in values (list)
    
    create a dict var, with defaultdict as an empty list
    
    iterate through input strs:
        create a tuple that is sorted with the ele
        dict[sorted].append(ele)
    
    return the values

"""
