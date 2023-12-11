class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_list
            self.length += 1
            return True

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self,value):
        new_node = Node(value)

        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            self.length += 1

            return True 
        
        new_node.next = self.head
        self.head = new_node

        self.length += 1

        return True
    
    def insert(self,value,index):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return True 

        if index == self.length:
            self.append 
            return True 
        
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next 

            after = temp.next 
            temp.next = new_node
            temp.next.next = after
            after = None
            self.length += 1

            return True

            



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


new_list = Linked_List(30)
new_list.append(40)
new_list.prepend(50)
new_list.insert(20,1)

new_list.print_list()
