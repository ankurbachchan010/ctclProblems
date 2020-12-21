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


def loopDetection(list):
    fast = list.head.next
    slow = list.head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return "Not a circular linked list"
    slow = list.head.next
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.data


circular_list = Linkedlist()
circular_list.insert(1)
circular_list.insert(2)
new_node = Node(9)
circular_list.tail.next = new_node
circular_list.tail = new_node
circular_list.insert(3)
circular_list.insert(4)
circular_list.insert(5)
circular_list.insert(6)
circular_list.insert(7)
circular_list.insert(8)
circular_list.tail.next = new_node
print(loopDetection(circular_list))


