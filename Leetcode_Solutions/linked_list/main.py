class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)

        # checking if the list is empty or not because when the list is empty, the head and tail both point to the same node
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        
    def prepend(self,value):
        new_node = Node(value)

        # checking if the list is empty or not because when the list is empty, the head and tail both point to the same node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        
        else:
            new_node.next = self.head # the new node's next value should point to the current head
            self.head = new_node # the new node should become the new head
            self.length += 1 # increment the length by 1
            return True
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self,):
        # checking if the list is empty
        if self.length == 0:
            return "there is no element in the list"
        
        # checking if the list has only 1 element there is no need to loop through the list
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        # if the list has more than 1 element
        current_node = self.head # current node is the head node
        while current_node.next is not None:
            previous_node = current_node # previous node is the node before the current node
            current_node = current_node.next 

        # now current node is the tail node and previous node is the node before the tail node

        previous_node.next = None # removing the pointer to the tail node
        temp = self.tail # storing the tail node in a temp variable to return it later
        self.tail = previous_node # setting the new tail node
        self.length -= 1 # decrementing the length by 1

        return temp # returning the deleted node
    
    def pop_first(self):
        # checking if the list is empty
        if self.length == 0:
            return "there is no element in the list"
        
        # checking if the list has only 1 element there is no need to loop through the list
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        # if the list has more than 1 element
        temp = self.head # storing the head node in a temp variable to return it later
        self.head = self.head.next # setting the new head node
        temp.next = None # removing the pointer to the next node
        self.length -= 1 # decrementing the length by 1

        return temp

    def get(self,index):
        # checking if the index is valid
        if index < 0 or index >= self.length:
            return None
        
    # if the index is in range
        temp = self.head
        
        for _ in range(index):
            temp = temp.next

        return temp

    def set(self,index,value):
        # getting the node at the index using the get method
        temp = self.get(index)

        # if the node is found
        if temp:
            temp.value = value
            return True
        
        # if the node is not found
        return False

    def insert(self,index,value):
        # checking if the index is valid
        if index < 0 or index > self.length:
            return "index out of range"
        
        # if the index is 0, we will use the prepend method
        if index == 0:
            return self.prepend(value)
        
        # if the index is the same as the length, we will use the append method
        if index == self.length:
            return self.append(value)
        
        # creating a new node
        new_node = Node(value)

        # getting the node before the index
        previous_node = self.get(index-1)

        # getting the node after the index
        temp = previous_node.next

        # setting the next value of the previous node to the new node
        previous_node.next = new_node

        # setting the next value of the new node to the temp node
        new_node.next = temp

        # incrementing the length by 1
        self.length += 1

        return True

    def remove(self,index):
        # checking if the index is valid
        if index < 0 or index >= self.length:
            return "index out of range"
        
        # if the index is 0, we will use the pop_first method
        if index == 0:
            return self.pop_first()
        
        # if the index is the same as the length-1, we will use the pop method
        if index == self.length-1:
            return self.pop()
        
        # getting the node before the index
        previous_node = self.get(index-1)

        # getting the node after the index
        temp = previous_node.next

        # setting the next value of the previous node to the temp node
        previous_node.next = temp.next

        # removing the pointer to the next node
        temp.next = None

        # decrementing the length by 1
        self.length -= 1

        return temp

    def reverse(self):
        # checking if the list is empty
        if self.length == 0:
            return "there is no element in the list"

        # if the list has only 1 element
        if self.length == 1:
            return self.head

        # if the list has more than 1 element we start with swapping the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # time for the worm
        previous_node = None
        current_node = temp 

        # time to walk through the list
        for _ in range(self.length):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return True


new_list = Linked_List(1)
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.insert(index=2,value=10)
new_list.insert(index=0,value=6)
new_list.insert(index=7,value=20)

print(f" The list before reversing: ")
new_list.print_list()

new_list.reverse() # reversing the list

print(f" The list after reversing: ")
new_list.print_list()