""" 
Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k=2 
Output: [1,2]

Thought process:
-use dict to hold value and frequencies, {1:3, 2:2, 3:1}
but dict does not have order info
-use heapq, a tree structure, the parent value >= childrens
heapq is implemented using list 
we push dict item to heapq
we pushpop item to heapq, only keep k items
lastly pop out the keys
"""

from typing import List 
import heapq 

# Use heapq or priority queue method 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []    # answer, in heap 
        freq = dict()

        for num in nums:    # convert list to dict of {num: freq} pairs
            if num not in freq:
                freq[num] = 1 
            else:
                freq[num] += 1 

        # iterate dict items 
        for key, val in freq.items():
            if len(ans) < k:     # if ans len < k 
                heapq.heappush(ans, [val, key])    # push val first, used to sort 
            else: 
                heapq.heappushpop(ans, [val, key])    # keep ans len to k 

        return [key for value, key in ans]    # only need key, keep value for learning purpose


nums1 = [1,1,1,2,2,3]
nums2 = [1,1,1,2,2,3,5,5,5,5]
k=2 

print(nums1)
print(f'top {k} items: {Solution().topKFrequent(nums1, k)}')
print(nums2)
print(f'top {k} items: {Solution().topKFrequent(nums2, k)}')


# python top_k_priority_queue.py 
# [1, 1, 1, 2, 2, 3]
# top 2 items: [2, 1]
# [1, 1, 1, 2, 2, 3, 5, 5, 5, 5]
# top 2 items: [1, 5]