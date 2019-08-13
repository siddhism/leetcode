# created one, couldn't handle "bbcaac", saw discussions 
# https://leetcode.com/problems/remove-duplicate-letters/discuss/76762/Java-O(n)-solution-using-stack-with-detail-explanation 
# https://leetcode.com/problems/remove-duplicate-letters/discuss/76762/Java-O(n)-solution-using-stack-with-detail-explanation 
# https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        rindex = {c:i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            # print  prev char ', result[-1], 'current pos' , i, 'which is less than ',  rindex[result[-1]]
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
                # print i, c, result
        return result


# print Solution().removeDuplicateLetters('cbacdcbc')

# notes :
# result[-1:] helps us with index error, if last char is not there gives ''
# cbacdcbc # check dry run to understand and read above solutions
# old code 
#         from collections import defaultdict
#         counts = defaultdict(list)
#         for index, c in enumerate(s):
#             counts[c].append(index)
#         for k, v in counts.items():
#             counts[k] = sorted(v, reverse=True)
#         counts = dict(sorted(counts.items()))
#         # pick first occurance of each char
#         # prev = counts[0][0]
#         res = ''
#         alpha = 'abcdefghijklmnopqrstuvwxyz'
#         chars = counts.keys()
#         for i in chars:
#             # import ipdb; ipdb.set_trace()
#             key, value = sorted(counts.items(), key=lambda kv: kv[1])[0]
#             if not value:
#                 continue
#             prev = value[0]
#             res += s[prev]
#             # remove all indexes smaller than prev picked index
#             counts.pop(key)
#             for k, indexes in counts.items():
#                 counts[k] = sorted([item for item in indexes if item > prev])
#             # counts = dict(sorted(counts.items(), key=lambda kv: kv[1]))
#         return res
