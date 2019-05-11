class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head

        while temp is not None:
            print temp.data,
            temp = temp.next

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def get(self, index):
        """
        Returns member of linked list at index
        return : Node object
        """
        length = self.len()
        if index < 1 or index > length:
            return None
        temp = self.head
        counter = 1
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter = counter + 1

    def tail(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp

    def particition(self, data):
        x = LinkedList()
        y = LinkedList()
        temp = self.head
        while temp:
            if temp.data < data:
                x.insert(temp.data)
            else:
                y.insert(temp.data)
            temp = temp.next
        # connect x and y
        print x.traverse()
        print y.traverse()
        x_tail = x.tail()
        print (x_tail.data)
        x_tail.next = y.head
        return x


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(3)
ll.insert(1)
ll.insert(3)
ll.insert(3)
ll.traverse()
print ('\n')

num = input('Enter particition number > ')
data = ll.particition(num)
data.traverse()
