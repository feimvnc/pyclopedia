""" 
Given an array which is already sorted in ascending order, 
find two numbers such that  they add up to a specfic target number.
Input: numbers: [2,7,11,15], target: 9
Output: [1,2]    # the index starts with 1, not 0

Hint: for sorted array, no need to look up number > target.
"""
from typing import List  

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l<r:
            curSum = nums[l]+nums[r]
            if curSum > target:
                r -= 1 
            elif curSum < target:
                l += 1 
            else: 
                return [l+1, r+1]   # found, add 1 to index 
        return []

print(Solution().twoSum([2,7,11,15], 9))