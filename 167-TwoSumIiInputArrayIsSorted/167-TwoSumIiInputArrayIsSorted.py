# Last updated: 25/05/2025, 21:12:19
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp=0
        ep=len(numbers)-1
        while(fp<ep):
            if numbers[fp]+numbers[ep]==target:
                return [fp+1,ep+1]
            elif numbers[fp]+numbers[ep]>target:
                ep=ep-1
            else:
                fp=fp+1