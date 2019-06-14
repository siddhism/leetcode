from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for i in range(len(equations)):
            eq = equations[i]
            num = eq[0]
            den = eq[1]
            val = values[i]
            graph[num][den] = val
            graph[den][num] = float(1) / val
            graph[num][num] = 1
            graph[den][den] = 1

        print graph
        # Compute from end to end
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        results = []
        for num, den in queries:
            result = graph[num].get(den, -1)
            results.append(result)
        return results

inp = [["a","b"],["b","c"]]
inp2 = [2.0,3.0]
inpt3 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Solution().calcEquation(inp, inp2, inpt3)