class Solution:
    def firstUniqChar(self, s: str) -> int:
        # if not s:
        #     return -1
        # dict = collections.Counter(s)

        # for i, char in s:
        #     if dict[char] == 1:
        #         return i

        # return -1

        dict = {}

        for i, char in enumerate(s):
            if char not in dict:
                dict[char] = [i]
            else:
                dict[char].append(i)

        for k, v in dict.items():
            if len(v) == 1:
                return v[0]

        return -1


"""
    count all the characters
    
    if there's one, get the index in the list

"""
