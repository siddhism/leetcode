#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create counts of chars and check count values in sorted order
        from collections import defaultdict
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        replace_map = {}
        n = len(s)
        for i in range(n):
            cs = s[i]
            ct = t[i]
            # print cs, ct, replace_map
            if cs in replace_map:
                if replace_map[cs] != ct:
                    return False
                continue
            else:
                # this is first time of this string
                # map it to ct so that further string can be replaced
                if ct in replace_map.values():
                    # no two chars should be mapped to same key
                    return False
                replace_map[cs] = ct
        return True



