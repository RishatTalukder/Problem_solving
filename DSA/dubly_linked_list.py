# Define a Node class with a constructor that initializes the node's value, and next and previous pointers to None
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Define a DoublyLinkedList class with a constructor that initializes the head and tail pointers to a new node with the given value, and the length to 0
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Define an append method that takes a value, creates a new node with that value, and adds it to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    # Define a pop method that removes and returns the last node in the list
    def pop(self):
        temp = self.tail
        if self.head is None:
            return "empty list"
        if self.length == 1:
            temp = self.head
            self.length -= 1
            self.head = None
            self.tail = None
            return temp.value
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp.value

    # Define a prepend method that takes a value, creates a new node with that value, and adds it to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    # Define a pop_first method that removes and returns the first node in the list
    def pop_first(self):
        if self.head is None:
            return "empty list"

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        self.length -= 1
        return temp.value

    # Define a get method that takes an integer index and returns the node at that index
    def get_index(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.head

        if index == self.tail:
            return self.tail

        else:
            if index < self.length / 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next

            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev

            return temp

    # Define a set_index method that takes an integer index, and a value, and updates the value of the node at that index with that value
    def set_index(self, index, value):
        temp = self.get_index(index)

        if temp:
            temp.value = value
            return True
        return False

    # Define an insert method that takes an integer index and a value, creates a new node with that value, and inserts it at that index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get_index(index - 1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        self.length += 1
        return True

    # Define a remove method that takes an integer index and removes the node at that index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get_index(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    # Define a print_list method that prints the values of each node in the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


linkedlist = DoublyLinkedList(0)
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.insert(7, 7)
print(linkedlist.remove(4).value)
print(linkedlist.length)
linkedlist.print_list()
