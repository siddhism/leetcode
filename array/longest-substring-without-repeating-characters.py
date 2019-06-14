class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        sub = ''
        prev_index = 0
        count = 0
        i = 0
        while i < len(s):
            c = s[i]
            # print 'current char ', c
            if c in sub:
                max_len = max(max_len, count)
                count = 1
                # reset where to start counting from again
                prev_index = s.index(c, prev_index)
                prev_index = prev_index + 1
                sub = s[prev_index] # restart sub
                i = prev_index + 1
                # print (' reset index to ', i)
            else:
                sub += c
                count += 1
                i = i + 1
            print sub
        return max(max_len, len(sub))

print Solution().lengthOfLongestSubstring('pwwkew')
