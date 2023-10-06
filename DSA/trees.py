# Define a Node class to represent a node in a binary search tree
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


# Define a BinarySearchTree class to represent a binary search tree
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # Define an insert method to insert a new node into the binary search tree
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True

        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False

                if value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True

                    else:
                        temp = temp.left

                else:
                    if temp.right == None:
                        temp.right = new_node
                        return True

                    else:
                        temp = temp.right

    # Define a contains method to check if a value is present in the binary search tree
    def contains(self, value):
        if self.root == None:
            return False

        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right

            else:
                return True

        return False


# If this file is run directly, create a binary search tree and test it
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)
    print(tree.contains(36))
