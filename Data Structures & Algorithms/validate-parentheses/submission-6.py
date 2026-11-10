class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}',
            '[':']',
        }
        stack = []
        for string in s:
            if string == '(' or string == '{' or string == '[':
                stack.append(string)
            else:
                if not stack: return False
                if mapping[stack[-1]] == string:
                    stack.pop()
                else:
                    return False


        if not stack:
            return True
        else:
            return False
