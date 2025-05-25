# Last updated: 25/05/2025, 21:12:33
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            fp=i+1
            ep=len(nums)-1
            while(fp<ep):
                # if fp>0 and nums[fp]==nums[fp]-1:
                #     fp=fp+1
                #     continue
                # if ep<len(nums)-1 and nums[ep]==nums[ep]+1:
                #     ep=ep-1
                #     continue
                if nums[i]+nums[fp]+nums[ep]==0:
                    res.append([nums[i],nums[fp],nums[ep]])
                    fp=fp+1
                    while(nums[fp]==nums[fp-1] and fp<ep):
                        fp=fp+1
                elif nums[i]+nums[fp]+nums[ep]>0:
                    ep=ep-1
                else:
                    fp=fp+1
        return res

    


        