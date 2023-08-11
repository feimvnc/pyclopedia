""" 
Given a string s, return true if the s can be palindrome after 
deleting at most one character from it.

Input: s = "aba"
Output: true 

Input: s = "abc"
Output: false

left   right
|      |
aaaaaaaa
"""

class Solution: 

    def validPalindrome_two_pointer(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                l2,r2,l3,r3 = l+1,r,l,r-1    # move right or move left one step, after first match 
                left_move, right_move = True, True    # move 1 step further and check 
                while l2<r2:    # left to right move 
                    if s[l2] != s[r2]:
                        left_move = False 
                        break 
                    l2+=1
                    r2-=1
                while l3<r3:
                    if s[l3] != s[r3]:    # right to left move 
                        right_move = False 
                        break 
                    l3+=1
                    r3-=1
                if left_move or right_move:
                    return True 
                else: 
                    return False 

            l+=1
            r+=1
        return True                     


    def validPalindrome_basic(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False 
            l+=1
            r-=1

        return True 


s1 = 'aba'
s2 = 'abc'
print(Solution().validPalindrome_basic(s1))
print(Solution().validPalindrome_basic(s2))