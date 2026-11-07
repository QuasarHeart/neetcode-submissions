from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        
        for string in strs:
            # 创建一个长度为 26 的全 0 计数列表
            count = [0] * 26
            for char in string:
                # 利用 ord() 计算字母在 26 个槽位中的索引
                count[ord(char) - ord('a')] += 1
            
            # 列表是不可变的，但转成 tuple 就可以作为哈希表的键了！
            hashmap[tuple(count)].append(string)
            
        return list(hashmap.values())



            




            
