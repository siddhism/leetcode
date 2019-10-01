#
# @lc app=leetcode id=642 lang=python
#
# [642] Design search
#

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.query = ''
        for idx, c in enumerate(sentences):
            self.add_record(c, times[idx])


    # methods to learn Trie

    # def get_index(self, char):
    #     if char == ' ':
    #         return 26
    #     else:
    #         return ord(char) - ord('a')

    # def insert(self, key):
    #     p_crawl = self.root
    #     n = len(key)
    #     for level in range(n):
    #         index = self.get_index(key[level])
    #         if not p_crawl.children[index]:
    #             p_crawl.children[index] = TrieNode()
    #         p_crawl = p_crawl.children[index] 
    #     p_crawl.isEnd = True
    
    # def search(self, key):
    #     n = len(key)
    #     p_crawl = self.root
    #     for i in range(n):
    #         index = self.get_index(key[level])
    #         if not p_crawl.children[index]:
    #             return False
    #         p_crawl = p_crawl.children[index]
    #     return p_crawl != None and p_crawl.isEnd


    def add_record(self, sentence, hot):
        p = self.root
        for i, c in enumerate(sentence):
            if c not in p.children.keys():
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot

    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for child_key in root.children:
                ret.extend(self.dfs(root.children[child_key]))
        return ret
    
    def search(self, keyword):
        p = self.root
        for i, c in enumerate(keyword):
            if not c in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
            
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        results = []
        if c !='#':
            self.query += c
            results = self.search(self.query)
        else:
            self.add_record(self.query, 1)
            self.query = ''
        return [item[1] for item in sorted(results)[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)