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


def sumlists(first, second):
    firstlist = "".join(map(str, reversed(first.display())))
    secondlist = "".join(map(str, reversed(second.display())))
    result = int(firstlist) + int(secondlist)
    final = reversed(str(result))
    finallist = Linkedlist()
    for i in final:
        finallist.insert(int(i))
    return finallist.display()


def sumlists_followup(first, second):
    firstlist = "".join(map(str, first.display()))
    secondlist = "".join(map(str, second.display()))
    result = str(int(firstlist) + int(secondlist))
    finallist = Linkedlist()
    for i in result:
        finallist.insert(int(i))
    return finallist.display()


first_linkedlist = Linkedlist()
first_linkedlist.insert(2)
first_linkedlist.insert(5)
first_linkedlist.insert(6)
print(first_linkedlist.display())

second_linkedlist = Linkedlist()
second_linkedlist.insert(8)
second_linkedlist.insert(9)
second_linkedlist.insert(1)
print(second_linkedlist.display())

print(sumlists(first_linkedlist, second_linkedlist))
print(sumlists_followup(first_linkedlist, second_linkedlist))
