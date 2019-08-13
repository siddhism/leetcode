# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        current = master = ListNode(0)
        lists = [(i.val, i) for i in lists if i]
        heapq.heapify(lists)
        while lists:
            current.next = heapq.heappop(lists)[1] # get min element node
            current = current.next
            if current.next:
                # push the next element from this list to heap
                heapq.heappush(lists, (current.next.val, current.next))
        return master.next
        