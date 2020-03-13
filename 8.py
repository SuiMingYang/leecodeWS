import re
class Solution:
    def myAtoi(self, str: str) -> int:
        try:
            str=re.search(r'(-?[\d]+)',str,re.M|re.I).group(1)
        except Exception as e:
            return 0
        num=int(str)
        if num>2**31-1:
            return 2**31-1
        elif num<-2**31:
            return -2**31
        else:
            return num


obj=Solution()
print(obj.myAtoi('"words and 987"'))
print(obj.myAtoi('jskh-123'))
print(obj.myAtoi('jskh123'))
print(obj.myAtoi(''))