from typing import List 

class Solution():
    def plusOne(self, digits: List[int] ) -> int:
        ls = len(digits)
        for i in reversed(range(ls)):
            if digits[i] < 9:
                digits[i] += 1 
                return digits 
            else:
                digits[i] = 0  
        digits.insert(0, 1)
        return digits 

print(Solution().plusOne([99]))