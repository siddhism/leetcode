from collections import defaultdict

class Heap:

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        min_heap_node = [v, dist]
        return min_heap_node

    def swap_min_heap_node(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    
