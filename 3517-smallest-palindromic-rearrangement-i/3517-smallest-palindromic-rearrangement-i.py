class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        # first = f, middle = m
        f = ""
        m = ""
        for ch in sorted(freq):
            f  += ch * (freq[ch] // 2)
            if freq[ch] % 2 == 1:
                m = ch
        return f + m + f[::-1]