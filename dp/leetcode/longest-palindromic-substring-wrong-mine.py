class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        n = len(s)
        max_len = defaultdict(int)
        for i, c in enumerate(s):
            max_len[i] = 1
        # import ipdb; ipdb.set_trace()
        for i in range(1, n):
            prev_match_index = max_len.get(i-1)
            # compare_index = i - 1 -prev_match_index
            compare_index = prev_match_index - i - 1
            # print 'max_len ', max_len.items()
            # print i, i-1, 'prev_match_index ', prev_match_index, compare_index
            if compare_index >= 0 and s[compare_index] == s[i]:
                max_len[i] = max_len[i-1] + 2
            elif compare_index + 1 >= 0 and s[compare_index + 1] == s[i]:
                max_len[i] = max_len[i-1] + 1
            elif s[i] == s[i-1]:
                # if not ideal palindrome, it can be palindrome with prev char
                max_len[i] = 2
            else:
                # same max length stays 1
                max_len[i] = max_len[i-1]
        # if s[n-1] == s[n-2]:
        #     max_len[n-1] = max(max_len[n-1], max_len[n-2] + 1)
        # get max value of key 
        # babab {0:1, 1:1, 2:3, 3:3: 4:5}
        # babac {0:1, 1:1, 2:3, 3:3: 4:1}
        max_k, max_v = 0, max_len[0]
        max_v = max(max_len.values())
        for k, v in max_len.items():
            if v == max_v:
                max_k = k
                break
        # print max_k, max_v, max_len
        # print max_k-max_v+1, max_k + 1
        return s[max_k-max_v+1:max_k+1]
        # return max_len[n-1]

print Solution().longestPalindrome("cbbd")
print Solution().longestPalindrome("babab")
print Solution().longestPalindrome("babad")
print Solution().longestPalindrome("bab")
print Solution().longestPalindrome("a")
print Solution().longestPalindrome("ccc")
print Solution().longestPalindrome("abadd")
