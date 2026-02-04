from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=Counter(nums)
        l=[]
        for i in a.items():
            for j in a:
                if a[j]==1:
                    return j
        