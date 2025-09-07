# Last updated: 08/09/2025, 01:25:12
class Solution:
    def myAtoi(self, s: str) -> int:
        s=list(s)
        neg=False
        num=0
        nums=["0","1","2","3","4","5","6","7","8","9"]
        i=0
        print(s)
        if s==[]:
            return 0
        while s[0]==" ":
            s.pop(0)
            if s==[]:
                return 0
        print(s)
        if s[0]=="+" or s[0]=="-":
            if s[i]=="-":
                neg=True
            s.pop(0)
        for i in s:
            if i not in nums:
                break
            elif int(i)>=0 and int(i)<=9:
                num+=int(i)
                num*=10
        num=num//10
        if neg:
            if (-1)*num<(-1)*pow(2,31):
                return (-1)*pow(2,31)
            return (-1)*num
        else:
            if num>pow(2,31)-1:
                return pow(2,31)-1
            return num

        