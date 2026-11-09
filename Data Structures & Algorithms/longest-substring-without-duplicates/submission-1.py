class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1]*128
        longest = 0
        length = len(s)
        first = 0
        
        for second in range(length):
            char_code = ord(s[second])
            if last_seen[char_code] >= first:
                first = last_seen[char_code]+1

            last_seen[char_code] = second
            longest = max(longest,second-first+1)

        
        return longest
        