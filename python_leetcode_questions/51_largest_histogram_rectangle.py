""" 
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest 
rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10 
The width of bar is 1, the largest rectangle
"""

from typing import List 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []    # create an empty sttack 
        res = 0     # set result to 0 
        for indx, height in enumerate(heights):    # enumerate through heights 
            stack_indx = indx     # track stack index, last popped index 
            while len(stack) > 0 and stack[-1][0] >= height:    # pop value check height
                stack_height, stack_indx = stack.pop()    # pop out 

            stack.append((height, stack_indx))    # [(2,0)]

            for val in reversed(stack):
                stack_height, stack_indx2 = val 
                width = indx - stack_indx2 + 1 
                res = max((width * stack_height), res)

        return res 

heights = [2,1,5,6,2,3]

print(heights)
print(Solution().largestRectangleArea(heights))

# python 51_largest_histogram_rectangle.py 
# [2, 1, 5, 6, 2, 3]
# 10