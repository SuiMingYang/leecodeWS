class Solution:
    def rob(self, nums) -> int:
        m = len(nums)

        if not m:
            return 0

        dp = [0] * (m + 1)

        dp[1] = nums[0]

        for i in range(1,m):

            dp[i+1] = max(dp[i], dp[i-1]+nums[i])

        return dp[-1]

obj=Solution()
print(obj.rob([111,2,3,111,3,2]))
print(obj.rob([2,2,311,3,211,1]))
print(obj.rob([2,2,311,311,2,3]))