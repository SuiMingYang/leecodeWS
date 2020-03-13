class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(p):
            if p[j]=='*':

            elif p[j]=='?':
                i+=1
                j+=1
            elif p[j]==s[i]:

            else:

            

obj=Solution()
print(obj.isMatch("adceb","*a*b"))