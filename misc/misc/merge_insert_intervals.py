# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i].start <= newInterval.end:
            newInterval = Interval(min(newInterval.start, intervals[i].start), \
                                max(newInterval.end, intervals[i].end))
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
