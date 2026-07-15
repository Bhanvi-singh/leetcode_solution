class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicate = -1
        missing = - 1
        s = set()
        for num in nums:
            if num in s:
                duplicate = num
            else:
                s.add(num)

        for i in range(1,n+1):
            if i not in s:
                missing = i

        return[duplicate,missing]