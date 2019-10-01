#
# @lc app=leetcode id=987 lang=python
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict, deque
        x_val_map = defaultdict(list)

        if not root:
            return []

        queue = deque()
        # root node is at x = 0, y = 0
        queue.appendleft((root, 0, 0))

        while len(queue) > 0:
            node, x, y = queue.popleft()
            if not node:
                continue

            # map the x value w.r.t value of level, that's first sorting order, second is node's value (if level is same)
            x_val_map[x].append((-y, node.val))
            # append all it's child with level x - 1 and x + 1
            queue.appendleft((node.left, x-1, y-1))
            queue.appendleft((node.right, x+1, y-1))
        
        # sort the hashmap in order of x
        min_key = min(x_val_map.keys())
        max_key = max(x_val_map.keys())
        result = []
        for key in range(min_key, max_key+1):
            nodes = x_val_map.get(key)
            if nodes:
                nodes = sorted(nodes)
                # print nodes
                node_vals = [item[1] for item in nodes]
                result.append(node_vals)
        
        return result


# @lc code=end

