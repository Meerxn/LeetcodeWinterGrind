class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        OPT = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    OPT[i] = max(OPT[i],1+OPT[j])
        return max(OPT)