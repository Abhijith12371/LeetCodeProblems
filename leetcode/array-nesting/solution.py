class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_len=0
        c=0
        visited=[False]*len(nums)
        for i in range(len(nums)):
            if not visited[i]:
                k=i
                c=0
            while not visited[k]:
                visited[k]=True
                k=nums[k]
                c+=1
            max_len=max(max_len,c)
        return max_len