class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        for curr in intervals:
            if not ans or ans[-1][1] < curr[0]:
                ans.append(curr)
            else:
                ans[-1][1] = max(ans[-1][1], curr[1])
        return ans
        