"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        solution = []
        intervals.sort(key = lambda s: s.start) 
        for i in intervals:
            if not solution or solution[-1].end < i.start:
                solution.append(i)
            else:
                solution[-1].end = max(solution[-1].end, i.end)    
        return solution
