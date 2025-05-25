# Last updated: 25/05/2025, 21:12:23
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        res=0
        temp=0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
                if r<len(prices)-1:
                    r=l+1
            else:
                temp=prices[r]-prices[l]
                r=r+1
                res=max(temp,res)
        return res

