#
# @lc app=leetcode id=551 lang=python
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_count = 0
        a_count = 0
        prev_c = s[0]
        if prev_c == 'L':
            l_count = 1
        if prev_c == 'A':
            a_count = 1
        for c in s[1:]:
            if c == 'L':
                if prev_c == 'L':
                    l_count += 1
                else:
                    l_count = 1
            if c == 'A':
                a_count += 1
            # print (prev_c, c, 
            # l_count, ' a count ', a_count)
            if a_count > 1 or l_count > 2:
                return False
            prev_c = c
        return True


# @lc code=end

print Solution().checkRecord('PPALLL')
print Solution().checkRecord('AA')
