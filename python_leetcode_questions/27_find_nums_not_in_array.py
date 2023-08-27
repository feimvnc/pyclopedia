""" 
Given an array nums of n integers where nums[i] is in the range [1,n],
return an array  of all the integers in the range [1,n] that do not 
appear in nums.
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

from typing import List 

class Solution:
    def findDisappeardNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) -1     # find index based on value  
            nums[i] = -1 * abs(nums[i])    # mark index to negative if exists

        res = [] 
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)   # convert index + 1 to value 
        return res 

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappeardNumbers(nums))