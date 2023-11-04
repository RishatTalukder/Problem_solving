# Define a Node class to represent a node in a binary search tree
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


# Define a BinarySearchTree class to represent a binary search tree
class BinarySearchTree:
    """
    A class representing a binary search tree.

    Attributes:
    -----------
    root : Node
        The root node of the binary search tree.

    Methods:
    --------
    insert(value)
        Inserts a new node with the given value into the binary search tree.
    contains(value)
        Checks if a node with the given value is present in the binary search tree.
    """

    def __init__(self) -> None:
        """
        Initializes an empty binary search tree.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a new node with the given value into the binary search tree.

        Parameters:
        -----------
        value : int
            The value to be inserted into the binary search tree.

        Returns:
        --------
        bool
            True if the value was successfully inserted, False otherwise.
        """
        new_node = Node(value)

        # If the tree is empty, set the new node as the root node
        if self.root == None:
            self.root = new_node
            return True

        # Otherwise, traverse the tree to find the correct position to insert the new node
        else:
            temp = self.root
            while True:
                # If the value already exists in the tree, return False
                if new_node.value == temp.value:
                    return False

                # If the value is less than the current node's value, traverse left
                if value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True

                    else:
                        temp = temp.left

                # If the value is greater than the current node's value, traverse right
                else:
                    if temp.right == None:
                        temp.right = new_node
                        return True

                    else:
                        temp = temp.right

    def contains(self, value):
        """
        Checks if a node with the given value is present in the binary search tree.

        Parameters:
        -----------
        value : int
            The value to be searched for in the binary search tree.

        Returns:
        --------
        bool
            True if a node with the given value is present in the binary search tree, False otherwise.
        """
        if self.root == None:
            return False

        temp = self.root

        # Traverse the tree until the value is found or the end of the tree is reached
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
