#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        from collections import defaultdict
        last_index = {}
        running_count = 0
        for i, c in enumerate(s):
            # if present in map, get it or cur index is prev_index (last seen at)
            prev_index = last_index.get(c) or i
            running_count += 1
            if running_count > max_len:
                max_len = running_count
            if c in last_index:
                # means it is within our running count
                # reset running count to last seen + 1
                running_count = i - prev_index
            last_index[c] = i
            print (i, c, running_count)
        return max_len        
# @lc code=end

