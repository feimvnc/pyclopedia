"""
Given a string S, find length of the longest substring with all distinct characters.
For example, for input "abca",
the output is 3 as "abc" is the longest substring with all distinct characters.
"""

class Solution:

    def is_distinct_str(self, s: str) -> bool:
        if len(list(s)) == len(set(s)):
            return True 
        else: 
            return False 

    def longestSubStr(self, s: str) -> int:
        all_subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        max_len = 1 
        for sub in all_subs:
            if len(sub) > max_len and self.is_distinct_str(sub):
                max_len = len(sub)
        return max_len 

s = "abca"

print(Solution().longestSubStr(s))  # -> 3