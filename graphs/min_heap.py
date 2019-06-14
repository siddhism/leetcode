from heapq import heapify, heappush, heappop

class MinHeap:

    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1)/2

    def get_min(self):
        return self.heap[0]

    # def extract_min(self):
    #     return heappop(self.heap)

    def min_heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        # swap smallest with idx
        if smallest != idx:
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            self.min_heapify(smallest)

    def heap_sort(self):
        n = len(self.heap)
        for i in range(n/2, -1, -1):
            heap_obj.min_heapify(i)

    def extract_min(self):
        # swap it with last node
        size = len(self.heap)
        if not self.heap:
            return None
        root = self.heap[0]
        # Replace last node with root node
        self.heap[0] = self.heap[size - 1]
        # remove last node
        self.heap = self.heap[:-1]
        # call min heapify on root node
        self.min_heapify(0)
        return root

    def insert_key(self, k):
        heappush(self.heap, k)

    def delete(self, k):
        self.decrease_key(k, float("-inf"))
        self.extract_min()

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # swap value with parent
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])
            i = self.parent(i)



heapObj = MinHeap() 
# heapObj.insert_key(3) 
# heapObj.insert_key(2) 
# heapObj.delete(1) 
# heapObj.insert_key(15) 
# heapObj.insert_key(5) 
# heapObj.insert_key(4) 
# heapObj.insert_key(45) 
  
# print heapObj.extract_min(), 
# print heapObj.get_min(), 
# heapObj.decrease_key(5, -10)
# print heapObj.get_min() 


heap_obj = MinHeap()  
heap_obj.heap = [10, 6, 5, 4, 3, 1, 2]
heapObj.min_heapify(0)
