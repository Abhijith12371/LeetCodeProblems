class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x <= 2**31 - 1:
            sign=-1 if x<0 else 1
            a=str(abs(x))
            rev=a[::-1]
            res=sign*int(rev)
            if res>2**31-1 or res<-2**31:
                return 0
            return res