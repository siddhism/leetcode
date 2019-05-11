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

    def len(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def delete(self, node):
        temp = self.head
        prev = self.head
        if self.head == node:
            self.head = self.head.next
            return
        while temp is not None:
            if temp == node:
              prev.next = temp.next
              temp.next = None
            prev = temp
            temp = temp.next


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

node = ll.get(1)
ll.delete(node)
ll.traverse()
