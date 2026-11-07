from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hashmap = {}
        
        for idx,string in enumerate(strs):
            hashmap_temp = tuple(sorted(Counter(string).items()))
            if hashmap_temp in hashmap:
                hashmap[hashmap_temp].append(idx)
            else:
                hashmap[hashmap_temp]=[idx]

        for value in hashmap.values():
            output_temp = []
            for idx in value:
               
               output_temp.append(strs[idx])

            output.append(output_temp)

        return output


            




            
