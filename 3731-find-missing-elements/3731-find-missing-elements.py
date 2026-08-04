class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        ans = []       
        for i in range(n - 1):
            for j in range(nums[i] + 1, nums[i + 1]):
                ans.append(j)
        return ans