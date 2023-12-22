class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def print_list(self, reverse = False):
        if self.head is None:
            return None
        
        # if reverse is True, print the list in reverse
        if reverse is True:
            # set temp to the tail
            temp = self.tail
            # while temp is not None, print the value and set temp to temp.prev
            while temp is not None:
                print(temp.value)
                temp = temp.prev

        else:
            # else set temp to the head
            temp = self.head
            # while temp is not None, print the value and set temp to temp.next
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        # create a new node
        new_node = Node(value)

        # if the head is None, set the head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return True
        
        # set the next of the tail to the new node
        self.tail.next = new_node
        # set the prev of the new node to the tail
        new_node.prev = self.tail
        # set the tail to the new node
        self.tail = new_node
        # increment the length by 1
        self.length += 1

        return True
    
    def prepend(self, value):
        # create a new node
        new_node = Node(value)

        # if the head is None, set the head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return True

        # set the next of the new node to the head
        new_node.next = self.head
        # set the prev of the head to the new node
        self.head.prev = new_node
        # set the head to the new node
        self.head = new_node
        # increment the length by 1
        self.length += 1

        return True

    def pop(self,):
        # if the head is None, return None
        if self.head is None:
            return None
        
        # if the length is 1, set the head and tail to None and decrement the length by 1
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp

        # set the temp to the tail
        temp = self.tail
        # set the tail to the prev of the tail
        self.tail = self.tail.prev
        # set the next of the new tail to None
        self.tail.next = None
        # set the prev of the temp to None
        temp.prev = None
        # decrement the length by 1
        self.length -= 1

        # return the value of the temp
        return temp

    def pop_first(self):
        # if the head is None, return None
        if self.head is None:
            return None
        
        # if the length is 1, set the head and tail to None and decrement the length by 1
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp

        # set the temp to the head
        temp = self.head
        # set the head to the next of the head
        self.head = self.head.next
        # set the prev of the new head to None
        self.head.prev = None
        # set the next of the temp to None
        temp.next = None
        # decrement the length by 1
        self.length -= 1

        # return the value of the temp
        return temp
    
    def get(self, index):
        # if the index is less than 0 or greater than or equal to the length, return None
        if index < 0 or index >= self.length:
            return None
        
        # if the index is 0
        if index == 0:
            return self.head
        
        # if the index is equal to the length - 1
        if index == self.length - 1:
            return self.tail
        
        # if the index is less than or equal to half the length
        if index <= self.length // 2:
            # set the temp to the head
            temp = self.head
            # set the counter to 0
            counter = 0
            # while the counter is less than the index, set the temp to the next of the temp and increment the counter by 1
            while counter < index:
                temp = temp.next
                counter += 1
            
            # return the temp
            return temp
        
        # else
        else:
            # set the temp to the tail
            temp = self.tail
            # set the counter to the length - 1
            counter = self.length - 1
            # while the counter is greater than the index, set the temp to the prev of the temp and decrement the counter by 1
            while counter > index:
                temp = temp.prev
                counter -= 1
            
            # return the temp
            return temp

    def set(self, index, value):
        # get the node at the index
        node = self.get(index)

        # if the node is None, return False
        if node is None:
            return False
        
        # set the value of the node to the value
        node.value = value

        # return True
        return True
    
    def insert(self, index, value):
        # if the index is less than 0 or greater than the length, return False
        if index < 0 or index > self.length or self.head is None:
            return False
        
        # if the index is 0, prepend the value and return True
        if index == 0:
            self.prepend(value)
            return True
        
        # if the index is equal to the length, append the value and return True
        if index == self.length:
            self.append(value)
            return True
        
        # create a new node
        new_node = Node(value)
        # get the node at the index - 1
        previous_node = self.get(index - 1)
        # setting the next_node
        next_node = previous_node.next

        # set the next of the previous_node to the new_node
        previous_node.next = new_node
        # set the prev of the new_node to the previous_node
        new_node.prev = previous_node
        # set the next of the new_node to the next_node
        new_node.next = next_node
        # set the prev of the next_node to the new_node
        next_node.prev = new_node

        # increment the length by 1
        self.length += 1

        # return True

    def remove(self,index):
        # checking if the index is valid or not and if the head is None
        if index < 0 or index >= self.length or self.head is None:
            return None
        
        # if the index is 0, pop the first element and return the value
        if index == 0:
            return self.pop_first()
        
        # if the index is equal to the length - 1, pop the last element and return the value
        if index == self.length - 1:
            return self.pop()
        
        # get the node at the index-1
        previous_node = self.get(index - 1)
        # get the node at the index
        node = previous_node.next
        # get the node at the index + 1
        next_node = node.next

        # set the next of the previous_node to the next_node
        previous_node.next = next_node
        # set the prev of the next_node to the previous_node
        next_node.prev = previous_node
        # set the next of the node to None
        node.next = None
        # set the prev of the node to None
        node.prev = None

        # decrement the length by 1
        self.length -= 1

        # return the value of the node
        return node.value
        