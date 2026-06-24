class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        mpp  = {}
        n = len(nums)
        for i in range (n):
           
            more = target - nums[i]
            if  more in mpp:
                 return [mpp[more], i]
            mpp [nums[i]] = i

