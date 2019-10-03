#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node(object):
    def __init__(self, val=None):
        from collections import defaultdict
        self.val = val
        # children will contain key to node mapping {'a': Node('a')}
        self.children = defaultdict(str)
        self.is_end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # create head node
        self.head = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        # insert a node at given position
        current_node = self.head

        for c in word:
            if not current_node.children.get(c):
                # create a new node if children at that index does not exist
                current_node.children[c] = Node(c)
            # move current node to next character, if there was not a node at word it's created above
            current_node = current_node.children[c]
        current_node.is_end = True        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.head
        queue = []
        visited = {self.head: True}
        
        for c in word:
            if not c in node.children:
                return False
            node = node.children[c]
        if node:
            return node.is_end
        return False


    def startsWith(self, prefix, index=0):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.head
        queue = []
        visited = {self.head: True}

        for c in prefix:
            if not c in node.children:
                return False
            node = node.children[c]
        # loop finished means the prefix was found till this pos
        return True

       
    
    def traverse(self):
        node = self.head
        queue = [self.head]
        visited = {self.head: True}
        while queue:
            top = queue.pop()
            visited[top] = True
            print top.val, ' is end ', top.is_end
            for k, v in top.children.items():
                if not visited.get(v):
                    queue.append(v)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert('apple')
# obj.insert('apex')
# obj.insert('app')
# obj.traverse()
# print obj.search('apple')
# print obj.search('app')
# print obj.startsWith('app')
# @lc code=end

