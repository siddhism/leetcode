#
# @lc app=leetcode id=158 lang=python
#
# [158] Read N Characters Given Read4 II - Call multiple times
#

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf, n):
        i = 0
        while i < n:
            buf4 = [''] * 4 
            _ = read4(buf4) 
            # add the read up chars from buffer to queue
            self.queue.extend(buf4)
            count = min(len(self.queue), n-i) 
            print ('current queue ', self.queue)
            print ('i ', i, ' n ', n, 'min of ', len(self.queue), ' and ', n - i, ' is count', count)
            if not count:
                break
            for _ in xrange(count):
                buf[i] = self.queue.popleft()
                i+=1
        print buf[:n]
        return i
        
