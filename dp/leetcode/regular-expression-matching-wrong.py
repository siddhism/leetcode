# regular-expression-matching
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        i = 0
        j = 0
        # traverse over p and try to match s
        while j < m:
            c = p[j]
            if i == n:
                break
            # print i, j, s[i], c
            if j + 1 < m and p[j] == '.' and p[j+1] == '*':
                # no need to match anything .* will eat remaining string
                i = n
            elif j + 1 < m and p[j+1] == '*':
                # traverse s up until same character comes
                while i < n and s[i] == c:
                    i = i + 1
            elif c == s[i] or c == '.':
                i = i + 1
            j = j + 1
        if j == m -2:
            # only if j -1 is * and last char if any matches the last char of s
            if p[m-1] == '*':
                return True
            if p[m-2] == '*' and p[m-1] == s[-1:]:
                return True
        if j == m -1:
            if p[m-1] == '*':
                return True
        return i == n and j == m


print Solution().isMatch('aa', 'a') == False
print Solution().isMatch('aa', 'a*') == True
print Solution().isMatch('ab', '.*') == True
print Solution().isMatch('aab', 'c*a*b') == True
print Solution().isMatch('mississippi', 'mis*is*p*.') == False
print Solution().isMatch('ab', '.*c') == False
print Solution().isMatch('', '') == True
print Solution().isMatch('aaa', 'aaaa') == False
print Solution().isMatch('aaa', 'a*a') == True
