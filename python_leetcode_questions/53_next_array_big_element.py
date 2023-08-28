""" 
Given two arrays, find the next big num in next array.

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: 
return value in nums2 which is bigger 
return -1 if not found 

nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
"""

from typing import List 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []    # keep result 
        stack = []    # store for monotone stack
        num_map = {}    # used for { num1: num2 }

        for num in nums2:    # 
            while stack and num > stack[-1]:
                num_map[stack[-1]] = num 
                stack.pop()
            stack.append(num)

        for num in nums1:
            res.append(num_map.get(num, -1))
        return res 


nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(Solution().nextGreaterElement(nums1, nums2))
