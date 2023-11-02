class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def get(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def remove(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def insert(self, index: int, value):
        if index < 0 or index > self.size:
            raise IndexError("Index is out of range")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def __iter__(self):
        return LinkedListIterator(self.head)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.data
        self.current = self.current.next
        return value


ll = LinkedList()
ll.push(5)
ll.push(10)
ll.push(12)
ll.insert(1, 20)
for value in ll:
    print(value)