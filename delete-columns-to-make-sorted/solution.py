class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l=["".join(i) for i in zip(*strs)]
        c=0
        for i in l:
            if not all([ord(i[j])<=ord(i[j+1]) for j in range(0,len(i)-1)]):
                c+=1
        return c