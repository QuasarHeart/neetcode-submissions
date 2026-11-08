class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s[:-1]
        # s = str(s.split())
        # s = s.lower()
        # length = len(s)
        # for idx in range(length//2):
        #     if s[idx] == s[length-idx-1]:
        #         continue
        #     else:
        #         return False

        # return True

        clean_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean_s == clean_s[::-1]
