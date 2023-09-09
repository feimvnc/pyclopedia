"""
Given a string S consisting only '0's and '1's,
 print the last index of the '1' present in it.
"""

import heapq
import collections
from typing import Any 

class Solution:

    def index_of_last_one(self, s: str) -> int:
        if not s: return False

        N = len(s)
        # for i in range(N-1, 0, -1):
        for i in reversed(range(N)):
            if s[i] == '1':
                return i
        return -1 

    # use map 
    def index_of_last_one_map(self, s: str) -> int:
        if not s: return False 

        d = {}
        N = len(s)
        for i in range(N):
            d[s[i]] = i
            print(d.items())
        return d['1']

    # use heapq  
    def index_of_last_one_heap(self, s: str) -> int:
        if not s: 
            return False  

        N = len(s)

        res = [] 
        for i in range(N):
            if s[i] == '1':
                heapq.heappush(res, (i, s[i]))
                print(res)
        return heapq.nlargest(1, res)[0][0]

    # use xor 
    def index_of_last_one_xor(self, s: str) -> int:
        if not s: 
            return False 

        N = len(s) - 1  
        n = N 
        while n >=0:
            if (ord(s[n]) ^ ord('0')):   # ord convert str to int, ord('1') ^ ord('0') -> 1 
                return n
            n -= 1

    # use dict and s
    def index_last_one_filter(self, s: str) -> int: 
        if not s: return False 

        N = len(s)
        def is_one(s: Any) -> bool:
            return s if s[1] == '1' else 0

        # d = {k:v for k, v in enumerate(s)}
        # print(sorted(list(filter(is_one, d.items())))[-1][0])   # -> 5,  [(2, '1'), (5, '1')]
        # return sorted(list(filter(is_one, d.items())))[-1][0]

        d = list(zip(s, range(N)))  
        # [('0', 0), ('0', 1), ..., ('1', 5)]
        return sorted(d)[-1][1]

    # bfs 
    def index_last_one_bfs(self, s: str) -> int:
        if not s: return False 
        N = len(s)
        ONE = '1'
        # ZERO = '0'
        queue = collections.deque() 
        queue.append(s[0])
        i = 0
        res = -1 
        while queue and i < N - 1:
            print(queue)
            # deque(['0'])
            # deque(['0'])
            # deque(['1'])
            # deque(['0'])
            # deque(['0'])
            # deque(['1'])
            x = queue.pop()
            if x == ONE:
                res = i 
            i += 1    # increment first 
            queue.append(s[i])   # then append 
        return res 

    # recursive  
    def index_last_one_recursive(self, s: str) -> None:
        if not s: 
            return -1
        
        if s and s[-1] == '1':
            # print('x, ', len(s)-1)   # print answer 
            return len(s)-1 
        n = len(s)-1
        s = s[:n]
        return self.index_last_one_recursive(s)     # return is needed to avoid None 
        

print(Solution().index_of_last_one('0010010'))   # -> 5
print(Solution().index_of_last_one_map('0010010'))   # -> 5
print(Solution().index_of_last_one_heap('0010010'))   # -> 5, [(2, '1'), (5, '1')]
print(Solution().index_of_last_one_xor('0010010'))  # -> 5
print(Solution().index_last_one_filter('0010010'))  # -> 5
print(Solution().index_last_one_bfs('0010010'))  # -> 5
print(Solution().index_last_one_recursive('0010010'))  # -> 5




