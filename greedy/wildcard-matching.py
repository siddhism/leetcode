class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pl = len(p)
        sl = len(s)
        j = 0
        i = 0
        match = True
        while i < pl and j < sl:
            # print 'i ', i, ' p[i] ', p[i], ' j ', j, ' s[j] ',s[j]  
            if s[j] == p[i]:
                i += 1
                j += 1
            elif p[i] == '*':
                if i-1>0 and p[i-1] == '?':
                    i += 1
                    continue
                if i + 1 < pl:
                    nxt = p[i+1]
                    # find nxt in s
                    idx = s.rfind(nxt)
                    if idx == -1:
                        # not found means entire string covered
                        return True
                    j = idx+1 # jump s
                    i = i + 2
                else:
                    return True
            elif p[i] == '?':
                j = j + 1
                i = i + 1
            else:
                return False
                # nothing could be matched
                # match = False
                # i = i + 1
                # j = j + 1
        # print 'j ', j, ' sl ', sl
        if j == sl and i == pl:
            return True
        return False

# print Solution().isMatch('aa', 'a*')
# print Solution().isMatch('aa', '*')
# print Solution().isMatch('cb', '?a')
# print Solution().isMatch('adceb', '*a*b')
# print Solution().isMatch('acdcb', 'a*c?b')

# print Solution().isMatch("mississippi", "m??*ss*?i*pi")
