# Last updated: 25/05/2025, 21:12:18
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>0:
            temp=nums.pop()
            nums.insert(0,temp)
            k=k-1