#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        if not l1 and not l2:
            return head
        out = head
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val  + carry
            res, carry = s % 10, s / 10
            node = ListNode(res)
            out.next = node
            out = out.next
            l1 = l1.next
            l2 = l2.next

        # if any of the nodes are left
        if l1:
            while l1:
                s = l1.val+carry
                res, carry = s % 10, s / 10
                node = ListNode(res)
                l1 = l1.next
                out.next = node
                out = out.next
        if l2:
            while l2:
                s = l2.val+carry
                res, carry = s % 10, s / 10
                node = ListNode(res)
                l2 = l2.next
                out.next = node
                out = out.next
        if carry:
            node = ListNode(carry)
            out.next = node
            out = out.next
        # since first node is dummpy, return after it
        return head.next


