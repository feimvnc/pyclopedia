""" 
Given a sorted array (an ascending order).

Input: nums = [-1,0,3,5,9,12], target=9
Output: 4   
9 exists in nums and its index is 4

If target not exists, return -1
"""
from typing import List 

class Solution:
    def search(self, nums:  List[int], target: int) -> int: 
        for i, n in enumerate(nums):    # just using loop
            if n == target:
                return i    # return the index of target
        return None 

    # because array is sorted, we can start in the middle  
    def binarySearch(self, nums:  List[int], target: int) -> int: 
        left = 0 
        right = len(nums)
        while left <= right:
            mid = left+(right-left)//2    # floor divide 
            num = nums[mid]
            if target == num:
                return mid 
            elif target > num: 
                left = mid+1
            elif target < num: 
                right = mid-1
        return -1     # not found case


print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().binarySearch([-1,0,3,5,9,12], 9))