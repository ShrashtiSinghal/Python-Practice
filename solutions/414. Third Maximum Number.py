class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setlist= set(nums)
        nums=list(setlist)
        nums.sort(reverse=True)
        if len(nums)<3:
            return nums[0]
        else:
            return nums[2]
        
        
        
        
