class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return None
        save = intervals
        # sort by keys
        intervals = sorted(intervals, key=lambda kv: (kv[0], kv[1]))
        # print intervals
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        n = len(intervals)
        result = [[prev_start, prev_end]]
        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]
            # if start is between prev_start to prev_end
            # or if end is between prev_start to prev_end
            # print prev_start, prev_end, start, end
            if (start >= prev_start and start <= prev_end)\
            or (end >= prev_start and end <= prev_end):
                new_start = min(start, prev_start)
                new_end = max(end, prev_end)
                # pop existing item with this merged interval
                # result = result[1:]
                if [prev_start, prev_end] in result:
                    result.remove([prev_start, prev_end])
                if [new_start, new_end] not in result:
                    result.append([new_start, new_end])
                prev_start = new_start
                prev_end = new_end
            else:
                # print '****'*5
                # print '\n'*2
                # print 'merge end, appending ', [prev_start, prev_end]
                # print 'result ', result
                if not ([prev_start, prev_end] in result):
                    result.append([prev_start, prev_end])
                # print 'result ', result
                prev_start = start
                prev_end = end
        # last item and not getting merged with anything
        # print '\n'*5
        # print 'Last item ', start, end, 
        # print 'merge end, appending ', [prev_start, prev_end]
        # print 'result ', result
        if not ([prev_start, prev_end] in result):
            result.append([prev_start, prev_end])
        return result

print Solution().merge([[1,3],[2,6],[8,10],[15,18]])
# print Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
print Solution().merge([[2,3],[5,5],[2,2],[3,4],[3,4]])
# print Solution().merge([[2,3],[5,5],[2,2],[3,4],[3,4]]) == [[2,4],[5,5]]
print Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
# print Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]) == [[1,3],[4,7]]

