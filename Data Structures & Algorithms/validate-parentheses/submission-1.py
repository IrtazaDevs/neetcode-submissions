class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        map = {')': '(', ']': '[', '}':'{'}
        
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

                