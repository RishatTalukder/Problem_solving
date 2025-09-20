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

bt = BT(1)
bt.root.left = Node(2)
bt.root.right = Node(4)
bt.root.left.left = Node(3)
bt.root.left.right = Node(5)

bt.print_BFS()

bt.print_BFS_2()