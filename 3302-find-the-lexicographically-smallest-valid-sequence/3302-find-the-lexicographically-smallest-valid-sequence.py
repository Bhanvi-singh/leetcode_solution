class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)

        # suf[i] = number of characters of word2
        # that can be matched from word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suf[i] += 1
                j -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed and suf[i + 1] >= m - j - 1:
                ans.append(i)
                j += 1
                changed = True

        return ans if len(ans) == m else []