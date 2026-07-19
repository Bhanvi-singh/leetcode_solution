class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for curr in intervals:
            if curr[1] <  newInterval[0]:
                ans.append(curr)
            elif  newInterval[1] < curr[0]:
                ans.append(newInterval)
                newInterval = curr
            else:
                newInterval[0] = min( newInterval[0], curr[0])
                newInterval[1] = max( newInterval[1], curr[1])
        ans.append(newInterval)
        return ans

        