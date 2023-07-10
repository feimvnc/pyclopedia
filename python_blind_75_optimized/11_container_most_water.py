""" 
Given n non-negative integers a1, a2, ..., an, where each represents a point at 
coordinatee (i, ai) * n vertical lines are drawn such that the two endpoints 
of the line i is at (i, ai), and (i, 0). Find two lines, which together with 
the x-axis forms a container, such that the container contains the most water.

Notice that you are not slant the container.

Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array. In this case,
the max area of water (blue section) the container can contain is 49.

"""

from typing import List 
import numpy as np  
from itertools import combinations 

class Solution:

    def container_most_water(self, heights: List[int])->int:
        # get all list of height pairs from left to right 
        h = list(combinations(heights, 2))

        # use map for element wise operation
        # calculate area = min of height pair * (right index - left index)
        # return the max value
        return max(list(map(lambda x: min(x)*(heights.index(x[1])-heights.index(x[0])), h)))


heights = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.container_most_water(heights))


""" 
$ python 11_container_most_water.py 
49

"""