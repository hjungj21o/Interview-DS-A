class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n >= 0:
            return self.helper(x, n)
        else:
            return 1/self.helper(x, (n * -1.0))

    def helper(self, x, n):
        if n == 0:
            return 1.0

        half = self.helper(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


"""
    solve recursively
        can solve o(N) and O(log n time)
            linear = go until n is 0, which then you return 1
            
    log n:
        same base case: if n == 0, return 1
        
        if n < 0:
            helper(x, n)
        else:
            helper(1/x, n)
            
        create a helper function, takes in x and n
            if n == 0: return 1
            
            if n % 2 == 0:
                return helper(x, n // 2) * helper(x, n // 2)
            else:
                return helper(x, n // 2) * helper(x, n // 2) * x
            
"""
