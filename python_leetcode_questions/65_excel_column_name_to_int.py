""" 
Excel column has A,B,C...AA,AB..., 
Given a column name, convert it to integer.

A equals to 1, ...
Exampel:
Input: = 'A' 
Output: 1
 
Input: 'AB' 
Output: 28
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord('A') - 1  # if 'A', value = 1, thus -1
        n = len(s)
        result = 0 

        for i in range(n):
            # n-1 -i , from right toward to left, index 
            result += (ord(s[n-1-i])-base) * pow(26, i)
        
        return result 

print(Solution().titleToNumber('A'))  # -> 1
print(Solution().titleToNumber('AB')) # -> 28 
