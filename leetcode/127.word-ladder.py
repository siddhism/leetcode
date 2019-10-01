#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict, deque
        import copy
        if not wordList:
            return 0

        def get_generic_versions(word):
            n = len(word)
            result = []
            for i in range(n):
                # store all combos of chars skipped one by one
                temp_word_list = copy.deepcopy(list(word))
                temp_word_list[i] = '*'
                temp_word = ''.join(temp_word_list)
                result.append(temp_word)
            return result

        n = len(wordList[0])
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                # store all combos of chars skipped one by one
                temp_word = word[:i] + '*' + word[i+1:]
                word_dict[temp_word].append(word)

        # print word_dict

        start = beginWord
        visited = defaultdict(bool)
        queue = deque()
        step = 1
        queue.append((start, step))
        n = len(beginWord)

        while len(queue) > 0:
            top, step = queue.popleft()
            if top == endWord:
                # found the last word, need to stop and return step count
                return step

            if visited[top]:
                # if top is already visited, continue
                continue
            visited[top] = True
            # print ' inside BFS for word ', top, ' step number ', step

            for i, c in enumerate(top):
                # all combos of eliminitaging one by one char
                checkpoint = top[:i] + '*' + top[i+1:]
                # get one distance away words from current checkpoint
                words = word_dict[checkpoint]
                # print ' for checkpoint ', checkpoint, ' words ', words
                for word in words:
                    # print 'sub_word ', checkpoint, ' appending ', word
                    queue.append((word, step+1))
            # print '\n\n\nqueue ', queue

        return 0


# print Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
# print Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"])
# print Solution().ladderLength(
#     "talk",
#     "tail",
#     ["talk","tons","fall","tail","gale","hall","negs"]
# )
