class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Doubly_linked_list:
    def __init__(self,val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.len = 1

    def print_ll(self, reverse=False):
        if reverse == False:
            temp = self.head 

            while temp:
                print(temp.val)
                temp = temp.next

        else:
            temp =  self.tail

            while temp:
                print(temp.val)
                temp = temp.prev

    def append(self, val):
        new_node = Node(val)

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        self.len += 1


dl = Doubly_linked_list(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.append(5)
dl.print_ll()
dl.print_ll(reverse=True)