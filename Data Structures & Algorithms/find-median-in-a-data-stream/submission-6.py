import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # 最大堆（存负数），存放较小的一半
        self.large = []  # 最小堆（存正数），存放较大的一半

    def addNum(self, num: int) -> None:
        # 1. 先把新数字无脑塞进左边的最大堆（记得取负号）
        heapq.heappush(self.small, -num)
        
        # 2. 保证有序性：把左边最大的数弹出来，交给右边的最小堆
        # 这样可以确保 small 里的所有数一定小于等于 large 里的所有数
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # 3. 保证数量平衡：我们约定允许 small 比 large 多 1 个元素
        # 如果右边的数量反超了左边，就把右边最小的数还给左边
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    def findMedian(self) -> float:
        # 如果总数是奇数，左边比右边多 1 个，直接返回左边堆顶
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # 如果总数是偶数，两边一样多，取两个堆顶的平均值
        return (-self.small[0] + self.large[0]) / 2.0

