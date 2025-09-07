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

    def index(self, ind):
        if ind < 0  or ind >= self.len:
            raise IndexError('Index out of bound')
        
        temp = self.head

        for i in range(ind):
            temp = temp.next

        return temp.val
    

    def insert(self, ind, val):
        prev = self.head

        for i in range(ind-1):
            prev = prev.next

        next = prev.next

        new_node = Node(val)

        prev.next = new_node
        new_node.next = next
        self.len += 1

    def pop(self):
        prev = self.head

        while prev.next.next:
            prev = prev.next

        prev.next = None 

        temp = self.tail

        self.tail = prev
        self.len -= 1

        return temp.val
    

    def remove(self, ind):
        prev = self.head
        
        for i in range(ind-1):
            prev = prev.next

        curr = prev.next
        next = curr.next

        prev.next = next
        curr.next = None

        self.len -= 1

        return curr.val
        


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def reverse(self):
        if self.len  == 0:
            return
        curr = self.head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head, self.tail = self.tail, self.head




llist = LinkedList(1)
llist.append(2)
llist.append(3)
llist.append(4)


llist.reverse()
print('Reversed list:')
llist.print_list()