class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = n + 1
 
        best = [INF] * (n + 1)
 
        seen = {0: 0}

        prefix = 0
        ans = INF

        for i in range(1, n + 1):
            prefix += arr[i - 1]

 
            if prefix - target in seen:
                j = seen[prefix - target]

                length = i - j
                if best[j] != INF:
                    ans = min(ans, best[j] + length)

                best[i] = min(best[i - 1], length)
            else:
                best[i] = best[i - 1]
            if prefix not in seen:
                seen[prefix] = i

        return -1 if ans == INF else ans