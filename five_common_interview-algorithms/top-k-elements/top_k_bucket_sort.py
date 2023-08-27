""" 
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2 
Output: [1,2]

Below solution uses Bucket Solution, which has O(N).
Better than Heap method, which has O(NlogN)
"""

from typing import List 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}    # use the hashmap to record the count of nums

        # don't use number for buckets, because number 1,000 needs 1,000 buckets
        # rather use the total count of array elements, the provided numbers 
        # clever trick
        # [1, 1, 1, 2, 2, 3]
        # i (count)   0   1   2   3   4   5   6   
        # values      _  [3] [2] [1]  _   _   _
        freq = [[] for i in range(len(nums)+1)]    # buckets which matchs length of nums

        for n in nums:
            count[n] = 1 + count.get(n, 0)    # update count{} with actual nums counts 
        print(count)    # {1: 3, 2: 2, 3: 1}

        for n, c in count.items():    # 
            freq[c].append(n)    # use index for counts, but count as key
        print(freq)    # [[], [3], [2], [1], [], [], []]

        res = [] 
        # from last index len(freq)-1, up to 0 but excluding -1, in descending order -1 
        for i in range(len(freq) - 1, -1, -1):   # index based, index from largest to smallest
            for n in freq[i]:    # bucket content [3], if not empty, it can have multiples [3,4,5]
                res.append(n)    # add to result 
                if len(res) == k:
                    return res 


nums = [1,1,1,2,2,3]
k = 2
print(f'{nums=}')
print(f'top {k=} {Solution().topKFrequent(nums, k)}')

# python top_k_bucket_sort.py 
# nums=[1, 1, 1, 2, 2, 3]
# top k=2 [1, 2]
