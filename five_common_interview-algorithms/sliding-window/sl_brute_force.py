""" 
Find the longest substring without repeating characters
Using brute force approach, as a comparison

O(N*N)
"""

class Solution: 
    def longest_substr(self, s: str) -> int:
        longest = 0 
        for start_index in range(len(s)):    # starts from 0 and move to next 
            contains=set()                   # create a new set for each start_index 
            for letter in s[start_index:]:   # slice from start_index till end 
                if letter in contains:       # duplicate found 
                    break
                contains.add(letter)         # not executed when break 
            longest = max(longest, len(contains))    # max of prev and new length, after break
        return longest 


s1='abcabcbb'
s2='bbbbb'
print(Solution().longest_substr(s1))
print(Solution().longest_substr(s2))
