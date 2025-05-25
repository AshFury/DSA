# Last updated: 25/05/2025, 21:12:05
class Solution:
    def minOperations(self, n: int) -> int:
        if n%2!=0:
            target=2*(n//2)+1
            vals=0
            i=1
            while i<target:
                vals=vals+target-i
                i+=2
            return vals
        else:
            targeta=2*(n//2)+1
            targeta-=1
            targetb=2*(n//2)-1
            targetb+=1
            vals=0
            i=1
            while i<targetb:
                vals=vals+targetb-i
                i+=2
            return vals
