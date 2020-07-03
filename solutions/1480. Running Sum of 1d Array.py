class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumnums= [0]
        for x in nums:
            sumnums.append(sumnums[-1]+x)
        
        sumnums.pop(0)
        return sumnums