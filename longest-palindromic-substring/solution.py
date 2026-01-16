class Solution:
    def longestPalindrome(self, s: str) -> str:
        l={}
        def is_palindrome(string):
            if string==string[::-1]:
                return True
            else:
                return False
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if is_palindrome(s[i:j]):
                    l[len(s[i:j])]=s[i:j]
        if l:
            return l[max(l)]
        else:
            return s