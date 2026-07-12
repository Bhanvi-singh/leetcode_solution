class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atmost(goal):
            if goal < 0:
                return 0
            n = len(nums)
            L = 0
            R = 0
            currSum = 0
            count = 0
            while R < n:
                currSum += nums[R]
                while currSum > goal:
                    currSum -= nums[L]
                    L += 1
                count += R - L + 1
                R += 1
            return count
        return atmost(goal) - atmost(goal-1)
                
