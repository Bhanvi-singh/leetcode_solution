class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1,n + 1):
            if i >= 1000:
                ans +=1
        return ans
        