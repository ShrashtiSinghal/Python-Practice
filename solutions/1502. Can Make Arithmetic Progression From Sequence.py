class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        count=0
        diff=arr[1]-arr[0]
        print (arr)
        for i in range (2,len(arr)):
            if diff != (arr[i])-(arr[i-1]):
                count=1
                break
        if count==0:
            return 1
        else:
            return 0