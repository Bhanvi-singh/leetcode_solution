class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            if k < 0:
                return 0 
            n = len(nums)
            L = 0
            R = 0
            ans = 0
            odd = 0
            while R <  n:
                if nums[R] % 2 != 0:
                    odd += 1
                while odd  > k:
                    if nums[L] % 2 != 0:
                        odd -= 1
                    L += 1
                ans += (R - L + 1)
                R += 1
            return ans
        return atmost(k) - atmost(k - 1)
                