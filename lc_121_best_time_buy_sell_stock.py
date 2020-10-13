class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_val = 0

        for price in prices:
            if price < min_val:
                min_val = price
            elif price - min_val > max_val:
                max_val = price - min_val
        return max_val


"""
    greedy
    create two vars, min val and max val. min val should be infinity and max val should be 0
    create a loop to iterate through the input array list
        compare min val to the current element. if curr val is less, then replace min val
        else if compare the difference between element and min val to max val
        if it is greater, than replace max val
    
    return max val
    time = O(n) b/c we're iterating through the entire list 
    space = O(1) b/c 
    
"""
