class DSU(object):
    def __init__(self, nums):
        self.len = len(nums)
        self.roots = dict((item, item) for item in nums)

    def parent(self, x):
        # print 'finding parent for x ', x
        while self.roots[x] != x:
            x = self.roots[x]
        return x

    def union(self, a, b):
        parent_a = self.parent(a)
        parent_b = self.parent(b)
        self.roots[parent_a] = parent_b


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        uf = DSU(nums)
        # initialize roots of DSU
        roots = [item for item in nums]
        for i in range(n):
            for j in range(i):
                diff = abs(nums[i] - nums[j])
                if diff <= n:
                    # print ' calling union for ', nums[i], nums[j]
                    uf.union(nums[i], nums[j])
                
        # calculate num of edges in root
        from collections import defaultdict
        counts = defaultdict(int)
        for k,v in uf.roots.items():
            counts[v] += 1
        counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
        return counts[0][0]


print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])