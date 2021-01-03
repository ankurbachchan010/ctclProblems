class Item:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Item()
        self.tail = self.head

    def pop(self):
        current = self.head
        while current.next is not None:
            previous = current
            if current.next == self.tail:
                self.tail = previous
                previous.next = current.next.next
                break
            current = current.next

    def push(self, item):
        new_item = Item(item)
        self.tail.next = new_item
        self.tail = new_item

    def peek(self):
        return self.tail.data

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


def threeInOne(ipt):
    n = len(ipt)
    stack1 = list()
    stack2 = list()
    stack3 = list()
    for i in range(n):
        if i < n//3:
            stack1.append(ipt[i])
        elif i < 2*n//3:
            stack2.append(ipt[i])
        else:
            stack3.append(ipt[i])
    return stack1, stack2, stack3


def threeInOneFlex(ipt):
    n = len(ipt)
    stack1 = [None] * (n // 3 + 1)
    stack2 = [None] * (n // 3 + 1)
    stack3 = [None] * (n // 3 + 1)
    for i in range(n):
        if i < len(stack1):
            stack1[i] = ipt[i]
        elif i < 2*len(stack2):
            stack2[i - len(stack1)] = ipt[i]
        else:
            stack3[i-(len(stack1) + len(stack2))] = ipt[i]
    return stack1, stack2, stack3


input = [1, 5, 7, 8, 6, 8, 4, 5, 2, 3, 0]
print(threeInOne(input))
print(threeInOneFlex(input))
