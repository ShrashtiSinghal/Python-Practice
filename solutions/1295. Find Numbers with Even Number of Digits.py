class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for x in nums:
            if len(str(x))%2==0:
                count=count+1
        return count