class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^A-Za-z0-9]', '', s)

        s="".join(("".join(s).split(" ")))
        if s.lower()==s[::-1].lower():
            return True
        else:
            return False