from collections import Counter
class Solution:
    def numSmallerByFrequency(self, queries, words):
        # def count(s):
        #     t='z'
        #     c=0
        #     for i in range(len(s)):
        #         if s[i]==t:
        #             c+=1
        #         elif s[i]<t:
        #             c=1
        #             t=s[i]
        #         else:
        #             continue

        #     return c
        
        # for i in range(len(queries)):
        #     queries[i]=count(queries[i])
        
        # for i in range(len(words)):
        #     words[i]=count(words[i])

        # res=[]
        # for q in queries:
        #     z=0
        #     for w in words:
        #         if w>q:
        #             z+=1
        #     res.append(z)
        # return res
        for i in range(len(queries)):
            queries[i]=Counter(list(queries[i]))[min(list(Counter(list(queries[i])).keys()))]
        for i in range(len(words)):
            words[i]=Counter(list(words[i]))[min(list(Counter(list(words[i])).keys()))]
        res=[]
        for q in queries:
            z=0
            for w in words:
                if w>q:
                    z+=1
            res.append(z)
        return res

                    
obj=Solution()
print(obj.numSmallerByFrequency(["cbd"],["zaaaz"]))


