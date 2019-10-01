#
# @lc app=leetcode id=911 lang=python
#
# [911] Online Election
#
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        from collections import defaultdict
        counts = defaultdict(int)
        self.times  = times
        ts = defaultdict(int) # timestamp of last appearances
        for idx, person in enumerate(persons):
            counts[person] += 1
            ts[person] = times[idx]

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # t = timestamp when we want to know top
        # find index which is smaller/equal to this
        import bisect
        left = bisect.bisect_left(self.times)
        # find counts greater than this index
        #  


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

