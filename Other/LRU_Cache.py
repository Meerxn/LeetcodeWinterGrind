class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class LRUCache:

  
        
        
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.main_cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

        
    def insert(self,node):
        previous_node = self.right.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.right
        self.right.prev = node
        
        
        
    def remove (self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.main_cache:
            self.remove(self.main_cache[key])
            self.insert(self.main_cache[key])
            return self.main_cache[key].value
        else:
            return -1
        
        
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.main_cache:
            self.remove(self.main_cache[key])
        self.main_cache[key] = Node(key,value)
        self.insert(self.main_cache[key])
        if len(self.main_cache.keys()) > self.capacity:
            leftmost = self.left.next
            self.remove(leftmost)
            del self.main_cache[leftmost.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)