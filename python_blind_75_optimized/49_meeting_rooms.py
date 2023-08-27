""" 
Given an array of meeting time intervals consisting of start and end times
[[s1, e1],[s2,e2],...](si<ei), determine if a person could attend all meetings.

Example:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false 
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start 
        self.end = end 

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                print(f'overlapping, {i1.end=}, {i2.start=}')
                return False 
        return True 


intervals = [Interval(0,5),Interval(5,10),Interval(15,20)]
print(Solution().canAttendMeetings(intervals))

intervals2 = [Interval(0,30),Interval(5,10),Interval(15,20)]
print(Solution().canAttendMeetings(intervals2))


# python 49_meeting_rooms.py 
# True
# overlapping, i1.end=30, i2.start=5
# False