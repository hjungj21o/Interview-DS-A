class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #         if not nums: return None

        #         dict = {}

        #         for num in nums:
        #             if num in dict:
        #                 dict[num][1] += 1
        #             else:
        #                 dict[num] = [num, 1]

        #         res = set()
        #         sorted_v = sorted(dict.values(), key=lambda x:x[1])

        #         i = len(sorted_v) - 1

        #         while k > 0:
        #             ele, freq = sorted_v[i]

        #             if ele not in res:
        #                 res.add(ele)
        #                 k -= 1
        #             i -= 1

        #         return res

        if len(nums) <= 1:
            return nums

        dict = collections.Counter(nums)
        max_val = max(dict.values())
        buckets = list([] for i in range(max_val + 1))

        for key, val in dict.items():
            buckets[val].append(key)
        res = []
        # print(buckets)
        for i in range(len(buckets) - 1, 0, -1):
            res += buckets[i]
            k -= len(buckets[i])
            if k < 1:
                break

        return res


"""
    Brute force:
        create a dictionary, key being the element of nums, value being a list of element and frequency
        
        iterate through nums to build dict:
            if it exists, dict[num][1] += 1
            else, dict[num] = [num, 1]
        
        sort the values of dict by its frequency
        
        while k > 0:
            add to res list the element (sorted[i]0)
            k -= 1
        
        return res
    Time: O(n log n)
    Space: O(n + m)
    
    Optimized: using buckets:
        create a counter dictionary
        create a bucket for the elements, with value of dict being the index
        
        iterate through dict, append key to buckets[val]
        
        create result list
        iterate through buckets backwards:
            res += buckets[i]
            decrement k by length of buckets
            if k < 1: break
            
        return res
        
    Time: O(n)
    Space: O(n + m)

"""
