# Last updated: 25/05/2025, 21:12:40
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        str1=""
        for r in range(0,numRows):
            increment=2*(numRows-1)
            for i in range(r,len(s),increment):
                str1+=s[i]
                if(r>0 and r<numRows-1 and (i+increment-(2*r))<len(s)):
                    str1+=s[(i+increment-(2*r))]
        return str1