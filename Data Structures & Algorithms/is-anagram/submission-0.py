class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}


        for letter in s:
            if letter in hashmap_s:
                hashmap_s[letter]+=1
            else:
                hashmap_s[letter]=1
        
        for letter in t:
            if letter in hashmap_t:
                hashmap_t[letter]+=1

            else:
                hashmap_t[letter]=1

        if hashmap_s==hashmap_t:
            return True

        return False