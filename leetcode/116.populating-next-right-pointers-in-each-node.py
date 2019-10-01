#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        from collections import deque
        lo = deque()
        # level order traversal with info of is left
        lo.append((root, True))
        result = []
        # for every node, put both left and right to queue and pop two at once
        while lo:
            top, is_right_child = lo.popleft()
            if not top:
                continue
            result.append(top)
            lo.append((top.left, False))
            if is_right_child and top.right:
                # if it's right of right
                lo.append((top.right, True))
                lo.append((None, False))
                result.append(None)
            elif top.right:
                lo.append((top.right, False))

        x = []
        for item in result:
            if item:
                x.append(item.val)
            else:
                x.append(None)
        print (x)

        n = len(result)
        for i in range(1, n-1):
            cur = result[i]
            nxt = result[i+1]
            if cur:
                cur.next = nxt

        return root

        

