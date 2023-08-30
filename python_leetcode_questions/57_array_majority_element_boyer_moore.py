""" 
Given an array  of size n, find the majority element.
The majority element is the element that appears more than : n/2 : times.

Hints: The must be only 1 element because only 1 elemment can appear n/2.

Boyer–Moore majority vote algorithm:  
The Boyer-Moore voting method is one of the most often used optimum algorithms 
for determining the majority element among elements with more than N/2 occurrences. 
This works wonderfully for finding the majority element, which requires 
two traversals over the provided items and is O(N) time and O(1) space complexity.
"""

from typing import List 

class Solution:
    def majorityElement(self, nums: List[int])->int:
        candidate = nums[0]    # init candidate with first element 
        counter = 1      # init counter to 1 because we have a candidate 
        for i in range(1, len(nums)):    # start at 1 to compare
            if counter == 0:
                candidate = nums[i]      # change candidate if candidate cancelld out  
            if nums[i] == candidate:     # increment counter for same candidate
                counter += 1 
            else:
                counter -= 1             # cancel out if diff candidate 

        return candidate                 # result must > n/2


nums1 = [3,2,3]
nums2 = [2,2,1,1,2,2]

print(nums1, '->', Solution().majorityElement(nums1))
print(nums2, '->', Solution().majorityElement(nums2))

# python 57_array_majority_element_boyer_moore.py 
# [3, 2, 3] -> 3
# [2, 2, 1, 1, 2, 2] -> 2
