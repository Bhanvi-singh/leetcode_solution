class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)

        # value + original index
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find one group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Values of this group
            values = [arr[i][0] for i in range(start, end + 1)]

            # Original indices of this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Put smallest values at smallest indices
            for i in range(len(values)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans