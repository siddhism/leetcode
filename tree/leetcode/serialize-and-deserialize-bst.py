# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def level_order(root):
            node = root
            queue = []
            queue.append(node)
            while len(queue) > 0:
                node = queue[0]
                queue = queue[1:]
                print (node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return queue
        data = level_order(root)
        return ','.join(map(str,data))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = []
        for item in data.split(','):
            if item!='None':
                values.append(int(item))
            else:
                values.append(None)
        print 'data here ', values
        data = values
        # root = TreeNode(data[0])
        n = len(data)
        def construct(i):
            if i >= n:
                return
            if not data[i]:
                return
            left = construct(2*i+1)
            right = construct(2*i+2)
            node = TreeNode(data[i])
            node.left = left
            node.right = right
            return node
        root = construct(0)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))