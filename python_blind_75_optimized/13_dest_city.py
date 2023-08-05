from typing import List 

class Solution:

    def desCity(self, paths: List[List[str]])->str:
        outgoing_count = {}
        for path in paths: 
            a, b = path    # unpack [a, b], 2nd array, b will be first value
            outgoing_count[a] = outgoing_count.get(a, 0) + 1   # [a,b], [b,c], [c,d], 
            outgoing_count[b] = outgoing_count.get(b, 0)   # the first time appearance
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city 

    def desCity2(self, paths: List[List[str]])-> str:
        A, B = map(set, zip(*paths))
        return (B-A).pop()

print(Solution().desCity([['A','B'], ['B','C'],['C','D']]))
print(Solution().desCity2([['A','B'], ['B','C'],['C','D']]))