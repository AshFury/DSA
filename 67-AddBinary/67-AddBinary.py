# Last updated: 11/09/2025, 09:49:01
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        for i in range(0,(x//2)+2):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1
            else:
                continue
    

        