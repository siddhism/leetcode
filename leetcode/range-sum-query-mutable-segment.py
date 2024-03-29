class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.total = root.left.total + root.right.total
            return root.total
        return updateVal(self.root, i, val)

        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        return rangeSum(self.root, i, j)
