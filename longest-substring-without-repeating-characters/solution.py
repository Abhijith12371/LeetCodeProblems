class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=[]
        max_len=0
        for i in s:
            if i in substring:
                while i in substring:
                    substring.pop(0)
        
            substring.append(i)
            max_len=max(max_len,len(substring))
        return max_len
        
