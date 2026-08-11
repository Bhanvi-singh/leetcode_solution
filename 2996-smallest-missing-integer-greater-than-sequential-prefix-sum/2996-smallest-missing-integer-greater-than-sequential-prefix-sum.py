class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
        
        while s in nums:
            s += 1
        
        return s