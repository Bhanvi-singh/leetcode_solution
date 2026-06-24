class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1 
        def possible (day):
            bouquets = 0
            count = 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                else:
                    bouquets += count // k
                    count = 0
            bouquets += count // k
            return bouquets >= m
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
              
         
        