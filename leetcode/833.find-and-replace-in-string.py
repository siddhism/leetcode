#
# @lc app=leetcode id=833 lang=python
#
# [833] Find And Replace in String
#

# @lc code=start
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        n = len(indexes)
        lookups = {indexes[i] : (sources[i], targets[i]) for i in range(n)}
        result = ""
        i = 0
        while i < len(S):
            # either at this index in source, something will be replaced or not
            if i in lookups and S[i:].startswith(lookups[i][0]):
                result += lookups[i][1]
                i += len(lookups[i][0]) # source index up
            else:
                result += S[i]
                i += 1
        return result

# @lc code=end

print Solution().findReplaceString(
    "abcd",
    [0, 2],
    ["a", "cd"],
    ["eee", "ffff"]
)