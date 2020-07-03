class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        prod=0
        while(x!=0):
            rem=x%10
            print (rem)
            prod=prod*10+rem
            print(prod)
            x=x//10
        
        if prod> (2**31) -1:
            return 0
        else:
            return prod*sign
        