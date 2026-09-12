class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)

        arr = sorted(
            (l, r, w, idx)
            for idx, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in arr]
        memo = {}

        def solve(i, k):
            if i >= n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            # Skip current interval
            score1, indices1 = solve(i + 1, k)

            l, r, w, idx = arr[i]

            # Next interval must start strictly after r
            j = bisect_right(starts, r)

            # Take current interval
            score2, indices2 = solve(j, k - 1)
            score2 += w

            indices2 = tuple(sorted((idx,) + indices2))

            if score2 > score1:
                ans = (score2, indices2)
            elif score1 > score2:
                ans = (score1, indices1)
            else:
                # Lexicographically smaller
                ans = (score1, min(indices1, indices2))

            memo[(i, k)] = ans
            return ans

        return list(solve(0, 4)[1])
 