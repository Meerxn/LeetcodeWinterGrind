class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for val in nums:
            if val in numSet:
                return True
            else:
                numSet.add(val)
        return False
        