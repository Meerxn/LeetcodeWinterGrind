class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        
        
        def swap(i,j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        def reverse(start,end):
            while start < end:
                swap(start,end)
                end-=1
                start +=1
        if len(nums) <= 1:
            return
        if len(nums) == 2:
            return swap(0,1)
        dec = len(nums) -2
        while dec >= 0 and nums[dec] >= nums[dec+1]:
            dec -=1
        reverse(dec+1,len(nums)-1)
        if dec == -1:
            return
        else:
            next_num = dec + 1
            while next_num < len(nums) -1 and nums[next_num] <= nums[dec]:
                next_num+=1
            swap(next_num,dec)
        
            
        """
        Do not return anything, modify nums in-place instead.
        """
       

        
        
        