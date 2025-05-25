# Last updated: 25/05/2025, 21:12:09
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i=0
        stones.sort()
        stones.reverse()
        while i<len(stones)-1:
            temp=stones[0]
            stones.pop(0)
            stones[0]=abs(abs(stones[0])-abs(temp))
            while stones[0]==0:
                stones.pop(0)
                if len(stones)==0:
                    return 0
            stones.sort()
            stones.reverse()
        if len(stones)==0:
            return 0
        return stones[0]