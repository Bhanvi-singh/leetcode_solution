class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # brute code
        """" while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(x - y)
        if len(stones) == 0:
            return 0
        return stones[-1]"""
        # optimal code
        heap = []
        for  stone in stones:
            heap.append(-stone)
        import heapq
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,x - y)
        if len(heap) == 0:
            return 0
        return -heap[0] 
