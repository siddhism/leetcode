class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(len(s)/2):
            # swap i and n-i-1 element
            # print (s[i], s[n-i-1])
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
        return s

print Solution().reverseString(["h","e","l","l","o"])