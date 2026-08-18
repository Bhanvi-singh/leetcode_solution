class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = {}

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                freq[x] = freq.get(x, 0) + 1

        ans = -1

        for x in freq:
            if freq[x] == 1:
                ans = max(ans, x)

        return ans