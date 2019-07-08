class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        n = len(num1)
        m = len(num2)
        i = n - 1
        j = m - 1
        while i >=0 and j >= 0:
            a = num1[i]
            b = num2[j]
            s = int(a) + int(b) + carry
            if s >= 10:
                carry = s / 10
                s = s - 10
            else:
                carry = 0
            result.insert(0, str(s))
            i = i - 1
            j = j - 1
        if i >=0:
            s = int(num1[i]) + carry
            if s >= 10:
                carry = s / 10
                s = s - 10
            else:
                carry = 0
            result.insert(0, str(s))
            i -= 1
        if j >=0:
            import ipdb; ipdb.set_trace()
            s = int(num2[j]) + carry
            if s >= 10:
                carry = s / 10
                s = s - 10
            else:
                carry = 0
            result.insert(0, str(s))
            j -= 1
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)

print Solution().addStrings('6', '501')
print Solution().addStrings('1', '9')