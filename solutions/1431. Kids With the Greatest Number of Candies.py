class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = max(candies)
        boollist=[]
        #print (great)
        for x in candies:
            if (x + extraCandies) >= great:
                boollist.append(1)
            else:
                boollist.append(0)
        return boollist
                