class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        checker = set()
        res = []
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] >0:
                return res
            if nums[i] == nums[i-1] and i > 0:
                continue
                
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                        
                        
                        
                    
                elif nums[left] + nums[right] + nums[i] > 0 :
                    right -=1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
        return res
            
                    
        