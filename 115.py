class Solution(object): 
    def numDistinct(self, s: str, t: str) -> int:
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls, lt = len(s), len(t)
        dp = [1] + [0] * lt
        for i in range(ls):
            for k in range(lt - 1, -1, -1): #不能改为正向，dp数组要用上次外循环的
                if s[i] == t[k]:
                    dp[k + 1] += dp[k]
        return dp[lt]
    

obj=Solution()
print(obj.numDistinct("babbbab", "bab"))