class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        count = 0
        l = 0
        r = 0
        while l < n and r < m:
            if g[l] <= s[r]:
                count += 1
                l += 1
            r += 1
        return count
                

       
      