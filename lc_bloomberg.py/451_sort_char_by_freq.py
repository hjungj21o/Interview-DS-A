# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""

        dict = collections.Counter(s)
        max_freq = max(dict.values())

        my_list = list([] for i in range(max_freq + 1))
        for k, v in dict.items():
            my_list[v].append(k)

        res = []
        for i in range(len(my_list) - 1, 0, -1):
            for char in my_list[i]:
                res.append(char * i)

        return "".join(res)


"""
    counter dictionary then create a bucket with max value
    
    create a counter dict
    get the max frequency max(dict.values())
    create a 2d bucket, going up to the max freq + 1
    
    iterate through counter dict:
        append character into [v] = v will serve as the index and the # of times it needs to be repeated
        
    create a result list
    
    iterate through the bucket backwards
        iterate through the eles in bucket, add to the res list
        
    return the joined res list

"""
