# Last updated: 25/05/2025, 21:12:22
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        # chars=[" ",",",":",".","@","$","%","^","&","*","#","_","-","!","~","`","'",'"',"/","\"]
        # for i in chars:
        #     s=s.replace(i,"")
        temp=[x for x in s if x.isalnum()]
        temp1=[y for y in s if y.isalnum()]
        # chars=[' ',',',':']
        # for i in chars:
        #     if i in temp:
        #         temp.remove(i)
        #         temp1.remove(i)
        temp1.reverse()
        print(temp)
        print(temp1)
        if temp==temp1:
            return True
        return False