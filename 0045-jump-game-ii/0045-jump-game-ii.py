class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        farthest = 0
        jump = 0
        currend = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == currend:
                jump += 1
                currend = farthest
        return jump