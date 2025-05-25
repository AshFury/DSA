# Last updated: 25/05/2025, 21:12:06
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list=s.split(" ")
        maxlen=0
        for i in s_list:
            if len(i)>maxlen:
                maxlen=len(i)
        for i in range(len(s_list)):
            s_list[i]=s_list[i]+" "*(maxlen-len(s_list[i]))
        res=["" for i in range(maxlen)]

        for i in s_list:
            for j in range(len(i)):
                res[j]+=i[j]
        for i in range(len(res)):
            res[i]=res[i].rstrip()
        return res
        