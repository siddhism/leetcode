class Solution(object):
    def traceback(self, result_map, key, n, cache):
        # find the value of this key iteratively until the value
        # is either empty or n
        # print 'called traceback for key ', key
        if cache.get(key) is not None:
            return cache[key]
        result = result_map.get(key)
        if not result:
            cache[key] = False
            return False
        if n-1 in result:
            cache[key] = True
            return True
        # if key is found down in any of the item key
        for key in result:
            # find n at next index
            if self.traceback(result_map, key+1, n, cache):
                cache[key] = True
                return True
        # if none of the path traced it down, return false
        cache[key] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        result_map = {i: [] for i in range(n)}
        cache = {i: None for i in range(n)}
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    result_map[i].append(j)
                    # if j == n-1:
                    #     cache[j] = True
        print result_map
        # start from first result and 
        # track upto all results to see if any of them ends at n
        if not result_map[0]:
            return False
        return self.traceback(result_map, 0, n, cache)

print Solution().wordBreak('catsandog', ['cats', 'cat', 'dog', 'and', 'sand'])
print Solution().wordBreak('catsandog', ['cats', 'cat', 'dog', 'and', 'sand', 'og'])
import time
s = time.time()
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print time.time() - s
