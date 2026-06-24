class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
           return x
        low = 1
        high = x
        
        while low <= high:
            mid = (low + high ) // 2
            if mid * mid == x:
              return mid
            elif mid * mid < x:
              
                 low = mid + 1
            else:
                high = mid - 1
        return high