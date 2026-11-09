class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 哈希表：记录当前窗口内每个字符的频次
        left = 0
        max_count = 0  # 窗口内出现次数最多的字符的数量
        longest = 0
        
        for right in range(len(s)):
            # 1. 右指针进窗口，更新哈希表
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. 更新窗口内主导字符的最大频次
            max_count = max(max_count, count[s[right]])
            
            # 3. 如果整个窗口长度减去主导字符频次（即杂质数量）大于 k
            # 说明替换机会不够了，左指针必须右移来缩小窗口
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            # 4. 此时窗口必然合法，更新最大长度
            longest = max(longest, right - left + 1)
            
        return longest

            
                
