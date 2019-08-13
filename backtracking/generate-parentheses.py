class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # print ' called generateParenthesis with n : ', n
        if n == 1:
            return ["()"]
        # create three possible soln for every new pair
        # beginning, gobble up existing solns
        # append at the end
        prev = self.generateParenthesis(n-1)
        result = []
        for item in prev:
            x = '(' + item + ')'
            if x not in result:
                result.append(x)
        for item in prev:
            x = item + '()'
            if x not in result:
                result.append(x)
            x = '()' + item
            if x not in result:
                result.append(x)
        print ' soln at n : ', n
        print result
        # print 'wanted : ', ["((()))","(()())","(())()","()(())","()()()"]
        return result

print Solution().generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
print Solution().generateParenthesis(4) == ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]


["(((())))","((()()))","((())())","(()(()))","(()()())","((()))()","()((()))","(()())()","()(()())","(())()()","()(())()","()()(())","()()()()"]
["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]