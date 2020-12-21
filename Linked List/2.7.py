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


def in_node(node, list):
    list.tail.next = node
    list.tail = node


def intersection(first, second):
    if first.tail != second.tail:
        return False
    check = {}
    first_line = first.head
    second_line = second.head
    while first_line.next is not None:
        if first_line.next in check or second_line.next in check:
            return True

        if first_line.next is not None and first_line.next not in check:
            check[first_line.next] = 1
            first_line = first_line.next

        if second_line.next is not None and second_line.next not in check:
            check[second_line.next] = 1
            second_line = second_line.next
    return False


first_list = Linkedlist()
first_list.insert(1)
first_list.insert(2)
first_list.insert(3)
new_node = Node(4)
in_node(new_node, first_list)
first_list.insert(5)
first_list.insert(6)
print(first_list.display())
second_list = Linkedlist()
second_list.insert(2)
second_list.insert(2)
in_node(new_node, second_list)
while second_list.tail.next is not None:
    second_list.tail = second_list.tail.next
print(second_list.display())
print(intersection(first_list, second_list))


