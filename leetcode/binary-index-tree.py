class BITree(object):

    def __init__(self, array):
        self.array = [0] * len(array)
        self.tree = [0] * (len(array) + 1)
        for i in range(len(array)):
            self.update(i, array[i])
    
    def get_next(self, index):
        return index + (index & -index)
    
    def get_parent(self, index):
        return index - (index & -index)
    
    def update(self, index, val):
        current = self.array[index]
        self.array[index] = val
        diff = val - current
        # Update all next eligible index with diff
        index = index + 1
        while index < len(self.tree):
            self.tree[index] += diff
            index = self.get_next(index)
    
    def prefix_sum(self, index):
        """
        Get sum upto index from starting position
        sum parents until you reach zero
        """
        total = 0
        # since tree index starts from +1 then array
        index += 1
        while index > 0:
            total += self.tree[index]
            index = self.get_parent(index)
        return total
    
    def range_sum(self, x, y):
        return (self.prefix_sum(max(x, y)) - self.prefix_sum(min(x, y)))

    def describe(self):
        print 'Array -> ', self.array
        print 'Tree  -> ', self.tree

tree = BITree([3,2,-1,6,5,4])
#   tree = FenTree([int(i) for i in input('Enter the array(space-separated integers): ').split()])
tree.describe()

tree.update(4, 8); #replaces 5 with 8 in the list given to the fenwick tree
tree.describe()

print(tree.range_sum(1, 5));  #returns 2-1+6+5+4
print(tree.prefix_sum(5));    #returns 3+2-1+6+5+4

tree = BITree([-2,0,3,-5,2,-1])
tree.describe()
print tree.range_sum(0, 2)
print tree.range_sum(1, 2)
print tree.range_sum(0, 2)