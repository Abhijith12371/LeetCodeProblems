class Solution:
    def climbStairs(self, n: int) -> int:
        def countStairs(n,memo):
            if n==0 or n==1:
                return 1
            if n not in memo:
                memo[n]=(countStairs(n-1,memo))+(countStairs(n-2,memo))
            return memo[n]
        memo={}
        return countStairs(n,memo)