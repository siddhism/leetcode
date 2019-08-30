#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# class Node(object):
#     def __init__(self, val, neighbors):
#         self.val = val
#         self.neighbors = neighbors

class Solution(object):

    def dfs(self, node):
        # key is node and value is node copy
        for nxt in node.neighbors:
            if nxt not in self.dic:
                nxt_copy = Node(nxt.val, [])
                self.dic[nxt] = nxt_copy
                self.dic[node].neighbors.append(nxt_copy)
                self.dfs(nxt)
            else:
                self.dic[node].neighbors.append(self.dic[nxt])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict
        if not node:
            return None
        self.dic = {}
        # start a new graph with given node val
        self.clone = Node(node.val, [])
        self.dic[node] = self.clone
        self.dfs(node)
        return self.clone

