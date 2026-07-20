class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def getend(interval):
            return interval[1]
        intervals.sort(key = getend)
        remove = 0
        prevend  = intervals[0][1]
        for curr in intervals[1:]:
            if curr[0] >= prevend:
                prevend = curr[1]
            else:
                remove += 1
        return remove