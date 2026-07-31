class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = Counter(word)

        counts = sorted(freq.values(), reverse=True)

        ans = 0

        for i in range(len(counts)):
            pushes = (i // 8) + 1
            ans += counts[i] * pushes

        return ans