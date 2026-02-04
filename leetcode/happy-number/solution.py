class Solution:
    def isHappy(self, n: int) -> bool:
        def isHappyNumber(s,l):
            sum_num=0
            if s==1:
                return True
            if s in l:
                return False
            l.append(s)
            for i in str(s):
                sum_num+=int(i)**2
            return isHappyNumber(sum_num,l)
        l=[]
        return isHappyNumber(n,l)