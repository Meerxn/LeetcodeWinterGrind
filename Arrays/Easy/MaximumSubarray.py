import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        currSum = 0
        for val in nums:
            if currSum < 0:
                currSum = 0
            currSum+= val
            currMax = max(currMax,currSum)
        return currMax
            
            
    
            