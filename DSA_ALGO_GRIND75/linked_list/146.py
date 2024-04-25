from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        return
    

## SOlution using doubly linked list

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    """
    A class representing a Least Recently Used (LRU) Cache.

    The LRUCache class implements a cache with a fixed capacity. It supports two operations:
    - get(key): Get the value of the key if the key exists in the cache, otherwise return -1.
    - put(key, value): Set or insert the value if the key is not already present. When the cache reaches its capacity,
      it should invalidate the least recently used item before inserting a new item.

    Attributes:
        capacity (int): The maximum number of items the cache can hold.
        cache (dict): A dictionary to store the key-value pairs.
        head (Node): The head of the doubly linked list representing the most recently used items.
        tail (Node): The tail of the doubly linked list representing the least recently used items.

    Methods:
        get(key: int) -> int:
            Get the value of the key if it exists in the cache, otherwise return -1.
            This method also updates the position of the accessed item in the cache.

        put(key: int, value: int) -> None:
            Set or insert the value for the given key.
            If the key already exists in the cache, update its value and move it to the most recently used position.
            If the cache is full, remove the least recently used item before inserting the new item.

        add(node: Node) -> None:
            Add a node to the cache and update the linked list.

        remove(node: Node) -> None:
            Remove a node from the cache and update the linked list.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with the given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists in the cache, otherwise return -1.
        This method also updates the position of the accessed item in the cache.

        Args:
            key (int): The key to retrieve the value for.

        Returns:
            int: The value of the key if it exists in the cache, otherwise -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Set or insert the value for the given key.
        If the key already exists in the cache, update its value and move it to the most recently used position.
        If the cache is full, remove the least recently used item before inserting the new item.

        Args:
            key (int): The key to set or insert the value for.
            value (int): The value to be associated with the key.

        Returns:
            None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        if len(self.cache) == self.capacity:
            self.remove(self.head.next)
        self.add(Node(key, value))
        return

    def add(self, node):
        """
        Add a node to the cache and update the linked list.

        Args:
            node (Node): The node to be added to the cache.

        Returns:
            None
        """
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.cache[node.key] = node
        return

    def remove(self, node):
        """
        Remove a node from the cache and update the linked list.

        Args:
            node (Node): The node to be removed from the cache.

        Returns:
            None
        """
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)