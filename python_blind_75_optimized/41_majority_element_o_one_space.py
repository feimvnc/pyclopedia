""" 
Given an integer array of size n, find all elements that appears more than [n/3] times.
Note: The algorithm should run in linear time and in O(1) space.

Example:
Input: [3,2,3]
Output: [3]

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

from typing import List 
from collections import Counter

class Solution: 
    def majorityElement_not_o_one(self, nums: List[int]) -> List[int]:
        N = len(nums)
        c = Counter(nums)
        return [i for i,n in c.items() if n>(N//3)]   # Not O(1) space 

    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # n/3: meaning the max results are 2 numbers, can't be 3 numbers
        # >n/3 -> total 3xn numbers, the length has to be <3xn
        # define 2 numbers which could be > n/3
        count1,count2,cand1,cand2=0,0,None,None 

        if not nums: return []    # if input is empty, return []

        for n in nums:
            if cand1 == n:    # count first number  
                count1+=1
            elif cand2 == n:    # count second number  
                count2+=1
            elif count1==0:   # assign first number, or assign new number when count==0
                cand1=n 
                count1+=1
            elif count2==0:   # assign secode number 
                cand2=n 
                count2+=1
            else:
                count1-=1    # when 3rd number starts, reduce other two numbers 
                count2-=1
        return [c for c in [cand1,cand2] if nums.count(c) > (N//3)]


nums1=[3,2,3]
nums2=[1,1,1,3,3,2,2,2]
print(Solution().majorityElement_not_o_one(nums1))
print(Solution().majorityElement_not_o_one(nums2))

print(Solution().majorityElement(nums1))
print(Solution().majorityElement(nums2))
