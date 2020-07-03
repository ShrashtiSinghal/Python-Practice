class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newlist=[]
        length= len(nums)
        for i in range(length):
            count=0
            for j in range(length):
                if (nums[i] > nums[j] ) and (i != j):
                    count=count+1
            
            newlist.append(count)
        
        return newlist