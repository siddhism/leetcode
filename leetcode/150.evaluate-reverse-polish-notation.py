#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = ['+', '-', '*', '/']
        import operator
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div
        }

        for item in tokens:
            if item in ops:
         
                # pick last two items and apply operation
                x = stack.pop()
                y = stack.pop()
                if item == '/':
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    # if x * y < 0 and x % y != 0:
                    #     res = x / y + 1
                    # else:
                    #     res = x / y
                    res = int(float(y)/ float(x))
                else:
                    res = op_map.get(item)(y, x)
                stack.append(res)
            else:
                stack.append(int(item))
            # print ' after pushing ', item, ' stack ', stack
        
        return stack[0]

print Solution().evalRPN(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
) == 22
# print Solution().evalRPN(["4", "3", "-"]) == 1
print Solution().evalRPN(
    ["4","-2","/","2","-3","-","-"]
)
print Solution().evalRPN(
    ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
)

        
# @lc code=end

