""" 
Given two arrays, return intersection of them, compute each element only once.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Method:
Use two pointers to go through each array
If nums1[l] < nums2[r], add to result 
If nums1[l] < nums2[r], l +=1
if nums1[l] > nums2[r], r +=1
"""

from typing import List 

# csd, cer, check, sort, defind; computte, edge, return 
class Solution: 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()

        l, r = 0, 0    # use two pointers moving from left to right 
        res = set()    # use set built-in to keep unique value

        while l<len(nums1) and r<len(nums2):
            if nums1[l]==nums2[r]:
                res.add(nums1[l])
                l+=1
                r+=1
            elif nums1[l] < nums2[r]:
                l+=1
            elif nums1[l] > nums2[r]:
                r+=1

        return [i for i in res]
        # return list(res)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(f'{nums1=}, {nums2=}')
print(Solution().intersection(nums1, nums2))        

# python 54_two_arrays_intersection.py 
# nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]
# [9, 4]