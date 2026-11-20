class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        
        res = []
        path = []  # 用来存放当前拼出来的字母，比如 ['d', 'g']

        def backtrack(index: int):
            # 1. 终止条件：已经处理完 digits 里的所有数字
            if index == len(digits):
                res.append("".join(path))  # 把 ['d', 'g'] 拼成字符串 "dg" 存进去
                return

            # 2. 找到当前层数字对应的字母表（例如 digits[0] == "3" -> "def"）
            current_digit = digits[index]
            letters = hashmap[current_digit]

            # 3. 遍历当前数字对应的每一个字母
            for char in letters:
                path.append(char)
                print(path)       # 做选择：选一个字母（比如 'd'）
                backtrack(index + 1)    # 递归：去选下一个数字（index + 1）的字母
                path.pop()
                print(path)                # 撤销选择：把 'd' 拿出来，下次循环试 'e'

        backtrack(0)
        return res





