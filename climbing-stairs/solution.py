class Solution:
    def climbStairs(self, n: int) -> int:
        def countStairs(n,memo):
            if n==0 or n==1:
                return 1
            if n not in memo:
                memo[n]=(countStairs(n-1,memo))+(countStairs(n-2,memo))
            return memo[n]
        def countStairs_tab(n,ways):
            for i in range(1,len(ways)):
                if i==1:
                    ways[i]=ways[i-1]
                else:
                    ways[i]=ways[i-1]+ways[i-2]
            return ways[n]
        memo={}
        ways=[0]*(n+1)
        ways[0]=1
        return countStairs_tab(n,ways)