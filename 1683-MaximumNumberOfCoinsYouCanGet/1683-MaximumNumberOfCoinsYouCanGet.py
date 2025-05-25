# Last updated: 25/05/2025, 21:12:03
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        f=0
        l=len(piles)-2
        res=0
        piles.sort()
        while f<l:
            res=res+piles[l]
            f+=1
            l-=2
        return res

            
