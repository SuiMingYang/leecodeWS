class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        mn=min(len(strs[0]),len(strs[1]),len(strs[2]))
        k=-1
        for i in range(mn):
            if strs[0][i]==strs[1][i] and strs[2][i]==strs[1][i]:
                k=i
            else:
                break
        if k!=-1:
            return strs[0][0:k+1]
        else:
            return ""

obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))


