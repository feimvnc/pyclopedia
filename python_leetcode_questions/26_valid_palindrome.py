""" 
Given a string s, return true  if the s can be palindrome after 
deleting at most one character from it.

Input: s  = "aba"
Output: true 
"""

class Solution:
    def validPalindrome(self, s: str) ->bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1]
                        or skipR == skipR[::-1])
            l, r = l+1, r-1
        return True 

    def validPalindrome_2(self, s: str) -> bool:
        left = 0 
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1 
                continue 
            # print(left,right)
            if not s[right].isalnum():
                right -= 1
                continue 
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else: 
                return False 
        return True 


s1 = "race a car"
s2 = "A man, a plan, a canal: Panama"
print(s1, Solution().validPalindrome_2(s1))
print(s2, Solution().validPalindrome_2(s2))


