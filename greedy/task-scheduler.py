class Solution(object):
    def leastInterval(self, tasks_inpt, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        if n == 0:
            return 0
        tasks = [0 for _ in range(26)]
        for task in tasks_inpt:
            tasks[ord(task)-65] += 1
        tasks = sorted(tasks)
        max_val = tasks[25] - 1
        idle_slots = max_val * n
        count = 0
        i = 24
        while i>=0 and tasks[i] > 0:
            # min of current task or max_val
            idle_slots -= min(tasks[i], max_val)
            i = i - 1
        if idle_slots > 0:
            # total idle slots + all tasks
            return idle_slots + len(tasks)
        else:
            # if there are no idle slots, 
            return len(tasks)

# print Solution().leastInterval(["A","A","A","B","B","B"], 0)
# print Solution().leastInterval(["A","A","A","B","B","B"], 2)
# print Solution().leastInterval(["A","B","C","A","B"], 2)
