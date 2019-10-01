#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#
class Solution(object):
    def match_str(self, s, t):
        # from collections import Counter
        # count_main = Counter(list(s))
        # count_t = Counter(list(t))
        # return dict(count_main).items() <= dict(count_t).items()
        # s = ''.join(sorted(list(s)))
        # t = ''.join(sorted(list(t)))
        from collections import defaultdict
        cache_s = defaultdict(int)
        cache_t = defaultdict(int)
        for i, c in enumerate(s):
            cache_s[c] += 1
        for i, c in enumerate(t):
            cache_t[c] += 1
        # print cache_s, cache_t
        # for each char in t, if cache_t count is == cache_s for char, return true
        for k, v in cache_t.items():
            if cache_s[k] < v:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        r = 0
        # result = ''
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        while r < len(s):
            # print l, r
            while not self.match_str(s[l:r+1], t) and r < len(s):
                r = r + 1
            # we are in desirable state, move left to + 1
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            l += 1
            while self.match_str(s[l:r+1], t) and l < len(s):
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                l += 1
            # left is exhausted now, increase r
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]


# print Solution().minWindow('ADOBECODEBANC', 'AABC')
# print Solution().minWindow('ADOBECODEBANC', 'ABC')
# print Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
# print Solution().minWindow("aaaaaaaaaaddcabbbbbcdd","abcdd")
# print Solution().minWindow("aaaaaaaaaaddcabbbbbcdd","abcdd") == 'ddcab'
print Solution().minWindow('a','aa')
# print Solution().minWindow('a','a')
