""" 
Find max value in an array using recursive method.
"""

from typing import List 
import random 

class Solution:

    def process(self, arr: List[int], L: int, R: int) -> int:
        if L == R: 
            return arr[L]

        mid = L + ((R-L)>>1)     # >>1 equals divide by 2
        left_max = self.process(arr, L, mid)
        right_max = self.process(arr, mid+1, R)
        return max(left_max, right_max)

    def get_max(self, arr: List[int]) -> int:
        return self.process(arr, 0, len(arr)-1) 


# arr = random.sample(range(20), k = 6)
arr = [17, 8, 2, 5, 12, 18]
print(arr)
print(Solution().get_max(arr))   # -> 18
