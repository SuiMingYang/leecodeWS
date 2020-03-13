class Solution:
    def rob(self, nums) -> int:
        
        
        if not :
            return 0
        nums=nums+[nums[0]]
        m = 
        dp = [0] * (m + 1)

        dp[1] = nums[0]

        for i in range(1,m):
            if i==m-1:
                if dp[i]<dp[i-1]+nums[i]:
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = dp[i]
            else:
                dp[i+1] = max(dp[i], dp[i-1]+nums[i])

        return dp[-1]

obj=Solution()
print(obj.rob([2,3,2]))
