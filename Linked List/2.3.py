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

    def delete_middle(self, node):
        if self.head.next.data == node.data or self.tail.data == node.data:
            return False
        else:
            current_node = self.head
            last_node = current_node
            current_node = current_node.next
            while True:
                if current_node.data == node.data:
                    last_node.next = current_node.next
                    break
                last_node = current_node
                current_node = current_node.next
            return True


n = Linkedlist()
n.insert(1)
n.insert(2)
n.insert(3)
n.insert(4)
print(n.display())
node = Node(3)
print(n.delete_middle(node))
print(n.display())



