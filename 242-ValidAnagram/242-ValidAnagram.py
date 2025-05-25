# Last updated: 25/05/2025, 21:12:13
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp=[x for x in s]
        temp1=[y for y in t]
        temp.sort()
        temp1.sort()
        if temp==temp1:
            return True
        return False