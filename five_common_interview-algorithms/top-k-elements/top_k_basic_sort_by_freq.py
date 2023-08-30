""" 
Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k=2 
Output: [1,2]

Thought process:
sort by frequency + pick top k  

Time complexity: O(nlogn)  
Space complexity: O(n) 
"""

from typing import List 

class Solution:
    def topKElement(self, nums: List[int], k: int):

        freq = {}
        ans = []    # keep answers 

        # convert list to dict freq 
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1
        print(freq)       # {1: 3, 2: 2, 3: 1}

        # sort dict by 
        ans = list(freq.items())    # convert freq to list 
        print(ans)     # [(1, 3), (2, 2), (3, 1), (5, 4)]
        ans.sort(key=lambda x: x[1])    # sort list tuples by frequency 
        print(ans)     # [(3, 1), (2, 2), (1, 3), (5, 4)]
            
        return [t[0] for t in ans[len(ans)-k:]]    # return first value, [(1, 3), (5, 4)]


nums = [1,1,1,2,2,3,5,5,5,5]
k=2 
print(nums)
print(Solution().topKElement(nums, k))

# python top_k_basic_sort_by_freq.py 
# [1, 1, 1, 2, 2, 3, 5, 5, 5, 5]
# {1: 3, 2: 2, 3: 1, 5: 4}
# [(1, 3), (2, 2), (3, 1), (5, 4)]
# [(3, 1), (2, 2), (1, 3), (5, 4)]
# [1, 5]
