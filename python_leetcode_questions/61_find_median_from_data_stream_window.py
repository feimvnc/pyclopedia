""" 
Find median from data stream 

Median is the middle value in an ordered integer list, 
if the size of the list is even, there is no median value, 
so the median is the mean of the two middle values.

Example:
[2,3,4], the median is 3 
[2,3], the median is (2+3) / 2 = 2.5

Design a data structure that supports the following two operations:
- void AddNum(int num) - Add a integer number from the data stream to the data structure 
- double findMedian() - Return the median of all elements so far.
"""
# use built heap, default is minheap, insert is O(logN), pop is O(1)
import heapq     

class Solution:
    def __init__(self):
        """ 
        Initiallize data structure
        """
        # two heaps, small for maxheap, large minheap
        # items in small <= items in maxheap 
        # heaps should be equal size 
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # python default has minheap, multiple -1 to make it a maxheap
        heapq.heappush(self.small, -1 * num)   

        # below operations are O(logn)
        # make sure every num small is <= every num in large 
        if (self.small and self.large and 
                (-1 *  self.small[0]) > self.large[0]):
            # convert to positive in large maxqueue
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        # move from small to large 
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # move from large to small, when len(large) too big > len(small) + 1
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)    # convert to negative for minheap

    def findMedian(self) -> float:
        # max value in small 
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # min value in large 
        if len(self.large) > len(self.small):
            return self.large[0]
        # return median of small max and large min 
        return (-1 * self.small[0] + self.large[0]) / 2 

s = Solution()
s.addNum(1)
s.addNum(2)
print(s.findMedian())    # 1.5
s.addNum(3)
print(s.findMedian())    # 2