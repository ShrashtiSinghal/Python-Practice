class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorlist=[1]
        for i in range (2, n+1):
            if n%i==0:
                factorlist.append(i)
        
        print (factorlist)
        if len(factorlist)>=(k):
            return (factorlist[k-1])
        else:
            return -1
        