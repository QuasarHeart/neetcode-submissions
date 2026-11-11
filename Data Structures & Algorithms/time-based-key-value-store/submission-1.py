from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            left = 0
            right = len(self.hashmap[key])-1
            while left<=right:
                mid = (left+right)//2
                if self.hashmap[key][mid][0] == timestamp:
                    return self.hashmap[key][mid][1]
                elif timestamp>self.hashmap[key][mid][0]:
                    left = mid+1
                else:
                    right = mid-1
            if right<0:
                return ""
            return self.hashmap[key][right][1]

        return ""


        
        
