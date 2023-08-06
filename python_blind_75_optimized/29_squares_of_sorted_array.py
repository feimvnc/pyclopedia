""" 
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
"""

from curses.ascii import SO
from typing import List 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [] 
        l, r = 0, len(nums)-1 
        while l<=r:
            if nums[l]*nums[l] >  nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l += 1
            else:
                res.append(nums[r]*nums[r])
                r -= 1

        return res[::-1]    # reverse order 
        
nums = [-4, -1, 0, 3, 10]

print(Solution().sortedSquares(nums))