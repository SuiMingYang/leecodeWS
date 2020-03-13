class Solution:
    def reverse(self, x: int) -> int:
        s=int(str(x)[::-1].replace('-',''))
        if s>2**31:
            return 0
        else:
            if x>0:
                return s
            else:
                return 0-s



obj=Solution()
print(obj.reverse(210))
print(obj.reverse(1534236469))