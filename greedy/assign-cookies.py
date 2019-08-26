class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        from collections import defaultdict
        g.sort()
        s.sort()
        childi = 0 # no. of happy childs
        cookiei = 0 # no. of cookies consumed

        while cookiei < len(s) and childi < len(g):
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1 # since one cookie is assigned to one person
        return childi

print Solution().findContentChildren([1,5], [1,2,3])
print Solution().findContentChildren([1,2], [1,2,3])
print Solution().findContentChildren([1,2,3], [1,1])
print Solution().findContentChildren([10,9,8,7,10,9,8,7], [10,9,8,7])
print Solution().findContentChildren([1,2,3],[3])
