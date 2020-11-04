class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #         dict = collections.Counter(s)

        #         for char in t:
        #             dict[char] -= 1

        #         for v in dict.values():
        #             if v != 0: return False
        #         return True

        dict = {}

        alpha = list(0 for num in range(27))

        for char in s:
            alpha[ord(char) - 97] += 1

        for char in t:
            alpha[ord(char) - 97] -= 1

        return not any(alpha)


"""
    suboptimal:
        
        collections.counter s
        collections.counter t
        
        if every count is 2, return True, else return False
        time: O(n)
        space: O(n)
        
    optimal:
        create a bucket equal to 26 characters in alphabet
        
        iterate through s, ord the char (to convert to ASCII), minus it by 97 and up the count
        iterate through t, ord the char, minus by 97, dec the count
        
"""
