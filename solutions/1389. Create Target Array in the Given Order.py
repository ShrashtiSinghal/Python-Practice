class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i in range (len(index)):
            target.insert(index[i],nums[i])
            #print (nums[index[i]])
            #print (index[i])
        return target
            
    