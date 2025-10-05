from hmac import new
from platform import node


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self.__insert(self.root, val)

    
    def __insert(self, root, val):

        if root is None:
            new_node = Node(val)
            root = new_node
            return
        
        if val < root.val:
            if root.left is None:
                new_node = Node(val)
                root.left = new_node

            else:
                self.__insert(root.left,val)

        else:
            if root.right is None:
                new_node = Node(val)
                root.right = new_node

            else:
                self.__insert(root.right, val)


    def __print_inorder(self,node):
        if node.left:
            self.__print_inorder(node.left)

        print(node.val)

        if node.right:
            self.__print_inorder(node.right)

    def print_inorder(self):
        self.__print_inorder(self.root)


bst = BST(15)
import random

random_arr = [random.randint(1,25) for i in range(10)]

for i in random_arr:
    bst.insert(i)

bst.print_inorder()