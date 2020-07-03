class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        count=0
        for i in range (1,len(A)):
            substring= A[i-1 : (i+1)]
            newsubstring= A[i] +A[i-1]
            print (substring)
            print(newsubstring)
            Z= A[0:i-1]+newsubstring + A[i+1:]
            print(Z)
            print (B)
            if newsubstring in B and Z==B:
                count=1
            Z=""
        if count==1:
            return 1
        else:
            return 0
                
            
        