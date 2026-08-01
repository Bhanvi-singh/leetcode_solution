class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = []
        n = len(nums)
        def solve(l, r):
            if l == r:
                return nums[l]
            lc = nums[l] - solve(l + 1, r)
            rc = nums[r] - solve(l, r - 1)
            return max(lc, rc)
        ans = solve(0, n - 1)
        if ans >= 0:
            return True
        else:
            return False
