class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0, i):
                # lookup all prev char if any of them are in worddict
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break # break the internal loop, one cond is enough to mark this index
        # for i in range(len(s)):
        #     print s[i], dp[i]
        return dp[n]

print Solution().wordBreak('applepenapple', ['apple', 'pen'])
print Solution().wordBreak('catsandog', ['cats', 'cat', 'dog', 'and', 'sand'])
print Solution().wordBreak('catsandog', ['cats', 'cat', 'dog', 'and', 'sand', 'og'])
import time
s = time.time()
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print time.time() - s
