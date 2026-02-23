class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        istrue=False
        for i,ele in enumerate(nums):
            if ele in d:
                if abs(i-d[ele])<=k:
                    return True
                
            d[ele]=i
        return False
