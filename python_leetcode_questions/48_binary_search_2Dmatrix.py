""" 
Write an efficient algorithm that search a value in m x n matrix.
-Integers in each row are sorted from left to right 
-The first integer of each row is greater than the last integer of the previous row

Input: matrix = [[1,2,5,7],[10,11,16,20],[23,30,34,60]], target=3
Output: True

"""

from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not len(matrix) or not len(matrix[0]):    # empty matrix return False
            return False 

        ROWS, COLS = len(matrix), len(matrix[0])    # set the dimensions of rows, cols

        # first portion of binary search 
        # check and identify rows first 
        top, bot = 0, ROWS-1     #  top row, bottom row 
        while top <= bot:
            row = (top + bot) // 2 
            if target > matrix[row][-1]:     # check last value 
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1 
            else:      # target fall within the row, break, row found  
                break 

        if not (top <= bot):     # target not found anywhere
            return False 

        # second portion of binary search 
        row = (top + bot) // 2 
        l, r = 0, COLS - 1 
        while l <= r:
            m = (l+r) // 2 
            if target > matrix[row][m]:
                l = m + 1 
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True    # target is found 
        
        return False     # not found after all search 


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3

print(Solution().searchMatrix(matrix, 3))
