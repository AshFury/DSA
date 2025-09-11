# Last updated: 11/09/2025, 09:35:16
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        max_len=max(len(a),len(b))
        carry=0
        for i in range(0,max_len):
            a_pos=(len(a)-1)-i
            b_pos=(len(b)-1)-i
            if a_pos>=0 and b_pos>=0:
                if a[a_pos]=="1" and b[b_pos]=="1":
                    if carry==1:
                        print("here")
                        res.append(1)
                    else:
                        print("here")
                        res.append(0)
                    carry=1
                elif a[a_pos]=="1" and b[b_pos]=="0":
                    if carry==1:
                        res.append(0)
                        carry=1
                    else:
                        res.append(1)
                        carry=0
                elif a[a_pos]=="0" and b[b_pos]=="1":
                    if carry==1:
                        res.append(0)
                        carry=1
                    else:
                        res.append(1)
                        carry=0
                else:
                    if carry==1:
                        res.append(1)
                    else:
                        res.append(0)
                    carry=0
            elif a_pos>=0 and b_pos<0:
                if a[a_pos]=="1":
                    if carry==1:
                        res.append(0)
                        carry=1
                    else:
                        res.append(1)
                        carry=0
                else:
                    if carry==1:
                        res.append(1)
                        carry=0
                    else:
                        res.append(0)
                        carry=0
            elif b_pos>=0 and a_pos<0:
                if b[b_pos]=="1":
                    if carry==1:
                        res.append(0)
                        carry=1
                    else:
                        res.append(1)
                        carry=0
                else:
                    if carry==1:
                        res.append(1)
                        carry=0
                    else:
                        res.append(0)
                        carry=0
        if carry==1:
            res.append(1)
            carry=0
        print(res)
        res.reverse()
        print(len(a))
        s=""
        for i in res:
            s=s+str(i)
        return s