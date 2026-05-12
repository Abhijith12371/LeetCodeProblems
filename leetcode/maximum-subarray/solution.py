class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum=nums[0] 
        curr_sum=nums[0]
        for i in nums[1:]:
            curr_sum=max(i,curr_sum+i)
            global_sum=max(global_sum,curr_sum)
        return global_sum