class Solution(object):
    def findKthLargest(self, nums, k):

        """nums.sort(reverse=True)
        return nums[k-1]"""
        # heap solution
        heap = []
        for num in nums:
            heap.append(-num)
        import heapq
        heapq.heapify(heap)
        for i in range(k -1):
            heapq.heappop(heap)
        answer = heapq.heappop(heap)
        return -answer

