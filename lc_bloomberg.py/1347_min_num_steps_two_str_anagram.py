class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        bucket_s = list(0 for i in range(27))
        bucket_t = list(0 for i in range(27))

        for k, v in count_s.items():
            bucket_s[ord(k) - 97] = v

        for k, v in count_t.items():
            bucket_t[ord(k) - 97] = v

        res = 0
        for i in range(27):
            res += abs(bucket_s[i] - bucket_t[i])

        return res // 2

#         memo = collections.Counter(s)
#         # saving the number of occurance of characters in s
#         # for char in s:
#         #     memo[char] += 1

#         # count = 0
#         for char in t:
#             if memo[char]:
#                 memo[char] -=1   # if char in t is also in memo, substract that from the counted number
#             # else:
#             #     count += 1
#         # return count #or
#         return sum(memo.values())
