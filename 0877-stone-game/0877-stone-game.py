class Solution(object):
    def stoneGame(self, piles):
        return True
        """
        :type piles: List[int]
        :rtype: bool
        """
#  brute
    #  """   ans = []
    #     n = len(piles)
    #     def solve(l, r):
    #         if l > r:
    #             return  0
    #         parity = (r - l - n) % 2
    #         if parity == 1:

    #             lc = piles[l] - solve(l + 1, r)
    #             rc = piles[r] - solve(l, r - 1)
    #             return max(lc, rc)
    #         else:
    #             lc = -piles[l] - solve(l + 1, r)
    #             rc = -piles[r] - solve(l, r - 1)
    #             return max(lc, rc)

    #     ans = solve(0, n - 1)
    #     if ans >= 0:
    #         return True
    #     else:
    #         return False"""