from typing import List 

class Solution:
    def maxProfit(self, prices: List[int])->int:
        l, r = 0, 1 
        maxP = 0 
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP, profit)
            else: 
                l=r 
            r += 1
        return maxP 

# print(Solution().maxProfit([7,1,5,3,100,4]))
if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4])==5, 'failed'
    print("correct")
    
    assert Solution().maxProfit([[7,1,5,3,6,4]])==6, "error"
    print("correct")