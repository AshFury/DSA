# Last updated: 25/05/2025, 21:12:17
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        # if nums[0]==nums[len(nums)//2]:
        #     return nums[0]
        # else:
        #     return nums[len(nums)-1]