""" 
Given year and month, print days of the month

Example:
Input: 2018 2
Output: 28 

Input: 2020 2
Output: 29

Input: 2019 1
Output: 31
"""

class Solution:

    def find_month_days(self, year: int, month: int) -> int:
        
        # leap year, 2 need to plus 1 more day
        y_d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}

        def is_leap_year(year: int):
            return (year % 4 == 0 and year % 100 !=0) or year % 400 ==0
 
        if month == 2 and is_leap_year(year):
            return y_d[2]+1

        return y_d[month]


print(Solution().find_month_days(2018, 2))
print(Solution().find_month_days(2020, 2))
print(Solution().find_month_days(2019, 2))

# 28
# 29
# 28

