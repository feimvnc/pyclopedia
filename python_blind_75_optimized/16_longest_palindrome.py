""" 
Given a string s, return the length of the longest palindrome that can be built 
with those letters.  
Input: s = "abccccdd
Output: 7
"dccaccd"

Idea: to count even number of chars 
"""

class Solution:
    def longestPalindrome(self, s: str) -> int: 
        char_count = {}   # use dict{} for counting 

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1   # char not seen before, add all chars

        final_count = 0 
        odd_is_present = False 
        for char in char_count:
            if char_count[char] % 2 == 0:
                final_count += char_count[char]
            else:
                final_count += (char_count[char]-1)    # for case of "ccc"
                odd_is_present = True 

        if odd_is_present:   # only if odd is present   
            final_count += 1 
        return final_count

s, s1, s2, s3 = "abccccdd", 'a',  'bb', 'ccc'
print(Solution().longestPalindrome(s))        
print(Solution().longestPalindrome(s1))        
print(Solution().longestPalindrome(s2))   
print(Solution().longestPalindrome(s3))        