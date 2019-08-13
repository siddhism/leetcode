Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.

Given a list of sets, find the set that should be excluded to maximize the size of the intersection of the remaining sets.

30, 50, 100, 17  -> 8      -> 1
30, 50, 8, 18    ->        -> 0
30, 50, 8, 19    ->        -> 0
8, 24, 42        -> 30, 50 -> 2


    0 1 2  3        4   
0 - 1 r  1-3        1-4     
1   
2
3
4






x = 30, 50, 8, 18 
y = 30, 50, 8, 19


def get_intersection_size(self, sets, exclude):
    # returns number of elements in the intersection of sets
    n = len(sets)
    if exclude = 0:
        first = 1
    else:
        first = 0
    result = set(sets[first])
    for i in range(n):
        if i == exclude or i == first:
            continue
        current_set = set(sets[i])
        result = result.intersection(current_set)
    return len(result)

def find_max_intersection_size(self, sets):
n = len(sets)
max_len = 0
max_index = -1
if n == 0:
    return max_index
if n == 1:
    return 0
for i in range(n):
    # find intersection of remaining sets
    cur_len = get_intersection_size(sets, exclude=i)
    if cur_len >= max_len:
        max_len = cur_len
        max_index = i
return max_index
    







nlogn * n-1 
n*n logn


intersect = []
blogb + alogb
O((a+b)logb)
for k1 in x:
    if k1 is in y:
        interesect.append(k1)
    


