# Last updated: 25/05/2025, 21:12:39
class Solution:
    def reverse(self, x: int) -> int:
        neg=0
        if x<0:
            neg=1
        x=abs(x)
        rev=0
        while x!=0:
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(rev>(pow(2,31)-1)):
            return 0
        if neg==1:
            rev=rev*(-1)
        return rev

