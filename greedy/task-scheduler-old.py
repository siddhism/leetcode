class Solution(object):
    def leastInterval(self, tasks_inpt, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        tasks = defaultdict(int)
        for task in tasks_inpt:
            tasks[task] += 1
        if not tasks:
            return 0
        max_tasks = max(tasks.values())
        execution = []
        wait = defaultdict(int)
        prev = defaultdict(int)
        for k, v in tasks.items():
            wait[k] = 0
        # get the key with minimum wait time
        # choose it, update all other keys wait time = -1
        # sort in order of values, get first element and it's key
        while len(tasks) > 0:
            # order by min wait and max pending task count
            min_wait_key = sorted(wait.items(), 
                key=lambda item: (item[1], -tasks[item[0]]))[0][0]
            # print 'wait ', dict(wait), 'tasks : ', dict(tasks)
            # print min_wait_key, tasks[min_wait_key], 'min_wait_key ', min_wait_key
            if wait[min_wait_key] < 0 or tasks[min_wait_key] == 0:
                # no action needed for already done tasks
                tasks.pop(min_wait_key)
                wait.pop(min_wait_key)
                continue
            if wait[min_wait_key] == 0:
                # if no more wait is needed do this task
                execution.append(min_wait_key)
                wait[min_wait_key] = n
                tasks[min_wait_key] -= 1
            else:
                execution.append('idle')
                wait[min_wait_key] -= 1
            for k, v in wait.items():
                if k == min_wait_key:
                    continue
                if wait[k] > 0:
                    wait[k] -= 1
            # print execution
        print execution
        return len(execution)
                
print Solution().leastInterval(["A","A","A","B","B","B"], 0)
# print Solution().leastInterval(["A","B","C","A","B"], 2)
