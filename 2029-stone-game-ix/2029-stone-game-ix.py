class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Remove pairs of remainder-0 stones
        if cnt[0] % 2 == 0:
            cnt[0] = 0
        else:
            cnt[0] = 1

        # Alice can start with remainder 1 or remainder 2
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        if cnt[0] == 0:
            return cnt[1] > 0 and cnt[2] > 0

        return abs(cnt[1] - cnt[2]) > 2