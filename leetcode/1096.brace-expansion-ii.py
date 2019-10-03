#
# @lc app=leetcode id=1096 lang=python
#
# [1096] Brace Expansion II
#

# @lc code=start
class Solution(object):
    def evaluate(self, expr):
        print 'inside evaluate ', expr
        out = set()
        n = len(expr)
        x, op, y = expr
        if op == ',':
            # this will work if x or y are strings or even set
            out = set(x).union(set(y))
        elif op == '.':
            out = set()
            for i1 in x:
                for i2 in y:
                    out.add(i1+i2)
        return out

    def braceExpansionII(self, exp):
        """
        :type expression: str
        :rtype: List[str]
        """
        # sample "{a,b}{c,{d,e}}"
        stack = []
        for c in exp:
            if c == '{':
                stack.append('{')
            elif c == '}':
                # while there is x , y format keep doing it and just keep 1 element to be operated
                while stack[-2] == ',':
                    set2 = stack.pop()
                    stack.pop()
                    stack[-1].update(set2)
                assert(stack[-2] == '{')
                tail = stack.pop()
                stack[-1] = tail
            elif c == ',':
                stack.append(',')
            else:
                stack.append(set(c))
            while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set(w1 + w2 for w1 in set1 for w2 in set2))
        assert(len(stack) == 1)
        return list(sorted(stack[-1]))


# @lc code=end

print Solution().braceExpansionII("{a,b}{c,{d,e}}")
# print Solution().braceExpansionII("{{a,z},a{b,c},{ab,z}}")


