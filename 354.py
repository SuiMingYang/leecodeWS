class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        width=0
        height=0
        length=[]
        for [w,h] in envelopes:
            if w<=width and h<=height:
                length+=1
            


obj=Solution()
print(obj.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])