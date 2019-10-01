#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        out_s = []
        out_t = []
        n = len(S)
        m = len(T)
        for i in range(n):
            if S[i] == '#':
                if len(out_s) > 0:
                    out_s.pop(-1)
            else:
                out_s.append(S[i])
        for i in range(m):
            if T[i] == '#':
                if len(out_t) > 0:
                    out_t.pop(-1)
            else:
                out_t.append(T[i])
        print out_s, out_t
        return out_s == out_t
        

# print Solution().backspaceCompare('ab#c', 'ad#c')
# print Solution().backspaceCompare('bxj##tw', 'bxj###tw')
# "bxj##tw"\n"bxj###tw        

