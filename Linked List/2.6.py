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


def length(list):
    current_node = list.head
    count = 0
    while current_node.next is not None:
        count += 1
        current_node = current_node.next
    return count


def palindrome(list,length):
    result = isPalindrome(list.head.next, length)
    if result is False:
        print(False)
    else:
        print(True)


def isPalindrome(head, len):
    if len == 0:
        return head
    elif len == 1:
        return head.next
    res = isPalindrome(head.next, len-2)
    if res.data == head.data:
        return res.next
    else:
        return False


input_list = Linkedlist()
input_list.insert(1)
input_list.insert(0)
input_list.insert(1)
input_list.insert(1)
input_list.insert(0)
input_list.insert(1)
print(input_list.display())
length = length(input_list)
palindrome(input_list, length)
