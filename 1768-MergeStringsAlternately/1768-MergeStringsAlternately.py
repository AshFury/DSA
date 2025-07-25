# Last updated: 12/07/2025, 19:13:53
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 +str1:
            return ""
        max_length = gcd(len(str1),len(str2))
        return str1[:max_length]
        