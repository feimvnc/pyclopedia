""" 
Given a non-empty array of integers, return the k most frequent elements.

Examples: 
Input: nums = [1,1,1,2,2,3], k=2
Output: [1,2]

Input: nums = [1], k=1
Output: [1]
"""

from typing import List 
from collections import Counter
import heapq

class Solution:
    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = sorted(c, key=lambda x:c[x],reverse=True)
        return c[:k]


    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = [(-v, k) for k,v in c.items()]    # use minus for max-heap 
        heapq.heapify(c)
        output = [] 
        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])    # item[1]
        return output

nums = [1,1,1,2,2,3]
nums2 = [1]

print(Solution().topKFrequentCounter(nums, 2))
print(Solution().topKFrequentCounter(nums, 1))

print(Solution().topKFrequentHeap(nums, 2))
print(Solution().topKFrequentHeap(nums2, 1))

