""" 
Given a string s, rearrange the characters of s so that any two 
adjacentt characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example:
Input s = "aab"
Output: "aba"

Example:  s = "aaab"
Output: ""
"""

from collections import Counter
import heapq

class Solution: 
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)     # Hashmap, counter for each chars 
        maxHeap = [[-cnt, char] for char, cnt in count.items()]    # build list, not a heap yet 
        heapq.heapify(maxHeap)     # turn the list to maxHeap, O(n)

        # build results 
        prev = None    # for previous char 
        res = "" 
        while maxHeap or prev:
            # a -> 2, b -> 1  
            if prev and not maxHeap:
                return ""     # no solution

            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char 
            cnt += 1 

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None 

            if cnt != 0:
                prev = [cnt, char]
        return res 

s1 = "aab"
s2 = "aaab"

print(Solution().reorganizeString(s1))
print(Solution().reorganizeString(s2))

# python 50_reorganize_string.py 
# aba
