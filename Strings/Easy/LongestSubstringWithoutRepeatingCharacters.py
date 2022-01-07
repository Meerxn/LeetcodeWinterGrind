class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currStr = set()
        left = 0
        currMax = 0
        for i in range(len(s)):
            while(s[i] in currStr):
                currStr.remove(s[left])
                left+=1
            currStr.add(s[i])
            currMax = max(currMax,i-left + 1)
        return currMax
            
                
        
        