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

    def dup(self):
        checker = []
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data in checker:
                last_node.next = cur_node.next
                if last_node.next == None:
                    self.tail = last_node
            else:
                checker.append(cur_node.data)
        return

    def dup1(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            runner = cur_node
            while runner.next != None:
                runner = runner.next
                if runner.data == cur_node.data:
                    cur_node.next = cur_node.next.next
        return


dup_list = linked_list()
dup_list.append(1)
dup_list.append(2)
dup_list.append(1)
dup_list.append(3)
dup_list.append(4)
dup_list.append(2)

dup_list.display()
dup_list.dup()
dup_list.display()
print(dup_list.get(2))
dup_list.dup1()
dup_list.display()