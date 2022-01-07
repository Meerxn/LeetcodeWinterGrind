class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countRes = {}
        currMax = 0
        l = 0
        r = 0 
        for r in range(len(s)):
            countRes[s[r]] = 1+ countRes.get(s[r],0)
            if -1*max(countRes.values()) +  r - l + 1 > k:
                countRes[s[l]] -= 1
                l += 1
            currMax = max(currMax,r-l+1)
        return currMax
        