class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length= len(nums)//2
        newList=[]
        for i in range(length):
            newList.append(nums[i])
            newList.append(nums[length+i])
        return newList