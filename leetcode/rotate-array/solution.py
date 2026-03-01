class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[0]*len(nums)
        for index,value in enumerate(nums):
            l[(index+k)%len(nums)]=nums[index]
        nums[:]=l[:]
        return nums