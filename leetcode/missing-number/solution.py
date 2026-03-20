class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        sum_nums=sum(nums)
        n=len(nums)
        sum_n=(n*(n+1))//2
        return sum_n-sum_nums