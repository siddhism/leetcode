class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # create data to keep track of which one is visited
        data = {i: costs[i] for i in range(len(costs))}
        # {0: [10, 20], 1: [30, 200], 2: [400, 50], 3: [30, 20]}   
        # sort a and b distances. store visited indexes
        a = sorted(data.items(), key=lambda kv: kv[1][0])
        b = sorted(data.items(), key=lambda kv: kv[1][1])
        # a = [(0, [10, 20]), (1, [30, 200]), (3, [30, 20]), (2, [400, 50])]
        # key = city, value = dist_a, dist_b

        done = 0
        visited = []
        total=0
        n = len(costs)
        a_visited = 0
        b_visited = 0
        while done < n:
            # if a visited city index comes back in the loop
            if a[0][0] in visited:
                a.pop(0)
                continue
            if b[0][0] in visited:
                b.pop(0)
                continue
            # take min of a city distance or b city distance
            x = a[0][1][0]
            y = b[0][1][1]
            cur = min(x, y)
            if cur == x or b_visited == n - 1:
                print 'choose a ', cur
                visited.append(a[0][0])
                a_visited += 1
                a.pop(0)
            else:
                print ' choose b', cur
                visited.append(b[0][0])
                b_visited += 1
                b.pop(0)
            else:
                continue
            done += 1
            total += cur
        return total

print Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
