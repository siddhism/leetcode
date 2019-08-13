# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         # self.level = 0

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        level = 0
        queue.append((root, 0))
        values = []
        # values.append((root.val, level))
        while queue:
            node, level = queue[0]
            values.append((node.val, level))
            queue = queue[1:]
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        # print queue
        zigzag = []
        prev_level = 0
        level = 0
        current = []
        for item, level in values:
            # print item, level
            if level == prev_level:
                current.append(item)
            else:
                print ' current : ', current, ' level ', level
                if level % 2 == 0:
                    zigzag.append(list(reversed(current)))
                else:
                    zigzag.append(current)
                current = []
                current.append(item) # append first item as well
                prev_level = level 
                # print 'changing level', level, ' current ', current
        print ' current : ', current, ' level ', level
        if level % 2 == 0:
            zigzag.append(list(reversed(current)))
        else:
            zigzag.append(current)
        return zigzag