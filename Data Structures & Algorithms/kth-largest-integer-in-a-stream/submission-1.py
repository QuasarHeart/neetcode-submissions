import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # 1. 初始化时建堆（只需执行这一次）
        heapq.heapify(self.nums)
        
        # 2. 如果初始元素超过 k 个，把多余的较小数全部弹出，只留最大的 k 个
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # 3. 新元素入堆
        heapq.heappush(self.nums, val)
        
        # 4. 如果堆的大小超过了 k，弹出当前最小的那个，保持堆大小始终为 k
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        # 5. 堆顶（第 0 个元素）永远是这 k 个最大数里最小的，即全局第 k 大！
        return self.nums[0]
