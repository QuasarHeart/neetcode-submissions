import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first == second:
                continue
            if first > second:
                heapq.heappush(max_heap,-(first-second))

        if not max_heap:
            return 0
        else:
            return -max_heap[0]




        

        