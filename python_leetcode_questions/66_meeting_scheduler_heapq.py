""" 
Given the availability time slot arrays slots1 and slots2 of two people and a meeting duration,
return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.
It is guaranteed that no two availability slots of the same person intersect with each other.
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, 
either start1 > end2 or start2 > end1.

Input: 
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration  = 8 
Output: [60,68]

Input:
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12 
Output: [] 
"""

# use priority queue method

from typing import List 
import heapq  
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # put slots onto heapq 
        heapq.heapify(slots1)
        heapq.heapify(slots2)

        while slots1 and slots2:
            l1, r1 = slots1[0]   # unpack schedules from both persons
            l2, r2 = slots2[0]
            left, right = max(l1, l2), min(r1, r2)
            if  right >= left + duration:
                return [left, left + duration]
            if l1 < l2:   # give up l1, pop the first value 
                heapq.heappop(slots1)
            else:
                heapq.heappop(slots2)

        return []   # exhausted no result 


slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration  = 8 
print(Solution().minAvailableDuration(slots1, slots2, duration))  # -> [60, 68]

slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12 
print(Solution().minAvailableDuration(slots1, slots2, duration))   # -> []
