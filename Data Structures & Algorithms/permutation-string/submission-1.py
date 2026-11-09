from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        first = 0
        second = len_s1-1
        s1_dict = Counter(s1)
        while second < len_s2:
            if s1_dict == Counter(s2[first:second+1]):
                return True
            second+=1
            first+=1

        return False

        

        
