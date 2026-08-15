class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        xor = 0
        has_nonzero = False

        for num in nums:
            xor ^= num

            if num != 0:
                has_nonzero = True

        if xor != 0:
            return n

        if has_nonzero:
            return n - 1

        return 0