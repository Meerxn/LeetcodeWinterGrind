from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for val in s:
            if val == "(" or val == "{" or val == "[":
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                if val == '}':
                    if stack.pop() != "{":
                        return False
                if val == ']':
                    if stack.pop() != "[":
                        return False
                if val == ')':
                    if stack.pop() != "(":
                        return False
        if len(stack)!=0:
            return False
        return True
                