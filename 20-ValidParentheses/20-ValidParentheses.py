# Last updated: 25/05/2025, 21:12:32
class Solution:
    def isValid(self, s: str) -> bool:
        chars=[0]*6
        close=[]
        for i in s:
            if i=="(":
                chars[0]+=1
                close.append("(")
            elif i==")":
                chars[1]+=1
                if len(close)>0 and close[len(close)-1]!="(":
                    return False
                if len(close)>0:
                    close.pop()
                else:
                    return False
            elif i=="{":
                chars[2]+=1
                close.append("{")
            elif i=="}":
                chars[3]+=1
                if len(close)>0 and close[len(close)-1]!="{":
                    return False
                if len(close)>0:
                    close.pop()
                else:
                    return False
            elif i=="[":
                chars[4]+=1
                close.append("[")
            elif i=="]":
                chars[5]+=1
                if len(close)>0 and close[len(close)-1]!="[":
                    return False
                if len(close)>0:
                    close.pop()
                else:
                    return False
        if chars[0]==chars[1] and chars[2]==chars[3] and chars[4]==chars[5]:
            return True
        else:
            return False
