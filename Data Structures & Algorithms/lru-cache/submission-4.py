from collections import deque,defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.frq = deque()
        self.capacity = capacity
        self.hashmap = {}
        self.key_count = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.frq.append(key)
            self.key_count[key]+=1
            return self.hashmap[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.frq.append(key)
        self.key_count[key]+=1
        self.hashmap[key]=value

        while len(self.hashmap) > self.capacity:
            old_key = self.frq.popleft()
            self.key_count[old_key]-=1

            if self.key_count[old_key] == 0:
                self.hashmap.pop(old_key)

        

           
                
            
        
