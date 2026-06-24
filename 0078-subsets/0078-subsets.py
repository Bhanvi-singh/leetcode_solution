class Solution(object):
    def subsets(self, nums):
        result = []
        """
        :type nums: List[int]
        :rtype: List[List[int]]
   """
        def func(index, subset, result):
            if index >= len(nums):
                result.append(subset[:]) 
                return
            subset.append(nums[index])       
            func(index + 1, subset, result)
            subset.pop()
            func(index + 1, subset, result)
        func(0, [], result)
        return result