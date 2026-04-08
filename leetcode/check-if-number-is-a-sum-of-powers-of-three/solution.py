class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i,curr):
            if curr==n:
                return True
            if curr>n:
                return False
            power=curr+3**i
            if power>n:
                return False
            return backtrack(i+1,power) or backtrack(i+1,curr)
        return backtrack(0,0)