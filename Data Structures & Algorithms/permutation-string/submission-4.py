from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        first = 0
        second = len_s1-1
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[first:second+1])

        while second < len_s2:
            if s1_dict == s2_dict:
                return True
            if second+1 >= len_s2:
                break


            
            s2_dict[s2[first]]-=1
            if s2_dict[s2[first]] == 0:
                del s2_dict[s2[first]]
        
                
            second+=1
            first+=1
            s2_dict[s2[second]] = s2_dict.get(s2[second], 0) + 1
        return False

        

        
