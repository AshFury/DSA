# Last updated: 14/09/2025, 18:12:15
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

    # max product ending at the current index
        currMax = nums[0]

    # min product ending at the current index
        currMin = nums[0]

    # Initialize overall max product
        maxProd = nums[0]

    # Iterate through the numsay
        for i in range(1, n):

        # Temporary variable to store the maximum product ending
        # at the current index
            temp = max(nums[i], nums[i] * currMax, nums[i] * currMin)

        # Update the minimum product ending at the current index
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)

        # Update the maximum product ending at the current index
            currMax = temp

        # Update the overall maximum product
            maxProd = max(maxProd, currMax)

        return maxProd
