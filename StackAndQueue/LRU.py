

# Class representing the LRU Cache
class LRUCache:
    # Doubly linked list node class
    class Node:
        # Constructor to initialize node
        def __init__(self, _key, _val):
            self.key = _key
            self.val = _val
            self.next = None
            self.prev = None

    # Constructor to initialize LRU cache
    def __init__(self, capacity: int):
        # Head and tail dummy nodes
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Capacity of cache
        self.cap = capacity
        # Hash map to store key-node mapping
        self.m = {}

    # Function to add a node right after head
    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    # Function to remove a given node from list
    def deleteNode(self, delNode):
        delPrev = delNode.prev
        delNext = delNode.next
        delPrev.next = delNext
        delNext.prev = delPrev

    # Function to get value from cache
    def get(self, key_):
        # If key exists in cache
        if key_ in self.m:
            resNode = self.m[key_]
            res = resNode.val
            # Remove old mapping
            del self.m[key_]
            # Move accessed node to front
            self.deleteNode(resNode)
            self.addNode(resNode)
            # Update map
            self.m[key_] = self.head.next
            return res
        # If not found
        return -1

    # Function to put key-value into cache
    def put(self, key_, value):
        # If key already exists
        if key_ in self.m:
            existingNode = self.m[key_]
            del self.m[key_]
            self.deleteNode(existingNode)
        # If capacity reached
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        # Insert new node at front
        self.addNode(self.Node(key_, value))
        self.m[key_] = self.head.next


# Driver code
if __name__ == "__main__":
    # Create cache with capacity 2
    cache = LRUCache(2)

    # Put values in cache
    cache.put(1, 1)
    cache.put(2, 2)

    # Get value for key 1
    print(cache.get(1))

    # Insert another key (evicts key 2)
    cache.put(3, 3)

    # Key 2 should be evicted
    print(cache.get(2))

    # Insert another key (evicts key 1)
    cache.put(4, 4)

    # Key 1 should be evicted
    print(cache.get(1))

    # Key 3 should be present
    print(cache.get(3))

    # Key 4 should be present
    print(cache.get(4))