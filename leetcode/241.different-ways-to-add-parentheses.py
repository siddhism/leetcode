class Solution(object):
    def diffWaysToCompute(self, input, memo={}):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in left:
                    for k in right:
                        op = self.get_op(c)
                        out = op(j, k)
                        res.append(out)
        memo[input] = sorted(res)
        return sorted(res)

    def get_op(self, c):
        import operator
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }
        return op_map.get(c)






        