from collections import defaultdict

class Solution(object):
    def get_count_chars(self, str):
            count = defaultdict(int)
            # get val 1-26
            for c in str:
                # val = ord(c) - 97
                # result += val * val
                count[c] += 1
            return count
        
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for str in strs:
            s = ''.join(sorted(str))
            result[s].append(str)
        return result.values()

print Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])