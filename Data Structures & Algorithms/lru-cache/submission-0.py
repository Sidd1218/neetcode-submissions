class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        else:
            node = self.nodes[key]
            self.remove(node)
            self.add_to_front(node)
            return node.value
                
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.remove(node)
            self.add_to_front(node)
            return

        node = Node(key, value)
        self.nodes[key] = node
        self.add_to_front(node)

        if len(self.nodes) > self.capacity:
            least_recent = self.tail.prev
            self.remove(least_recent)
            del self.nodes[least_recent.key]
