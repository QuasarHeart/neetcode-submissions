from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for line in board:

            hashmap = Counter(line)
            length = len(hashmap)
            if length == 9:
                continue
                
            num_of_dots = hashmap["."]
            if length+num_of_dots!=10:
                return False

        transposed = list(map(list,zip(*board)))
        for line in transposed:
            hashmap = Counter(line)
            length = len(hashmap)
            if length == 9:
                continue
                
            num_of_dots = hashmap["."]
            if length+num_of_dots!=10:
                return False

        for i in range(1,4):
            for j in range(1,4):
                block = [row[3*(j-1):3*j] for row in board[3*(i-1):3*i]]
                hashmap = Counter(sum(block,[]))
                length = len(hashmap)
                if length == 9:
                    continue
                
                num_of_dots = hashmap["."]
                if length+num_of_dots!=10:
                    return False

        return True


                