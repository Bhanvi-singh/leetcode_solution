class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        ans  = sys.maxsize
        n = len(nums)
        low = 0 
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans
            

