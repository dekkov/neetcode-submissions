class Node:
    def __init__(self, key = "", val = 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.node_map = {} # key: node
        self.capacity = capacity
        self.size = 0
        

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # key already exists
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return

        # cache is full
        if len(self.node_map) >= self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.node_map[lru.key]

        # add new node
        newN = Node(key, value)
        self.node_map[key] = newN
        self.add(newN)
        
        
        










