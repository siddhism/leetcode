import string
from collections import defaultdict
import random

class Codec:

    def __init__(self):
        self.choices = string.uppercase + string.lowercase + string.digits
        self.choices = [i for i in self.choices]
        self.len = 6
        self.urls = {}

    def _get_random_key(self):
        key = ''.join([self.choices[random.randint(0, len(self.choices)-1)] for i in range(self.len)])
        return key


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self._get_random_key()
        self.urls[key] = longUrl
        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]
        
codec = Codec()
x = codec.encode('https://leetcode.com/problems/design-tinyurl')
print x 
print codec.decode(x)
