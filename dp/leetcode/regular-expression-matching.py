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
        dp = [[False for i in range(m+1)] for _ in range(n+1)]

        # empty pattern can only match empty string
        if m ==  0:
            return n == 0

        dp[0][0] = True
        # empty string and pattern
        # Only '*' can match with empty string 
        for j in range(1, m):
            if p[j-1] == '*':
                if dp[0][j-1] or (j > 1 and dp[0][j - 2]):
                    dp[0][j] = dp[0][j-1]

        # fill the table in bottom up manner
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] != s[i-1] and j > 1 and p[j-2] != '.':
                        # * contributes zero characters
                        dp[i][j] = dp[i][j-2]
                    else:
                        # in this case, a* counts as multiple a
                        # or, a* counts as single a
                        # or, a* counts as zero empty
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or (j> 1 and dp[i][j-2])
        return dp[n][m]




print Solution().isMatch('aa', 'a') == False
print Solution().isMatch('aa', 'a*') == True
print Solution().isMatch('ab', '.*') == True
print Solution().isMatch('aab', 'c*a*b') == True
print Solution().isMatch('mississippi', 'mis*is*p*.') == False
print Solution().isMatch('ab', '.*c') == False
print Solution().isMatch('', '') == True
print Solution().isMatch('aaa', 'aaaa') == False
print Solution().isMatch('aaa', 'a*a') == True
