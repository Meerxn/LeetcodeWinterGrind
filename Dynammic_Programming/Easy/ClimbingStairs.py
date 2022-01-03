# My solution
class Solution:
    def climbStairs(self, n: int) -> int:
        OPT = [1,2]
        if n <=2:
            return OPT[n-1]
        for i in range(2,n):
            OPT.append(OPT[i-2]+ OPT[i-1])
        return OPT[n-1]