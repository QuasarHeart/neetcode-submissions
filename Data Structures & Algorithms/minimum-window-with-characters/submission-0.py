from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        window_count = {}
        
        # required 是 t 中独特字符的数量
        required = len(t_count)
        # formed 用来记录当前窗口内满足 t 中频次要求的独特字符数量
        formed = 0
        
        left = 0
        # 记录最小窗口的长度，以及它的左右边界坐标
        ans = float("inf"), 0, 0
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # 如果当前字符在 t 中，且频次达到了 t 的要求，formed + 1
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
                
            # 当窗口已经完全覆盖了 t 的所有字符时，尝试收缩左边界
            while left <= right and formed == required:
                # 更新全局最短答案
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # 准备把 left 指向的字符踢出窗口
                removed_char = s[left]
                window_count[removed_char] -= 1
                
                # 如果踢掉它之后，导致它的频次低于 t 的要求了，formed - 1
                if removed_char in t_count and window_count[removed_char] < t_count[removed_char]:
                    formed -= 1
                    
                left += 1  # 左边界右移
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

            

            




            
