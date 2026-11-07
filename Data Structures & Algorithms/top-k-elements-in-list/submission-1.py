from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        hashmap = sorted(hashmap,key=hashmap.get,reverse=True)
        return hashmap[:k]