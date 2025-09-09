# Last updated: 09/09/2025, 10:22:06
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        start=False
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if s[i]==" " and not start:
                continue
            elif s[i]==" " and start:
                return res
            else:
                start=True
                res+=1
        return res
        