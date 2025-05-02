class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            val = node.val
            self.remove(node)
            self.add(node)
            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)

        if len(self.hashmap) == self.cap:
            self.remove(self.tail.prev)

        self.add(Node(key, value))



    def remove(self,node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        del self.hashmap[node.key]

    def add(self, node):
        after = self.head.next
        node.next = after
        node.prev = self.head
        self.head.next = node
        after.prev = node
        self.hashmap[node.key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)