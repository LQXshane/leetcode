# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, time_range):
        if not intervals or len(intervals)==0: return time_range
        intervals.sort(key=lambda x: x.start)
        res = []
        cur=Interval(intervals[0].start,intervals[0].end)
        if cur.start>time_range.start: res.append(Interval(time_range.start,min(time_range.end,cur.start)))
        for i in range(1,len(intervals)):
            if intervals[i].start>=time_range.end: break
            if cur.end >= intervals[i].start:
                cur.end=max(intervals[i].end,cur.end)
                if cur.end>=time_range.end:break
            else:
                if intervals[i].start>time_range.start:
                    res.append(Interval(max(time_range.start,cur.end),min(time_range.end,intervals[i].start)))
                cur.start=intervals[i].start
                cur.end=intervals[i].end
        if cur.end<time_range.end:res.append(Interval(cur.end,time_range.end))
        return res
