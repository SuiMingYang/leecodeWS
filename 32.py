class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left=0
        tag=[]
        ready=[]
        i=0
        for t in s:
            if t=='(':
                left+=1
                ready.append(i)#坐标
                tag.append('1')
                i+=1
            elif t==')':
                if left>0:
                    left-=1
                    tag[ready[len(ready)-1]]='2'
                    ready.pop()#配对出栈
                else:#无法配对的右括号
                    ready.append(i)
                    tag.append('1')
                    i+=1
        tag=[len(item)*2 for item in ''.join(tag).split('1')]
        return sorted(tag)[-1]


obj=Solution()
print(obj.longestValidParentheses(")()())"))