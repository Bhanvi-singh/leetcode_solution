class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        l = [1] * n
        r = [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[ i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r[i] = r[ i + 1] + 1
        ans = 0
        for i in range(n):
            ans += max(l[i], r[i])
        return ans


