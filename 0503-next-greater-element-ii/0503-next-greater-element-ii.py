class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
         
        n = len(nums)
        ans =  [-1] * n
        for i in range(2 * n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if i< n:
                if stack:
                    ans[i] = nums[stack[-1]]
            stack.append(i % n)
        return ans 
        