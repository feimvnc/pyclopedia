""" 
Knapsack 0-1 problem soving using recursive and dynamic programming 
Giving list of weights and values, total items, and capacity, find the max values.
"""
class Solution:
    # Use single char var name for easy understanding purpose here 
    def knapsack_recursive(self, n, w, v, c):
        """
        Args:
            n (int): total number of item allowed to put in the knapsack
            w (list): weights
            v (list): values
            c (int): total capacity allowed

        Returns:
            int: max value
        """
        
        # recursive method 
        def ks(n, c):
            if n==0 or c == 0:                 # 1. base case, no item or no capacity left
                result = 0 
            elif w[n] > c:                     # 2. ignore, weight bigger than capacity left
                result = ks(n-1, c)
            else:
                tmp1 = ks(n-1, c)              # prev value to compare against new item value
                tmp2 = v[n] + ks(n-1, c-w[n])  # 3. include new item value + ([prev_count] - total_capacity - current_capacity )
                result = max(tmp1, tmp2)
            return result 

        return ks(n,c)                         # call ks

    # dynamic programming, memorize intermediate results
    def knapsack_dp_memo(self, n, w, v, c):
        # Initialize 2D array to store weight and value table
        # The order of w and n must match the positions used in the ks_dp function arr[n][c]
        arr = [[None for _ in range(c+1)] for _ in range(len(w)) ]

        def ks_dp(n, c):
            if arr[n][c] != None: return arr[n][c]
            if n==0 or c == 0:                 # 1. base case, no item or no capacity left
                result = 0 
            elif w[n] > c:                     # 2. ignore, weight bigger than capacity left
                result = ks_dp(n-1, c)
            else:
                tmp1 = ks_dp(n-1, c)              # prev value to compare against new item value
                tmp2 = v[n] + ks_dp(n-1, c-w[n])  # 3. include new item value + ([prev_count] - total_capacity - current_capacity )
                result = max(tmp1, tmp2)
            arr[n][c] = result
            return result 

        return ks_dp(n,c)                         # call ks


w = [0,1,2,4,2,5]
v = [0,5,3,5,3,2]
c = 10
n = 5 

print(Solution().knapsack_recursive(n, w, v, c))
print(Solution().knapsack_dp_memo(n, w, v, c))

# python knapsack_recursive_dp.py 
# 16
# 16