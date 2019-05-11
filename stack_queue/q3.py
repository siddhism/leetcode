class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = None

    def push(self, data):
        node = StackNode(data)
        if not self.min:
            self.min = data
        elif data < self.min:
            self.min = data
        # print 'is empty ', self.is_empty()
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        # print ('pushing ', data , ' to stack')

    def get_min(self):
        print ('min : ', self.min)
        return self.min

    def pop(self):
        if self.is_empty():
            return
        # print ('pop ', self.top.data , ' from stack')
        self.top = self.top.next

    def top(self):
        return self.top

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False

    def traverse(self):
        """traverse the stack"""
        print ("Here's your stack > ")
        temp = self.top
        while temp:
            print temp.data,
            temp = temp.next
        print ('\n')

x = Stack()
x.push(2)
x.push(3)
x.push(4)
x.traverse()
x.get_min()
x.push(5)
x.push(1)
x.traverse()
x.get_min()