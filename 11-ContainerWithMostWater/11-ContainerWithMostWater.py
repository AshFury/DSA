# Last updated: 25/05/2025, 21:12:36
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        i=0
        j=len(height)-1
        while i<j:
            area=abs(i-j)*min(height[i],height[j])
            print(area)
            if area>maxi:
                maxi=area
            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
        return maxi
