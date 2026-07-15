class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mp = {}
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        for i in range(n):
            if sorted_nums[i] not in mp:
                mp[sorted_nums[i]] = i
        ans = []
        for num in nums:
            ans.append(mp[num])
        return ans