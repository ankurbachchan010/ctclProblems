class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = self.head

    def append(self, data):
        new_node = node(data)
        self.tail.next = new_node
        self.tail = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR : Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR : Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                if last_node.next == None:
                    self.tail = last_node
                return
            cur_idx += 1


def getkthelement(dup_list, k):
    p1 = dup_list.head.next
    p2 = dup_list.head.next
    count = 0
    for i in range(k-1):
        p2 = p2.next
    while p2.next is not None:
        count += 1
        p1 = p1.next
        p2 = p2.next
    return p1.data, count


dup_list = linked_list()
dup_list.append(1)
dup_list.append(2)
dup_list.append(1)
dup_list.append(3)
dup_list.append(4)
dup_list.append(2)

dup_list.display()
print(getkthelement(dup_list, 4))
