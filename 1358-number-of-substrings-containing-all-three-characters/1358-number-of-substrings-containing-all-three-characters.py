class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = { 'a' : 0,'b': 0,'c': 0}
        l = 0
        r = 0
        ans = 0
        n = len(s)
        while r < n:
            freq[s[r]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                ans += n - r
                freq[s[l]] -= 1
                l += 1
            r += 1
        return ans
