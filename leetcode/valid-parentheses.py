class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        comp = {'}': '{', ')': '(', ']': '['}
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for i, ch in enumerate(s):
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                if not stack:
                    # no opening bracket for this closing
                    return False
                top = stack[-1]
                # get top element, if it is complimenting current parantheses
                if top == comp.get(ch):
                   stack = stack[:-1] # pop this
                else:
                    return False
        if stack:
            # not all brackets were closed
            return False
        # if reached here, means everything went fine
        return True

print Solution().isValid("()")            
print Solution().isValid("()[]{}")
print Solution().isValid("(]")
print Solution().isValid("([)]")
print Solution().isValid("{[]}")