class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False


    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()

            node = node.children[char]

        node.isEnd = True


        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            # 从第 index 个字符开始，沿着当前 node 往下找
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # 遇到通配符 '.'：遍历当前节点的所有子节点，逐个递归尝试匹配后面的字符 (i + 1)
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    # 所有分支都试过了，全都不行，返回 False
                    return False
                else:
                    # 普通字母：照常往下走
                    if char not in node.children:
                        return False
                    node = node.children[char]
            
            # 整个 word 都遍历完了，看最后停下的节点是不是单词结尾
            return node.isEnd

        return dfs(0, self)


            
        
        
