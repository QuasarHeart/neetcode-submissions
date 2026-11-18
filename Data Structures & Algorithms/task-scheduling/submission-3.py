from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        hashmap = Counter(tasks)
        length = len(hashmap)
        gap = n+1
        longest = max(hashmap.values())
        num = longest-1
        total = 0
        for key,val in hashmap.items():
            if val <= num:
                hashmap[key] = 0
            else:
                hashmap[key] -= num

            total+=hashmap[key]
        return max(num*gap+total,len(tasks))