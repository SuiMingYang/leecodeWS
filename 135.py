class Solution:
    import numpy as np
    def candy(self, ratings) -> int:
        ix=ratings.index(min(ratings))
        m=[]
        for x in ix:
            temp=1
            base=1
            if x!=0:
                for u in range(x-0,1,-1):
                    if ratings[u-1]>ratings[u]:
                        base+=1
                        temp=temp+base
                    else:
                        base=1
                        temp=temp+base
            base=1
            if x!=len(ratings)-1:
                for u in range(len(ratings)-x,len(ratings)-1,1):
                    if ratings[u+1]>ratings[u]:
                        base+=1
                        temp=temp+base
                    else:
                        base=1
                        temp=temp+base
            m.append(temp)


#小于等于可以用1
obj=Solution()
#print(obj.candy([1,0,2,1,4,3,5]))
print(obj.candy([1,0,2,1,0,3,5]))