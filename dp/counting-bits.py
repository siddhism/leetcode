class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x = [0, 1]
        i = 2
        chunk = 2
        while i < num:
            print 'i ', i, ' chunk ', chunk
            print ' looping j from ', i, i * 2
            for j in range(i, i * 2):
                temp = x[j-chunk] + 1       
                x.append(temp)
            chunk = chunk * 2
            i = i * 2
        return x
        
print Solution().countBits(17)