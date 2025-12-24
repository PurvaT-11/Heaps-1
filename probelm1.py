"""
We maintain a heap of size k, so the top element will be our kth largest element. We iterate through each element and analyse its position towards the heap. so TC is O(nlogk) as pushing
and popping from heap takes logk time for n elements and space taken would be o(K)
"""


import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]