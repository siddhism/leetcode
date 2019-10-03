#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        n = len(secret) # length of secret and guess are equal
        from collections import defaultdict
        secret_map = defaultdict(int)
        guess_map = defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            cs = secret[i]
            secret_map[cs] += 1
            cg = guess[i]
            guess_map[cg] += 1

        # count all common chars
        cows = 0
        for i in range(0, 10):
            c = str(i)
            a = secret_map[c]
            b = guess_map[c]
            ans = min(a, b)
            cows += ans
        # print 'total matches ', cows
        cows = cows - bulls
        # print ('bulls ', bulls, ' cows ', cows)
        return '{}A{}B'.format(bulls, cows)


        
# @lc code=end

print Solution().getHint('1807', '7810')

