class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        ordered_people = sorted(people, key=lambda item: (item[0], -item[1]))
        # print ordered_people
        queue = []
        for item in reversed(ordered_people):
            h, k = item[0], item[1]
            queue.insert(k, item)
            # print ' queue after inserting ', item, ' : ', queue
        return queue
        # return ordered_people

print Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
)