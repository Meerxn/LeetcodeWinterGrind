class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) -1
        while left < right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    right-=1
                    left+=1
        return True
            
        
        