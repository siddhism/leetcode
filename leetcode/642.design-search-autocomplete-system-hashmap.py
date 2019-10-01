#
# @lc app=leetcode id=642 lang=python
#
# [642] Design search
#

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        from collections import defaultdict
        self.data = defaultdict(int)
        self.query_cache = defaultdict(list)
        for idx, sentence in enumerate(sentences):
            for i, c in enumerate(sentence):
                cur_str = sentence[:i]
                self.data[cur_str] = times[idx]
                # updated count
                count = self.data[cur_str]
                # for each sentence part
                self.query_cache[cur_str].append((times[idx], sentence))
        # print self.data
        # print self.query_cache
        self.query = ''         

    def update_cache(self, sentence):
        for i, c in enumerate(sentence):
            cur_str = sentence[:i]
            self.data[cur_str] += 1 
            count = self.data[cur_str]
            # for each sentence part
            self.query_cache[cur_str].append((count, sentence))


    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c !='#':
            self.query += c

        # find top 3 from query cache
        query_cache = self.query_cache[self.query]
        sentcs = sorted(query_cache, key=lambda kv:(-kv[0], kv[1]))
        data = [item[1] for item in sentcs][:3]
        # initialize query again
        if c == '#':
            self.query = ''
            self.update_cache(self.query, 1)
        return data


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)