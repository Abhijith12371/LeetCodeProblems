class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        for right in range(len(nums)):
            if nums[left]!=nums[right]: #0 0 0 1 0 2
                left+=1
                nums[left]=nums[right]
        return left+1
