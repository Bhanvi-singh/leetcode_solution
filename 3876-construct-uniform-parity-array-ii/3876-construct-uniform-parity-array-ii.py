class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # n = len(nums1)
        # l = 0
        # r = n - 1
        # while l < r:
        #     if nums1[l] % 2 != 0 and nums1[r] % 2 != 0:
        #         l += 1
        #         r -= 1
        #     elif  nums1[l] % 2 == 0 and nums1[r] % 2 == 0:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True
        n = len(nums1)

        mn = min(nums1)

        if mn % 2 != 0:
            return True
        for num in nums1:
            if num % 2 != 0:
                return False
        return True