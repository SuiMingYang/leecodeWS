class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        return self.fn(n)
        
    def fn(self,n):
        if n==0:
            return 1
        if n==1:
            return 10
        if n>10:
            return 0
        f = 9
        i = 1
        while i<n and i<=10:
            f *= 10-i
            i+=1
        return f+self.fn(n-1)


s = Solution()
# print(s.isMatch('aaabc', 'a*bc'))


print('3',s.countNumbersWithUniqueDigits(0))
print('3',s.countNumbersWithUniqueDigits(1))
print('3',s.countNumbersWithUniqueDigits(2))
print('3',s.countNumbersWithUniqueDigits(3))
print('4',s.countNumbersWithUniqueDigits(4))
print('5',s.countNumbersWithUniqueDigits(5))