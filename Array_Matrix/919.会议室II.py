'''
🍊919.会议室 II
中等  https://www.lintcode.com/problem/919/
给定一系列的会议时间间隔intervals，包括起始和结束时间[[s1,e1],[s2,e2],...] (si < ei)，找到所需的最小的会议室数量。

样例1
输入: intervals = [(0,30),(5,10),(15,20)]
输出: 2
解释: 需要两个会议室
会议室1:(0,30)
会议室2:(5,10),(15,20)

样例2
输入: intervals = [(2,7)]
输出: 1
解释: 只需要1个会议室就够了
'''

# python: 扫描线 

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) <= 1:
            return 0 if not intervals else 1
        times = []
        for t in intervals:
            times.append((t.start, 1))
            times.append((t.end, -1))
        times = sorted(times, key = lambda x: x[0])

        match, need = 0, 1
        cur = 0
        for time in times:
            match += time[1]
            need = max(need, match)
            cur = time[0]
        return need






