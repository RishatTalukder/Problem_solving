class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height += 1
            return True

        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        temp = self.top
        if self.top is None:
            return None

        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return True

        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        temp = self.first
        if self.first is None:
            return None
        
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
            return temp
        
        self.first = self.first.next 
        temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


sueue = Queue(1)
sueue.enqueue(2)
sueue.print_queue()

print(sueue.dequeue().value)
print(sueue.dequeue().value)
print(sueue.dequeue())