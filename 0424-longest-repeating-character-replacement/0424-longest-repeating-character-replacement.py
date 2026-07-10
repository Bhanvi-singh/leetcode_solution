class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L = 0
        R = 0
        ans = 0
        freq = {}
        maxfreq= 0
        n = len(s)
        while R < n:
            freq[s[R]] = freq.get(s[R], 0) + 1
            maxfreq = max(maxfreq, freq[s[R]])
            while (R - L + 1) - maxfreq > k:
                freq [s[L]] -= 1
                L += 1
            ans = max(ans , R - L + 1)
            R += 1
        return ans
            