class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if not self.rear:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node
        print ('Enqueued {}'.format(data), self.rear.data)  

    def dequeue(self):
        if self.is_empty():
            return None
        # temp = self.front
        if self.front == None:
            self.rear = None
        self.front = self.front.next
        # print ('dequeue ', temp.data , ' from queue')
        # return temp.data

    def is_empty(self):
        if not self.front and self.rear:
            return True
        else:
            return False

    def traverse(self):
        """traverse the stack"""
        print ("Here's your queue > ")
        temp = self.front
        while temp:
            print temp.data,
            temp = temp.next
        print ('\n')

x = Queue()
x.enqueue(1)
x.traverse()
x.enqueue(2)
x.traverse()
x.enqueue(3)
x.traverse()
x.dequeue()
x.traverse()
x.dequeue()
x.traverse()
x.dequeue()
x.traverse()
x.dequeue()
x.traverse()
