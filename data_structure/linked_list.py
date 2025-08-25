from node import Node


class LinkedList:
    def __init__(self,val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.len = 1
 
    def append(self,val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.len += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

llist = LinkedList(1)
llist.append(2) 
llist.append(3)
llist.append(4) 

llist.print_list()
a = 2
print(type(a))
print(__name__)