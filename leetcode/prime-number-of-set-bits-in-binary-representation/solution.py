class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def countNumberOfOnes(bNumber):
            s=[]
            numberOfOnes=len([True for i in str(bNumber) if i=='1'])
            return numberOfOnes
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        c=0
        # l=[]
        for i in range(left,right+1):
            bits=countNumberOfOnes(bin(i))
            if isPrime(bits):
                c+=1
                # l.append(i)
        return c