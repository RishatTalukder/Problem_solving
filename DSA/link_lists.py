"""
Full Linked list using Python and every line is explained with a comment after the line 
"""


# Node class to create new node
class Node:
    def __init__(self, Value=0) -> None:  # constructor to create new node
        self.value = Value  # value of the node
        self.next = None  # points to the next node


# linked list class to execute all the functions and methods of a linked list
class LinkedList:
    def __init__(self, value):  # constructor to create a linked list
        new_node = Node(value)  # create a new node
        # as the linkde list was empty the head and tail points to the new node
        self.head = new_node  # head points to the new node
        self.tail = new_node  # tail points to the new node
        self.length = 1  # length of the linked list is 1

    # function to print the linked list
    def print_list(self):
        temp = self.head  # temp points to the head

        if self.head is None:  # if the linked list is empty
            print("Linked list is empty")

        while temp is not None:  # checking if there is a node linked to the temp value
            print(
                temp.value
            )  # if a node is connected print the value of the current temp value
            temp = temp.next  # then set the next node a the new temp

    # function to add an element to the linked list
    def append(self, value):
        new_node = Node(value)  # create a new node
        if self.head is None:  # if the linked list is empty
            self.head = new_node  # head points to the new node
            self.tail = new_node  # tail points to the new node too

        else:
            self.tail.next = new_node  # only the tail points to the new node
            self.tail = new_node  # now the tail points to the new node

        self.length += 1  # increase the length

        return True

    # function the last element from the linked list
    def pop(self):
        if self.length == 0:  # if the linked list is empty
            return None

        else:
            temp = self.head  # tempp points to the head
            pre = temp

            while (
                temp.next is not None
            ):  # checking if there is a node linked to the temp value
                pre = temp  # pre points to the current temp value
                temp = temp.next  # then set the next value as the new temp

            self.tail = pre  # now the tail points to the pre value
            self.tail.next = None  # now the tail points to nothing
            self.length -= 1  # decrease the length

            if (
                self.length == 0
            ):  # checking if the linked list is empty after decreasing the length
                # we have to fix the issue of head and tail still pointing to the temp value
                self.head = None  # head points to nothing
                self.tail = None  # tail points to nothing

            return temp

    # function to add an element to the Linked list
    def prepend(self, value):
        new_node = Node(value)  # create a new node
        if self.head is None:  # checking if the linked list is empty
            self.head = new_node  # head points to the new node
            self.tail = new_node  # tail points to the new node too

        else:
            new_node.next = (
                self.head
            )  # as we are adding to the head, the new node points to the head
            self.head = new_node  # as the new node is the head, assigning the new node to the head

        self.length += 1  # increase the length

        return True

    # function to remove the first element
    def pop_first(self):
        temp = self.head  # settting temp as the head
        if self.head is None:  # checking if the linked list is empty
            return None

        else:
            self.head = self.head.next  # now the head points to the next
            temp.next = None  # now temp points to nothing
            self.length -= 1

            if self.length == 0:  # checking if the linked list is empty
                self.tail = None  # now the tail points to nothing

        return temp

    # fucntion to get the value of an index
    def get(self, index):
        if index < 0 or index >= self.length:  # checking if the index is out of range
            return None

        else:
            temp = self.head  # setting temp as the head
            for _ in range(index):  # going through the list to find the right index
                temp = temp.next  # resetting temp as the next value

            return temp

    # function to set the value of an index
    def set(self, index, value):
        temp = self.get(index)  # getting the value of the index using the get method
        if temp:  # checking if the index exists
            temp.value = value  # setting the value
            return True

        return False

    # inseritng an element to the linked list
    def insert(self, index, value):
        if index < 0 or index > self.length:  # checking if the index is out of range
            return "shit"

        if index == 0:  # checking if the index is 0
            return self.prepend(value)  # insert using the prepend method

        if index == self.length:  # checking if the index is the last index
            return self.append(value)  # insert using the append method

        else:
            new_node = Node(value)  # create a new node
            temp = self.get(index - 1)  # getting the vnode in the index
            new_node.next = temp.next
            temp.next = new_node  # setting the next value of the node to the new node
            self.length += 1
            return True

    # removing a item from the linked list
    def remove(self, index):
        if index < 0 or index >= self.length:  # checking if the index is out of range
            return False

        if index == 0:
            return self.pop_first()  # removing using the pop method

        if index == self.length - 1:
            return self.pop()  # removing using the pop method

        else:
            pre = self.get(index - 1)  # getting the previous node in the index
            temp = pre.next  # setting temp as the next value
            pre.next = (
                temp.next
            )  # setting the next value of the previous node to the next value of the temp
            temp = None  # now temp points to nothing
            self.length -= 1  # decreasing the length
            return True

    # finally reversing a linked list
    def reverse(self):
        """step 1 :
        swapping the head and tail"""
        temp = self.head
        self.head = self.tail
        self.tail = temp

        """step 2:
        taking three variables to iterate through the linked list
        temp,before,after"""
        before = None  # previous node

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    # creating the linked list
    linked_list1 = LinkedList(2)
    linked_list1.append(4)
    linked_list1.append(6)
    linked_list1.insert(1, 23)

    print(linked_list1.print_list())
