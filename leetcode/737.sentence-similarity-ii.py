#
# @lc app=leetcode id=737 lang=python
#
# [737] Sentence Similarity II
#


class DSU(object):

    def __init__(self, V):
        from collections import defaultdict
        self.parent = defaultdict(str)
        self.size = defaultdict(int)
    
    def union(self, a, b):
        parent_a = self.root(a)
        parent_b = self.root(b)
        if self.size[parent_a] <= self.size[parent_b]:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += 1
        else:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += 1

    
    def root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def find(self, a, b):
        return self.root(a) == self.root(b)


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        n = len(words1)

        dsu = DSU(n)
        # initialize self parent
        for i in range(n):
            word = words1[i]
            dsu.parent[word] = word
            word = words2[i]
            dsu.parent[word] = word

        # connect all pairs
        for word1, word2 in pairs:
            dsu.union(word1, word2)

        # print dsu.parent        
        # check words1 and words2
        for i in range(n):
            a = words1[i]
            b = words2[i]
            if a == b or dsu.find(a, b):
                continue
            else:
                return False
        return True


# print Solution().areSentencesSimilarTwo(
#     ["great","acting","skills"],
#     ["fine","painting","talent"],
#     [["great","fine"],["drama","acting"],["skills","talent"]]
# )

        
