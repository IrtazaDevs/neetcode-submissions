class Solution:

    def isValid(self,s: str) -> bool:

        closed = {')':'(',']':'[','}':'{'}
        stack = []

        for c in s:
            if c not in closed: # this means its an open bracket
                stack.append(c) 
            else: # also need to cater for closed bracked
                 if len(stack) == 0:
                    return False # because closed bracket is here without any opening one
                 else:
                    popped = stack.pop()
                    if popped != closed[c]:
                        return False
        return len(stack) == 0


