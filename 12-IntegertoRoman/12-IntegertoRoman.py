# Last updated: 09/09/2025, 10:27:52
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num+=i
            num*=10
        num=num//10
        num+=1
        res=[]
        while num>0:
            res.append(num%10)
            num=num//10
        print(res)
        res.reverse()
        return res