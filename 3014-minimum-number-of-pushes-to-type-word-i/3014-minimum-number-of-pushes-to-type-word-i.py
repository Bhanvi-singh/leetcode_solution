class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0
        n = len(word)
        for i in range(n):
            ans += (i // 8) + 1
        return ans