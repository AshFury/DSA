# Last updated: 08/09/2025, 00:06:47
class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if x<0:
            neg=True
        x=abs(x)
        if x>pow(2,31)-1:
            return 0
        lis=[]
        while x>0:
            lis.append(x%10)
            x=x//10
        num=0
        print(lis)
        for i in range(0,len(lis)):
            num+=lis[i]
            if i!=len(lis)-1:
                num*=10
        if neg and num<=pow(2,31)-1:
            return (-1)*num
        elif not neg and num<=pow(2,31)-1:
            return num
        else:
            return 0

        