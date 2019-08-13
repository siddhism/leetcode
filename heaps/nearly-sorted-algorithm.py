from heapq import heappush, heappop, heapify

def sort_k(arr, k):
    """
    sort nearly sorted arary
    """
    # create a min heap of first k elements
    n = len(arr)
    heap = arr[:k+1]
    heapify(heap)

    # go through all other elements and find min. keep appending to result
    result = []
    target_index = 0
    for i in range(k+1, n):
        elem = heappop(heap)
        result.append(elem)
        heappush(heap, arr[i])
    while heap:
        # add the remaining elements
        elem = heappop(heap)
        result.append(elem)
    return result

k = 3
arr = [2, 6, 3, 12, 56, 8] 
n = len(arr) 
result = sort_k(arr, k) 
  
print('Following is sorted array') 
print result