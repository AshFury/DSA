# Last updated: 08/09/2025, 01:37:42
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1=list(haystack)
        l2=list(needle)
        i=0
        j=0
        while i<len(l1):
            if l1[i]==l2[j]:
                i+=1
                j+=1
                if j==len(l2):
                    print("hi")
                    return i-j
            else:
                i-=j
                j=0
                i+=1
        return -1

        