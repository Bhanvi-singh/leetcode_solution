class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # Memoization
        memo = {}

        def dfs(i, j):
            if i >= j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            ans = 0

            left_sum = 0
            right_sum = prefix[j + 1] - prefix[i]

            for k in range(i, j):

                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                # Left is smaller
                if left_sum < right_sum:

                    # Pruning
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(i, k)
                    )

                # Right is smaller
                elif left_sum > right_sum:

                    # Pruning
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, j)
                    )

                # Equal
                else:
                    ans = max(
                        ans,
                        left_sum + dfs(i, k),
                        right_sum + dfs(k + 1, j)
                    )

            memo[(i, j)] = ans
            return ans

        return dfs(0, n - 1)
 
 