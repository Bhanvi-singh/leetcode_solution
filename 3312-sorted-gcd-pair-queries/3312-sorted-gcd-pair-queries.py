class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs having gcd exactly g
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0

            # Count numbers divisible by g
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            # Remove pairs already counted with larger gcd
            for multiple in range(2 * g, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        # Prefix count of sorted gcd values
        prefix = []
        values = []
        total = 0

        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans