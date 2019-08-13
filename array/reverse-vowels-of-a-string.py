class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        l = 0
        r = n -1
        vowel = ['a' ,'e', 'i', 'o', 'u']
        s = [i for i in s]
        while l < r:
            # print 'string ', s
            # print 'left ', l, s[l], ' right ', r, s[r]
            if s[l] in vowel and s[r] in vowel:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l = l + 1
                r = r - 1
            elif s[r] in vowel:
                l = l + 1
            elif s[l] in vowel:
                r = r - 1
            else:
                l = l + 1
                r = r - 1
        return ''.join(s)
    
print Solution().reverseVowels('wow')