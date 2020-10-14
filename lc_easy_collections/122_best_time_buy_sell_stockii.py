class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sumz = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                sumz += (prices[i] - prices[i - 1])

        return sumz


"""
    look at the previous day and compare it to the current day
    create sum val
    iterate through the length of the array but starting at 1
        if the previous day is less than current day, increment sum by the difference of those two nums
    returm sum

"""
