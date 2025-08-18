class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node(2)
b = Node(3)

a.next = b 
c = Node(4)

b.next = c

while a:
    print(a.val)
    a = a.next