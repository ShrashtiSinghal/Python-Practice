class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        bitwisexor= 0
        for i in range (n):
            nums.append(start+(2*i))
            bitwisexor= bitwisexor ^ nums[i]
        return bitwisexor
        