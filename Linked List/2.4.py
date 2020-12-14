class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def insert(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements


def partition(n, first_linkedlist, second_linkedlist, value):
    current_node = n.head
    while current_node.next is not None:
        if current_node.next.data < value:
            first_linkedlist.insert(current_node.next.data)
            current_node = current_node.next
        else:
            second_linkedlist.insert(current_node.next.data)
            current_node = current_node.next
    first_linkedlist.tail.next = second_linkedlist.head.next
    print(first_linkedlist.display())

n = Linkedlist()
n.insert(1)
n.insert(2)
n.insert(7)
n.insert(4)
n.insert(5)
n.insert(6)
n.insert(3)
n.insert(8)
print(n.display())
first_linkedlist = Linkedlist()
second_linkedlist = Linkedlist()
partition(n, first_linkedlist, second_linkedlist, 5)







