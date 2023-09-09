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

    def longestPalindrom_2(self, s: str) -> bool:
        N = len(s)

        # check if s self is palindrom
        # aba
        for i in range(N):
            if s == s[::-1]:
                return True     
            # remove left char
            elif s[i:] == s[i:][::-1]:   
                return True        
            # remove right char 
            elif s[:N-i] == s[:N-i][::-1]:
                return True
            # remove chars at both ends   
            elif s[i+1:N-i] == s[i+1:N-i][::-1]:
                return True 
            # return False if not found 
            return False
        return False  


s, s1, s2, s3 = "abccccdd", 'a',  'bb', 'ccc'
print(Solution().longestPalindrome(s))        
print(Solution().longestPalindrome(s1))        
print(Solution().longestPalindrome(s2))   
print(Solution().longestPalindrome(s3))     

print(Solution().longestPalindrom_2('abccba'))   # -> True 
print(Solution().longestPalindrom_2('abc'))   # -> False 

print(Solution().longestPalindrom_two_pts('a'))   # -> False 


