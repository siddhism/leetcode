#
# @lc app=leetcode id=482 lang=python
#
# [482] License Key Formatting
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        x = ''.join(S.split('-'))
        k = K
        y = []
        x = S.replace('-', '').upper()[::-1]
        n = len(x)
        for chunk_start in range(0, n, k):
            # print chunk_start-k, chunk_start
            sub = x[chunk_start:chunk_start+k]
            y.append(sub)
        return '-'.join(y)[::-1]
        
# @lc code=end

print Solution().licenseKeyFormatting("2-5g-3-J", 2)
print Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4)
