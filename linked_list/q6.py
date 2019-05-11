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
        print ('\n')

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

def reverse(ll):
    if not ll.head:
        return
    prev = ll.head
    node = ll.head.next
    prev.next = None
    while node:
        temp = node.next # keep the reference for setting later
        node.next = prev
        prev = node
        node = temp
    # set old head to end node
    # set head at the last node
    ll.head = prev
    return ll



ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

ll.traverse()
x = reverse(ll)
x.traverse()
# ll.traverse()
# result = LinkedList()
# temp = ll.head
# save = temp
# while temp:
#     node = Node(temp.data)
#     node.next = result.head
#     result.head = node
#     temp = temp.next
# result.traverse()