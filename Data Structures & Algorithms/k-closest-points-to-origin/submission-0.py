import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = x * x + y * y
            heapq.heappush(min_heap, (dist, point))
            
        output = []
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            output.append(point)
            
        return output



    