class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach = 0
        n = len(nums)
        for i in range(n):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + nums[i])
        return True
                