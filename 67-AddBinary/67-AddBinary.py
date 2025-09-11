# Last updated: 11/09/2025, 10:49:45
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        low=0
        high=len(nums)
        vals=[]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                vals.append(mid)
                temp=mid
                while nums[temp]==target:
                    temp-=1
                    if temp>=0 and temp<len(nums):
                        if nums[temp]==target:
                            vals.append(temp)
                    else:
                        break
                temp=mid
                while nums[temp]==target:
                    temp+=1
                    if temp>=0 and temp<len(nums):
                        if nums[temp]==target:
                            vals.append(temp)
                    else:
                        break
                break
        return [min(vals),max(vals)]


        