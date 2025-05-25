# Last updated: 25/05/2025, 21:12:01
class Solution:
    def maximumTime(self, time: str) -> str:
        chars=time.split(":")
        hr=[x for x in chars[0]]
        minutes=[x for x in chars[1]]
        if len(hr)>1:
            if hr[0]=="?":
                if hr[1]=="?":
                    hr[0]="2"
                    hr[1]="3"
                elif int(hr[1])>3:
                    hr[0]=1
                else:
                    hr[0]=2
            if hr[1]=="?":
                if hr[0]=="?":
                    hr[0]="2"
                    hr[1]="3"
                elif hr[0]=="0":
                    hr[1]="9"
                elif hr[0]=="1":
                    hr[1]="9"
                elif hr[0]=="2":
                    hr[1]="3"
        if len(minutes)>1:
            if minutes[1]=="?":
                minutes[1]="9"
            if minutes[0]=="?":
                minutes[0]="5"
        res=""
        for i in hr:
            res=res+str(i)
        res=res+":"
        for j in minutes:
            res=res+str(j)
        return res
            