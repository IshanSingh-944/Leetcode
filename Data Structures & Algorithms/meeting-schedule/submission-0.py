"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, arr: List[Interval]) -> bool:
        arr.sort(key = lambda x:x.start)
        for i in range(1,len(arr)):
            i1 = arr[i-1]
            i2 = arr[i]
            if i1.end > i2.start:
                return False
        return True