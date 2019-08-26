class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        from collections import defaultdict
        gmap = defaultdict(int) # greed
        smap = defaultdict(int) # suppy
        for item in g:
            gmap[item] += 1
        for item in sorted(s):
            smap[item] += 1
        # we will start with supply
        result = 0
        gmap = dict(sorted(gmap.items(), key=lambda kv: kv[1]))
        smap = dict(sorted(smap.items(), key=lambda kv: kv[0]))
        print gmap, smap
        for gk, demand in gmap.items():
            # get min key in smap which is equal or greater than this
            sup_key_space = [item[0] for item in smap.items() if item[0] >= gk and item[1] > 0]
            if not sup_key_space:
                continue
            sup_key = min(sup_key_space)
            sup = smap[sup_key]
            if demand <= sup:
                # supply all the demand
                result += demand
                gmap[gk] = 0
                smap[sup_key] -= demand
                # drop this portion
                # gmap.pop(gk)
            else:
                diff = demand - sup
                result += diff
                gmap[gk] -= diff
                smap[sup_key] -= diff
            print gmap, smap
        return result

print Solution().findContentChildren([1,5], [1,2,3])
print Solution().findContentChildren([1,2], [1,2,3])
print Solution().findContentChildren([1,2,3], [1,1])
print Solution().findContentChildren([10,9,8,7,10,9,8,7], [10,9,8,7])
print Solution().findContentChildren([1,2,3],[3])
