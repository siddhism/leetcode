class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # order by finish time
        intervals = sorted(intervals, key=lambda kv:kv[0])
        count = 1
        if not intervals: return 0
        n = len(intervals)
        start = intervals[0][0]
        finish = intervals[0][1]
        print intervals
        for i in range(1, n):
            cur_start = intervals[i][0]
            cur_finish = intervals[i][1]
            if cur_start >= finish:
                continue
            else:
                count += 1
                finish = cur_finish
                start = cur_start
        return count

print Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2
print Solution().minMeetingRooms([[5,8],[6,8]]) == 2
print Solution().minMeetingRooms([[9,10],[4,9],[4,17]]) == 2
print Solution().minMeetingRooms([[1,5],[8,9],[8,9]]) == 2
print Solution().minMeetingRooms([[2,11],[6,16],[11,16]]) == 2