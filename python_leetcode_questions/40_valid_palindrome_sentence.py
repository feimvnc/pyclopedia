""" 
Given a string, determine if it is a palindrome.
Considering only alphanumeric characters and ignoring cases.
For this problem we define empty string as valid  palindrome.

Example:  
Input: "A man, a plan, a canal: Panama"
Output: true 

Input: "race a car"
Output: false 
"""

# we use left and right pointers to move towards to center and compare
class Solution: 
    # use normal left and right pointer to move towards center approach 
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1    # left, right, -1 because it is 0 index
        while l<r:   # loop through full str 
            while l<r and not s[l].isalnum():    # skip l if not alnum
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():       # when not match 
                return False    
            l+=1    # match found, move l and r 
            r-=1
        return True 

    # use regex to clean up input str first to simply char handling
    def isPalindrome_2(self, s: str) -> bool: 
        import re 
        # remove non-alnum 
        # s1="A man, a plan, a canal: Panama" -> s1='amanaplanacanalpanama'
        s = re.sub("[^a-z|^0-9]", "", s.lower())
        l,r = 0,len(s)-1
        while l<r:      # direct compare l and r
            if s[l]!= s[r]:
                return False 
            l+=1
            r-=1
        return True 


s1="A man, a plan, a canal: Panama"
s2="race a car"

print(Solution().isPalindrome(s1))
print(Solution().isPalindrome(s2))

print(Solution().isPalindrome_2(s1))
print(Solution().isPalindrome_2(s2))