class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float('inf') for amt in range(amount + 1)]
        num_coins[0] = 0

        for coin in coins:
            for amount in range(len(num_coins)):
                if coin <= amount:
                    num_coins[amount] = min(
                        num_coins[amount], 1 + num_coins[amount - coin])

        return num_coins[amount] if num_coins[amount] != float('inf') else -1


"""
    bottom-up dynamic programming approach
    
    create a list, num_coins with length of amount + 1 and default value being inf
    first element will be 0
        **num_coins index will represent the actual amount of dollars, element will hold the min. amount of coins it
            will take to reach index(amount)
        **first element is 0 because to get to amount 0, we need 0 coins
        
        iterate through all the coins because we need to check how many coins it takes to reach that amount
            nested loop where we go through the index(amount) in the num_coins list
                if coin <= amount (meaning if change is lower or is the exact change of amount):
                    num_coins[amount] = get the minimum between current num of coins OR num_coins[amount - coin] (change after you subtract amount - current coin) + 1(current coin denomination)
                    
        return -1 if amount is still inf(there's no change small enough to get our amount) or num_coins[amount] (min number of change needed to get to that amount)

"""
