# Last updated: 07/09/2025, 19:58:27
class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        res=0
        vals={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i=0
        while i<n:
            if i==n-1:
                res=res+vals[s[i]]
                i+=1
            else:
                if s[i]=="I":
                    if s[i+1]=="V":
                        res=res+4
                        i+=2
                    elif s[i+1]=="X":
                        res=res+9
                        i+=2
                    else:
                        res=res+vals[s[i]]
                        i+=1
                elif s[i]=="X":
                    if s[i+1]=="L":
                        res=res+40
                        i+=2
                    elif s[i+1]=="C":
                        res=res+90
                        i+=2
                    else:
                        res=res+vals[s[i]]
                        i+=1
                elif s[i]=="C":
                    if s[i+1]=="D":
                        res=res+400
                        i+=2
                    elif s[i+1]=="M":
                        res=res+900
                        i+=2
                    else:
                        res=res+vals[s[i]]
                        i+=1
                else:
                    res=res+vals[s[i]]
                    i+=1
        return res



            
            
            
        