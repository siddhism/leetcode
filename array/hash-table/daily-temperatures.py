class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        result = [0] * len(T)
        n = len(T)
        temps = {}
        i = n-1
        while i >= 0:
            temp = T[i]
            day = str('inf')
            for j in range(temp+1, 101):
                if j in temps:
                    day = min(day, temps[j] - i)
            if day != str('inf'):
                result[i] = day
            temps[temp] = i # reset day to current day, as elems lower than this can see this
            i = i - 1
        return result

print Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70])
