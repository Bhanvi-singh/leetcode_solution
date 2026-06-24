class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int 
        :rtype: int
        """
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
 
            if hours <= h:
               high = mid - 1
            else:
               low = mid + 1
        return low
 
