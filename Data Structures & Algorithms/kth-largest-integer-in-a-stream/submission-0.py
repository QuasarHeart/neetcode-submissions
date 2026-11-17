import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # heapq.heapify(self.nums)
        # heapq.heappush(self.nums,val)
        # self.nums[self.k]
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]

