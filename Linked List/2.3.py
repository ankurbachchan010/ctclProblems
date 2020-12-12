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


n = Linkedlist()
n.insert(1)
n.insert(2)
n.insert(3)
n.insert(4)
print(n.display())
