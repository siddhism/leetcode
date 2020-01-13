#
# @lc app=leetcode id=269 lang=python
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        level_table = defaultdict(list)
        rev_map = defaultdict(int)
        for word in words:
            for i, c in enumerate(word):
                if c in level_table[i]:
                    for j in range(i+1):
                        if c in level_table[j] and level_table[j].index(c):
                            print c, i
                if c not in level_table[i]:
                    level_table[i].append(c)
        # sort the level table
        level_table = sorted(level_table.items(), key = lambda kv: kv[0])

        # print (level_table)
        # join the table
        output = []
        for k, v in level_table:
            for char in v:
                if char not in output:
                    output.append(char)
        return ''.join(output)
                
        
# @lc code=end

print Solution().alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])

print Solution().alienOrder([
    "z",
    "x",
    "z"
])