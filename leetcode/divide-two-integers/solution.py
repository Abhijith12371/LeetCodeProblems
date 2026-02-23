class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        #divison means how many times we can subtract the divisor
        # c=0
        # n=False
        # if dividend == -2**31 and divisor == -1:
        #     return 2**31 - 1
        
        # # Determine sign
        # n = (dividend < 0) != (divisor < 0)

        # dividend=abs(dividend)
        # divisor=abs(divisor)
        # while dividend>=divisor:
        #     dividend=dividend-divisor
        #     c+=1
        # if n:
        #     return -c
        # else:
        #     return c
        
        c=0
        l=[]
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>0:
            res=divisor*(2**c)
            if res>dividend:
                l.append(math.floor(2**(c-1)))
                dividend=dividend-divisor*(2**(c-1))
                c=0
            else:
                c+=1
        if negative:
            return -sum(l)
        return sum(l)