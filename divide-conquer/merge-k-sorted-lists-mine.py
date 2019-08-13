# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_index(self, lists, key):
        n = len(lists)
        if not lists:
            return 0
        for i,list in enumerate(lists):
            if list and list.val == key:
                return i
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        heads = [list for list in lists]
        data = [head.val for head in heads]
        min_key = min(data)
        master = ListNode(None)
        answer = ListNode(min_key)
        master = answer
        min_key_index = self.get_index(heads, min_key)
        while True:
            data = [head.val for head in heads if head is not None]
            if not data:
                break
            min_key = min(data)
            min_key_index = self.get_index(heads, min_key)

            print min_key_index
            if heads[min_key_index]:
                node = ListNode(heads[min_key_index].val)
                answer.next = node
                answer = answer.next
                heads[min_key_index] = heads[min_key_index].next
            else:
                break
        return master.next
        