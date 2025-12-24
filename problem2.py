"""
we have a heap of size k and we take the minimum from each list, so we first put the first node from each list and then repeatedly take the smallest one and add it to out result
This takes nlogk time for all the nodes in all the lists since processing pushing and popping takes logk time and we have n such nodes, space is O(K) for number of lists
"""
import heapq
class HeapCompare:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, HeapCompare(node))

        dummy = ListNode(0) #init dummy node
        curr = dummy
        while heap:
            hn = heapq.heappop(heap) #have a heapnode by popping one for the heap
            node = hn.node #establish it as our node that we are processing

            curr.next = node #shift pointers
            curr = curr.next

            if node.next:
                heapq.heappush(heap, HeapCompare(node.next)) #perform same thing again

        return dummy.next