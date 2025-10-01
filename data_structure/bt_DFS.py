from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def __init__(self, val):
        self.root = Node(val)

    def print_BFS(self):
        q = []
        if self.root:
            q.append(self.root)

        while q:
            level = []

            for node in q:
                print(node.val)
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            q = level

    def print_BFS_2(self):
        q = deque([self.root])

        while q:
            node = q.popleft()
            print(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    def print_inorder(self,node):
        if node.left:
            self.print_inorder(node.left)

        print(node.val)

        if node.right:
            self.print_inorder(node.right)

    def print_preorder(self,node):
        print(node.val)

        if node.left:
            self.print_preorder(node.left)

        if node.right:
            self.print_preorder(node.right)

    def print_postorder(self,node):
        if node.left:
            self.print_postorder(node.left)

        if node.right:
            self.print_postorder(node.right)

        print(node.val)


bt = BT(1)
bt.root.left = Node(2)
bt.root.right = Node(4)
bt.root.left.left = Node(3)
bt.root.left.right = Node(5)

# bt.print_inorder(bt.root)
# bt.print_preorder(bt.root)
bt.print_postorder(bt.root)