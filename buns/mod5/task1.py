class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(5)
stack.push(10)
ll = stack.pop()
print(ll)