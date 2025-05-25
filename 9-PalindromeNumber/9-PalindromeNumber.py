# Last updated: 25/05/2025, 21:12:37
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1=str(x)
        print(str1)
        lis=list(str1)
        print(lis)
        lis2=list(reversed(lis))
        print(lis2)
        for i in range(0,len(lis)):
            if lis[i]!=lis2[i]:
                return False
        return True