class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mins = float('inf')
        res = []

        for i in range(len(arr) - 1):
            j = i + 1

            mins = min(mins, abs(arr[i] - arr[j]))

        for i in range(len(arr) - 1):
            j = i + 1
            if arr[j] - arr[i] == mins:
                res.append([arr[i], arr[j]])

        return res
