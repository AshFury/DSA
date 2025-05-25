# Last updated: 25/05/2025, 21:12:10
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        l=0
        mid=1
        r=2
        while r<len(flowerbed):
            if flowerbed[l]==0 and flowerbed[mid]==0 and flowerbed[r]==0:
                n=n-1
                flowerbed[mid]=1
            l+=1
            mid+=1
            r+=1
        if n<=0:
            return True
        else:
            return False
