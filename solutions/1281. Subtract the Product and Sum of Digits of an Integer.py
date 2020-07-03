class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumdi=0
        prod=1
        while n!=0:
            rem=n%10
            prod=prod*rem
            sumdi = sumdi +rem
            n=n//10
        return prod-sumdi