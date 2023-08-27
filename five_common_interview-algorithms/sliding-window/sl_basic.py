""" 
sliding window problem solving considerations
-use size to created a container
-container is the sub-array
-container size is the provided value 
-move container from left to right
-add to the right
-pop from the left 
-store container operation results

"""

# sum up the subarray adn add it to the result 
# the simpliest form of sliding window 
from typing import List 

class Solution:
    def sliding_window(self, arr: List[int], k: int) -> List[int]:
        curr_subarray = sum(arr[:k])    # first sub-array
        result = [curr_subarray]    # assign value to result 

        # move sub-array window, add to right, remove from left
        for i in range(1, len(arr)-k+1):    # range is exclusive, thus add 1
            curr_subarray = curr_subarray - arr[i-1]     # remove 
            curr_subarray = curr_subarray + arr[i+k-1]    # add, arr starts at 0, thus minus 1 
            result.append(curr_subarray)     # append 
        
        return result  

arr = [ i for i in range(10) ]
k = 3
print(arr)
print(Solution().sliding_window(arr, k))


# Output:
# python sl_basic.py 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3, 6, 9, 12, 15, 18, 21, 24]