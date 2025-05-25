# Last updated: 25/05/2025, 21:12:29
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rep=nums[0]
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=rep:
                rep=nums[i]
                nums[j]=nums[i]
                j+=1
            # print(nums)
        return j


        