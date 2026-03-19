class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        i=2
        if 8<=n<=11:
            return 11
        while True:
            s=str(i)
            pal=int(s+s[-2::-1])
            if pal>=n and isPrime(pal):
                return pal
            i+=1