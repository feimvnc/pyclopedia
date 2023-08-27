""" 
dynamic sized sliding window problem sovling

-start small, expand expand until condition is matched 
-after condition is met, contracting from left side to find minimum size 
-expand to right
-find condition is met 
-contract from left 
"""

from typing import List  

# find the minimum length sub-array whose sum equals to x
class Solution:
    def dynamic_sliding_window(self, arr: List[int], x: int)->int:
        # Track min sub-array size 
        min_length = float('inf')    # The current range and sum of our sliding window
        start = 0       
        end = 0 
        current_sum = 0 

        # Extend the sliding window until our criteria is met 
        while end < len(arr):
            current_sum = current_sum + arr[end]
            end = end + 1 

            # Then contract the sliding window until it 
            # no longer meets our condition
            while start < end and current_sum >= x:
                current_sum = current_sum - arr[start]
                start = start + 1 

                # Update the min_length if this is shorter 
                # than the current min 
                min_length = min(min_length, end-start+1)

        return min_length 


arr = [1,2,3,4,5,6]
target = 9
print(arr)
print("minimum length:", Solution().dynamic_sliding_window(arr, target))

# python sl_dynamc_size.py 
# [1, 2, 3, 4, 5, 6]
# minimum length: 2